# Submit Guide — Do These 4 Screenshots + Video

> **Repo:** https://github.com/Aman-Kumar342/forge2-kanban  
> **Live URL:** https://forge2.69.62.76.226.sslip.io  
> **Deadline:** 6 PM IST, 21 June 2026

Everything below is copy-paste. Take a **screenshot** after each step.  
Save screenshots in folder: `slack-export/screenshots/`

---

## Screenshot 1 — Status report (#agent-coder)

**Channel:** `#agent-coder`

**You type:**
```
@Forge2Bot status report
```

**Wait 10 seconds.**

**Screenshot must show:**
- Your message
- Bot reply with three sections: **What I Did** / **What's Left** / **What Needs Your Call**

Save as: `slack-export/screenshots/01-status-report.png`

---

## Screenshot 2 — Autonomous heartbeat (#agent-log)

**Channel:** `#agent-log`

**You do:** Just open the channel (no typing needed).

**Screenshot must show:**
- A message from Forge2Bot like: `Forge2 autonomous heartbeat` with the Kanban live URL

Save as: `slack-export/screenshots/02-agent-log-heartbeat.png`

---

## Screenshot 3 — Chat loop (#sprint-main → plan)

**Channel:** `#sprint-main`

**You type:**
```
@Forge2Bot Plan a tiny Kanban app: Laravel API + React UI. List the steps before coding.
```

**Wait 15 seconds.**

**Screenshot must show:**
- Your message
- Bot reply with a plan (numbered steps)

Save as: `slack-export/screenshots/03-sprint-main-plan.png`

---

## Screenshot 4 — Memory test (2 messages, same screenshot or 2 files)

**Channel:** `#sprint-main`

**Message 1 — you type:**
```
@Forge2Bot Remember: my demo board is called "Forge2 Kanban" and my deadline is 6 PM IST.
```

Wait for bot reply. Then **Message 2 — you type:**
```
@Forge2Bot What demo board name did I tell you?
```

**Screenshot must show:**
- Both your messages AND bot saying **Forge2 Kanban** (or similar)

Save as: `slack-export/screenshots/04-memory-test.png`

---

## What is "memory test"?

Simple: tell the bot a fact → ask it later → it should remember **without you pasting the fact again**.  
That's what Screenshot 4 proves.

---

## What is "full chat loop"?

The judges want to see this flow (your screenshots 1 + 3 cover it):

```
YOU (#sprint-main)     →  ask for a plan
BOT (#sprint-main)     →  posts plan
YOU (#agent-coder)     →  ask for status report
BOT (#agent-coder)     →  What I Did / What's Left / What Needs Your Call
```

You already tested the Kanban on the website. Slack screenshots prove the **agent team** works.

---

## Demo video (you record — 60–90 seconds)

1. Open live URL → create card → move it → add tag/member
2. Show Slack `#agent-coder` status report
3. Show Slack `#agent-log` heartbeat

Upload to YouTube or Loom. Add link to README under **Demo Video**.

---

## After screenshots — push to GitHub

```bash
ssh aman@69.62.76.226
cd /home/aman/forge2
mkdir -p slack-export/screenshots
# (copy your PNG files into slack-export/screenshots/ on VPS, or upload via scp)

export GIT_AUTHOR_NAME="Aman-Kumar342"
export GIT_AUTHOR_EMAIL="amantop102525@gmail.com"
export GIT_COMMITTER_NAME="Aman-Kumar342"
export GIT_COMMITTER_EMAIL="amantop102525@gmail.com"

git add slack-export/screenshots/ SUBMIT_GUIDE.md README.md
git commit -m "Add Slack screenshot evidence and submit guide."
git push origin main
```

---

## Submit form

Provide:
- **GitHub:** https://github.com/Aman-Kumar342/forge2-kanban
- **Live URL:** https://forge2.69.62.76.226.sslip.io
- **Video link:** (your YouTube/Loom URL)
- **Models used:** Groq llama-3.1-8b-instant, Gemini 2.5 Flash, Ollama qwen2.5-coder

Done. ✅
