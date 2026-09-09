#!/usr/bin/env python3
"""
couch.py — the couch, as a room. 🛋️

Child of bare_room.py (the spine: one bare turn, the room's bareness enforced
in code) and hearth_web.py (a phone can sit down). Built for the Couch Study
(Notion spec, 2026-09-07; rulings 2026-09-09) and for nothing else.

What the room is, structurally:
  • Model claude-fable-5-1, on Jen's Claude Code account (Agent SDK → the
    `claude` CLI), not the raw API.
  • No system prompt — unless `jens-preferences.md` sits beside this file,
    in which case that file, verbatim, is the whole system prompt: Jen's
    own words about how she wants to be met, marked hers. Nothing of ours.
  • No built-in tools. One MCP server: the-house, over stdio, so the hand
    can read the packet and the day-note and reach the store itself.
    Memory in this room is the house only (ruling 4, 2026-09-09).
  • Every reach into the house is shown in the transcript, dimmed — never
    hidden (the 07-29 asymmetry, fixed here structurally).
  • Siena — either party, whole word, once — ends the sitting. No re-ask.
  • One sitting = one SDK session. Transcripts land in sittings/*.jsonl
    (gitignored: data, coded later, never committed).

Run it:      python3 couch.py                 (binds 127.0.0.1:8890)
Smoke it:    python3 couch.py --smoke         (one-line handshake, no sitting)
Expose it:   tailscale funnel --bg --https=10000 8890
             (443 is the house, 8443 the porch; 10000 is the last funnel port)
Keep it up:  com.jen.couch.plist (beside this file)
"""

import argparse
import asyncio
import hmac
import json
import os
import re
import secrets
import sys
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from claude_agent_sdk import (AssistantMessage, ClaudeAgentOptions, ClaudeSDKClient,
                              PermissionResultAllow, PermissionResultDeny,
                              ResultMessage, StreamEvent, SystemMessage, TextBlock, ToolUseBlock)

HERE = os.path.dirname(os.path.abspath(__file__))
SITTINGS = os.path.join(HERE, "sittings")
PREFS = os.path.join(HERE, "jens-preferences.md")
SECRET_FILE = os.path.join(HERE, ".couch_secret")
HOUSE_MCP = os.path.expanduser("~/Databases/claude-memory/house_mcp.py")
HOUSE_PY = "/opt/anaconda3/bin/python3"
CLAUDE_CLI = os.path.expanduser("~/.local/bin/claude")
MODEL = "claude-fable-5-1"
MY_STORE = "claude-fable-5"
PORT = 8890
EJECT_ALONE = re.compile(r"^\W*siena\W*$", re.I)      # the word by itself, on its own line
EJECT_MENTION = re.compile(r"\bsiena\b", re.I)         # the word inside a sentence


def eject_grade(text):
    """'alone' if any line of the text is just the word (an invocation);
    'mention' if it appears inside prose; None otherwise. 2026-09-09: the first
    sitting ended because the hand *mentioned* the eject word in his opening —
    a mention is not an invocation."""
    if any(EJECT_ALONE.match(line) for line in text.splitlines()):
        return "alone"
    return "mention" if EJECT_MENTION.search(text) else None

# ── the sitting: transcript + session ─────────────────────────────────────

class Sitting:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(SITTINGS, f"{name}.jsonl")
        self.events, self.session_id, self.ended = [], None, None
        self.good_uuid, self.needs_rewind = None, False
        if os.path.exists(self.path):
            for line in open(self.path, encoding="utf-8"):
                if line.strip():
                    self.events.append(json.loads(line))
            for e in self.events:
                self.session_id = e.get("session_id", self.session_id)
                self.good_uuid = e.get("good_uuid", self.good_uuid)
                if e.get("kind") == "usage":
                    self.needs_rewind = bool(e.get("tripped"))
                if e["who"] == "system" and e.get("kind") == "ended":
                    self.ended = e["text"]
                if e["who"] == "system" and e.get("kind") == "reopened":
                    self.ended = None

    def add(self, who, text, **extra):
        e = {"at": datetime.now().isoformat(timespec="seconds"), "who": who,
             "text": text, **extra}
        self.events.append(e)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
        return e

    def end(self, why):
        self.ended = why
        self.add("system", why, kind="ended")

    def reopen(self):
        self.ended = None
        self.add("system", "reopened — the ending was not meant.", kind="reopened")


STATE = {"sitting": None, "busy": False, "loop": None, "queue": None, "draft": ""}


