#!/usr/bin/env python3
import os, json, urllib.request
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

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
CHANNEL = "C0BBL75J5AB"

SYSTEM = """You are Forge2Bot, the coding agent for the Forge2 Edition 1 hackathon qualifier.

PROJECT FACTS (use only these, do not invent features):
- Built a Kanban board app: Laravel 13 API + React Vite frontend + SQLite
- Live URL: https://forge2.69.62.76.226.sslip.io
- Features working: boards/lists/cards, move cards, edit title/description, colored tags, members, due dates
- Agents: Hermes (brain, Gemini) for #sprint-main, Forge2Bot (hands, Groq) for #agent-coder
- Autonomous cron posts heartbeat to #agent-log every 10 minutes
- Docs: README, ARCHITECTURE, agent-log, SCORE_100_PLAN.md, skills/status-report/SKILL.md
- Repo on VPS at /home/aman/forge2 with 4 git commits

WHEN ASKED FOR STATUS REPORT, reply ONLY with these three sections using real facts above:
**What I Did** — list 3-5 bullets of completed work
**What's Left** — list 2-4 bullets of remaining tasks
**What Needs Your Call** — list 2-3 decisions only the human must make

Do NOT mention knowledge graphs, dashboards, content moderation, marketing, or any feature not listed above.
Keep each bullet one short line. Be factual, not generic."""

app = App(token=BOT_TOKEN)

def groq_reply(user_text):
    body = json.dumps({
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_text or "status report"},
        ],
        "max_tokens": 400,
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
        data = json.load(resp)
    return data["choices"][0]["message"]["content"]

@app.event("app_mention")
def handle_mention(event, say, logger):
    if event.get("channel") != CHANNEL:
        return
    text = event.get("text", "")
    user_text = text.split(">", 1)[-1].strip() if ">" in text else text
    log("mention: " + user_text[:80])
    try:
        reply = groq_reply(user_text)
        say(text=reply, thread_ts=event.get("ts"))
        log("replied ok")
    except Exception as e:
        log("error: " + str(e))
        say(text="Sorry, error: " + str(e), thread_ts=event.get("ts"))

if __name__ == "__main__":
    log("Forge2Bot responder starting on #agent-coder...")
    SocketModeHandler(app, APP_TOKEN).start()
