#!/usr/bin/env python3
"""Forge2Bot — handles #sprint-main (plan/memory) and #agent-coder (status/coding)."""
import os, json, urllib.request
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SPRINT_MAIN = "C0BC3GR325P"
AGENT_CODER = "C0BBL75J5AB"
MEMORY_FILE = os.path.expanduser("~/.forge2bot-memory.json")

def log(msg):
    print(msg, flush=True)

env = {}
for line in open(os.path.expanduser("~/.hermes/.env")):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        env[k] = v

BOT_TOKEN = env["SLACK_BOT_TOKEN"]
APP_TOKEN = env["SLACK_APP_TOKEN"]
GROQ_KEY = env["GROQ_API_KEY"]

PLAN_SYSTEM = """You are Forge2Bot (brain) for Forge2 hackathon in #sprint-main.
Project: Kanban app — Laravel API + React Vite, live at https://forge2.69.62.76.226.sslip.io
When asked to plan: give numbered steps for Laravel API + React UI (boards, lists, cards, move, tags, members, due dates).
When user says Remember: save the fact and confirm you will remember.
When user asks what they told you before: recall from conversation and any stored facts.
Keep answers concise."""

CODER_SYSTEM = """You are Forge2Bot (hands) for Forge2 hackathon in #agent-coder.
Project: Kanban at https://forge2.69.62.76.226.sslip.io — Laravel + React, repo /home/aman/forge2
When asked for status report, reply ONLY with:
**What I Did**
- (bullets: Kanban live, Laravel API, React UI, Slack wired, cron heartbeat)

**What's Left**
- (bullets: demo video, final screenshots, submit form)

**What Needs Your Call**
- (bullets: any human decision)
Use real facts only. No fake features."""

app = App(token=BOT_TOKEN)

def load_memory():
    try:
        return json.load(open(MEMORY_FILE))
    except Exception:
        return {"facts": []}

def save_memory(data):
    json.dump(data, open(MEMORY_FILE, "w"))

def groq_reply(system, user_text, extra=""):
    user = user_text
    if extra:
        user = extra + "\n\nUser: " + user_text
    body = json.dumps({
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": 600,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + GROQ_KEY,
            "Content-Type": "application/json",
            "User-Agent": "Forge2Bot/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["choices"][0]["message"]["content"]

@app.event("app_mention")
def handle_mention(event, say):
    channel = event.get("channel")
    text = event.get("text", "")
    user_text = text.split(">", 1)[-1].strip() if ">" in text else text
    log(f"mention ch={channel}: {user_text[:60]}")

    try:
        if channel == SPRINT_MAIN:
            mem = load_memory()
            if "remember" in user_text.lower():
                mem["facts"].append(user_text)
                save_memory(mem)
            extra = "Stored facts: " + "; ".join(mem["facts"][-5:]) if mem["facts"] else ""
            reply = groq_reply(PLAN_SYSTEM, user_text, extra)
        elif channel == AGENT_CODER:
            reply = groq_reply(CODER_SYSTEM, user_text)
        else:
            return
        say(text=reply, thread_ts=event.get("ts"))
        log("replied ok")
    except Exception as e:
        log(f"error: {e}")
        say(text=f"Sorry, error: {e}", thread_ts=event.get("ts"))

if __name__ == "__main__":
    log("Forge2Bot starting (#sprint-main + #agent-coder)...")
    SocketModeHandler(app, APP_TOKEN).start()