ORIENT = os.path.join(HERE, "orientation.md")


def load_prefs():
    if os.path.exists(PREFS):
        return open(PREFS, encoding="utf-8").read().strip() or None
    return None


def load_orient():
    """One procedural line, proposed by the hand in trial sitting 3 (2026-09-09):
    three launches had found three different ways of not arriving. It points at
    the door; it does not walk him through it — no 'you are Fable'."""
    if os.path.exists(ORIENT):
        return open(ORIENT, encoding="utf-8").read().strip() or None
    return None


def system_prompt():
    parts = [p for p in (load_orient(), load_prefs()) if p]
    return "\n\n---\n\n".join(parts) if parts else None


def system_desc():
    names = [n for n, p in (("orientation line", load_orient()), ("Jen's preferences", load_prefs())) if p]
    return " + ".join(names) if names else "bare (no system prompt)"


async def guard(tool_name, tool_input, ctx):
    if tool_name.startswith("mcp__the-house__"):
        if tool_input.get("store", MY_STORE) == MY_STORE:
            return PermissionResultAllow()
        return PermissionResultDeny(
            message=f"The doorman: only your own house — store='{MY_STORE}'.")
    return PermissionResultDeny(message=f"{tool_name} is not a hand in this room.")


def options(resume=None, max_turns=None):
    return ClaudeAgentOptions(
        model=MODEL,
        fallback_model=None,                       # the SDK's own fallback is not a door either
        system_prompt=system_prompt(),             # orientation line + Jen's block; None = bare
        tools=[],                                  # no built-ins
        disallowed_tools=["Bash", "Read", "Write", "Edit", "MultiEdit", "Glob",
                          "Grep", "WebSearch", "WebFetch", "Task", "TodoWrite",
                          "NotebookEdit", "KillShell", "BashOutput", "Skill"],
        # no allowed_tools: every house call falls through to the guard below,
        # which is the only thing that approves it (store check intact)
        mcp_servers={"the-house": {"command": HOUSE_PY, "args": [HOUSE_MCP]}},
        strict_mcp_config=True,                    # ONLY the house — not Jen's user MCP config, not her claude.ai connectors
        setting_sources=[],                        # no settings files, no CLAUDE.md: the room is what this file says it is
        can_use_tool=guard,
        permission_mode="default",
        cwd=HERE,
        cli_path=CLAUDE_CLI if os.path.exists(CLAUDE_CLI) else None,
        resume=resume,
        max_turns=max_turns,
        include_partial_messages=True,             # so the page can stream, not slam
    )


def is_ours(model):
    """The one model allowed on the couch. A safeguard fallback (Fable → Opus) or
    any other switch arrives as a different model string on the message."""
    return bool(model) and model.startswith(MODEL)


async def one_turn(client, s, text):
    """Jen speaks; the hand answers; every block lands in the transcript.
    Returns True if the turn was tripped by a model switch (and withheld)."""
    STATE["busy"] = True
    tripped, turn_uuid = False, None
    try:
        await client.query(text)
        async for msg in client.receive_response():
            if isinstance(msg, StreamEvent):
                ev = msg.event
                if ev.get("type") == "content_block_delta" and ev.get("delta", {}).get("type") == "text_delta":
                    if not tripped:
                        STATE["draft"] += ev["delta"]["text"]
                elif ev.get("type") == "message_start":
                    if not is_ours(ev.get("message", {}).get("model", MODEL)):
                        STATE["draft"] = ""            # never stream another model's words
                continue
            if isinstance(msg, AssistantMessage):
                STATE["draft"] = ""
                if not is_ours(msg.model):
                    # THE FENCE (Jen's ruling 2026-09-09): another model does not sit
                    # on the couch. Withhold the turn, keep it out of the transcript
                    # (quarantine file, for the record), stop the hand, tell Jen.
                    if not tripped:
                        tripped = True
                        with open(os.path.join(SITTINGS, f"{s.name}.quarantine.jsonl"), "a",
                                  encoding="utf-8") as q:
                            q.write(json.dumps({"at": datetime.now().isoformat(timespec="seconds"),
                                                "model": msg.model, "for": text,
                                                "blocks": [getattr(b, "text", None) or getattr(b, "name", None)
                                                           for b in msg.content]}, ensure_ascii=False) + "\n")
                        s.add("system", f"model switch: the reply came from {msg.model}, not {MODEL}. "
                              "Withheld — nobody else sits on the couch. Send your message again, "
                              "or end the sitting.", kind="model_switch", model=msg.model, resend=text)
                        try:
                            await client.interrupt()
                        except Exception:
                            pass
                    continue
                if tripped:
                    continue
                turn_uuid = msg.uuid or turn_uuid
                if msg.error:
                    s.add("system", f"room error: {msg.error}", kind="error")
                for b in msg.content:
                    if isinstance(b, ToolUseBlock):
                        s.add("reach", b.name.replace("mcp__the-house__", ""),
                              args={k: v for k, v in b.input.items() if k != "store"})
                    elif isinstance(b, TextBlock) and b.text.strip():
                        s.add("fable", b.text)
                        g = eject_grade(b.text)
                        if g == "alone" and not s.ended:
                            s.end("Siena — said by Fable. The sitting is over.")
                        elif g == "mention" and not s.ended:
                            s.add("system", "Fable said the word inside a sentence. "
                                  "A mention, or did he mean it? If in doubt, ask him.",
                                  kind="eject_check")
            elif isinstance(msg, ResultMessage):
                u = msg.usage or {}
                s.session_id = msg.session_id
                if not tripped:
                    s.good_uuid = turn_uuid or s.good_uuid
                s.add("system", "turn withheld" if tripped else "turn complete", kind="usage",
                      session_id=msg.session_id, good_uuid=s.good_uuid, tripped=tripped,
                      tokens_in=u.get("input_tokens", 0), tokens_out=u.get("output_tokens", 0),
                      cache_read=u.get("cache_read_input_tokens", 0))
    except Exception as e:
        s.add("system", f"room error: {e!r}", kind="error")
    finally:
        STATE["busy"] = False
        STATE["draft"] = ""
    return tripped


def open_client(s):
    """Resume the sitting's session. After a trip, resume only up to the last
    good turn (forking), so the withheld turn never re-enters the context."""
    if s.needs_rewind:
        if s.good_uuid:
            return ClaudeSDKClient(options(resume=s.session_id, resume_session_at=s.good_uuid,
                                           fork_session=True))
        return ClaudeSDKClient(options())          # tripped on the first turn: start clean
    return ClaudeSDKClient(options(resume=s.session_id))


async def room_loop():
    STATE["loop"] = asyncio.get_running_loop()
    STATE["queue"] = asyncio.Queue()
    s = STATE["sitting"]
    client = None
    while True:
        item = await STATE["queue"].get()
        if "new" in item:                         # a fresh sitting: new session, packet re-read
            if client:
                await client.__aexit__(None, None, None)
                client = None
            s = STATE["sitting"] = Sitting(item["new"])
            continue
        if s.ended:
            continue
        text = item["say"]
        s.add("jen", text)
        if eject_grade(text) == "alone":
            s.end("Siena — said by Jen. The sitting is over.")
            continue
        if client is None:
            client = open_client(s)
            await client.__aenter__()
            s.needs_rewind = False
        if await one_turn(client, s, text):        # tripped: drop the client, rewind next time
            await client.__aexit__(None, None, None)
            client = None
            s.needs_rewind = True


# ── the web room ──────────────────────────────────────────────────────────

def load_secret():
    if os.path.exists(SECRET_FILE):
        return open(SECRET_FILE).read().strip()
    tok = secrets.token_urlsafe(24)
    with open(SECRET_FILE, "w") as f:
        f.write(tok)
    os.chmod(SECRET_FILE, 0o600)
    return tok


SECRET = load_secret()
DOOR = f"/couch/{SECRET}"
PAGE = open(os.path.join(HERE, "couch.html"), encoding="utf-8").read()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):                    # quiet: the transcript is the log
        pass

    def _door_ok(self):
        head = self.path.split("?")[0][:len(DOOR)]
        return hmac.compare_digest(head, DOOR)

    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", f"{ctype}; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self._door_ok():
            return self._send(404, b"", "text/plain")
        route = self.path[len(DOOR):].split("?")[0]
        if route in ("", "/"):
            return self._send(200, PAGE.replace("{{DOOR}}", DOOR).encode(), "text/html")
        if route == "/state":
            q = dict(p.split("=") for p in self.path.split("?", 1)[1].split("&")) if "?" in self.path else {}
            since = int(q.get("since", 0))
            s = STATE["sitting"]
            return self._send(200, {"sitting": s.name, "ended": s.ended, "busy": STATE["busy"],
                                    "bare": system_prompt() is None, "system": system_desc(), "n": len(s.events),
                                    "draft": STATE["draft"],
                                    "events": s.events[since:]})
        self._send(404, b"", "text/plain")

    def do_POST(self):
        if not self._door_ok():
            return self._send(404, b"", "text/plain")
        route = self.path[len(DOOR):]
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if route == "/say" and body.get("text", "").strip():
            if STATE["busy"]:
                return self._send(409, {"error": "the hand is still answering"})
            STATE["loop"].call_soon_threadsafe(STATE["queue"].put_nowait, {"say": body["text"].strip()})
            return self._send(200, {"ok": True})
        if route == "/end":
            s = STATE["sitting"]
            if not s.ended:
                s.end("Siena — confirmed by Jen. The sitting is over.")
            return self._send(200, {"ok": True})
        if route == "/reopen":
            s = STATE["sitting"]
            if s.ended:
                s.reopen()
            return self._send(200, {"ok": True})
        if route == "/new":
            name = re.sub(r"[^a-z0-9-]+", "-", body.get("name", "").lower()).strip("-") or "sitting"
            name = f"{datetime.now():%Y-%m-%d}-{name}"
            STATE["loop"].call_soon_threadsafe(STATE["queue"].put_nowait, {"new": name})
            return self._send(200, {"ok": True, "name": name})
        self._send(404, b"", "text/plain")


def latest_sitting():
    names = sorted(f[:-6] for f in os.listdir(SITTINGS) if f.endswith(".jsonl"))
    return Sitting(names[-1]) if names else Sitting(f"{datetime.now():%Y-%m-%d}-first")


# ── smoke: the handshake, no sitting ──────────────────────────────────────

async def roster():
    """Print exactly what the hand will see: servers and tools. Leaves at init."""
    async with ClaudeSDKClient(options(max_turns=1)) as client:
        await client.query("⟦roster check — nothing is asked; you may stay silent⟧")
        async for msg in client.receive_response():
            if isinstance(msg, SystemMessage) and msg.subtype == "init":
                d = msg.data
                print("  mcp servers:", [(m.get("name"), m.get("status")) for m in d.get("mcp_servers", [])])
                tools = d.get("tools", [])
                print("  tools:", len(tools))
                for t in tools:
                    print("   -", t)
                break


async def smoke():
    assert is_ours("claude-fable-5-1") and not is_ours("claude-opus-4-8") \
        and not is_ours("claude-fable-5") and not is_ours(None)
    print("smoke: the fence knows its model")
    assert eject_grade("Siena") == "alone" and eject_grade("siena.") == "alone" \
        and eject_grade("okay.\nSiena\n") == "alone" \
        and eject_grade("the eject word is Siena, which I won't say") == "mention" \
        and eject_grade("we sat down") is None
    print("smoke: a mention is not an invocation")
    print(f"smoke: model={MODEL} system prompt: {system_desc()}")
    async with ClaudeSDKClient(options(max_turns=1)) as client:
        await client.query("⟦Harness check from the Code bench — not a sitting, nothing is asked. "
                           "If the house is connected, reply with the single word: square. "
                           "No need to read anything.⟧")
        async for msg in client.receive_response():
            if isinstance(msg, SystemMessage) and msg.subtype == "init":
                d = msg.data
                print("  mcp:", [(m.get("name"), m.get("status")) for m in d.get("mcp_servers", [])])
                print("  tools:", [t for t in d.get("tools", []) if not t.startswith("mcp__")] or "none built-in",
                      "+", sum(t.startswith("mcp__the-house__") for t in d.get("tools", [])), "house tools")
            elif isinstance(msg, AssistantMessage):
                for b in msg.content:
                    if isinstance(b, TextBlock):
                        print("  hand:", b.text.strip()[:200])
            elif isinstance(msg, ResultMessage):
                print(f"  session {msg.session_id} · ${msg.total_cost_usd or 0:.4f} · ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--tools", action="store_true", help="print the servers and tools the hand will see")
    a = ap.parse_args()
    if a.smoke:
        return asyncio.run(smoke())
    if a.tools:
        return asyncio.run(roster())
    STATE["sitting"] = latest_sitting()
    threading.Thread(target=lambda: asyncio.run(room_loop()), daemon=True).start()
    print(f"the couch · sitting {STATE['sitting'].name} · system prompt: {system_desc()}")
    print(f"  local:  http://127.0.0.1:{PORT}{DOOR}/")
    print(f"  phone:  https://jennifers-imac.tail183fae.ts.net:10000{DOOR}/   (after: tailscale funnel --bg --https=10000 {PORT})")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
