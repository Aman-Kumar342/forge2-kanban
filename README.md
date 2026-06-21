# Forge2 Kanban

My submission for the Forge2 Edition 1 qualifier — a small Kanban board (Laravel API + React UI) built with Hermes and OpenClaw on a VPS, wired into Slack.

**Live app:** https://forge2.69.62.76.226.sslip.io  
**Demo video + screenshots:** https://drive.google.com/drive/u/0/folders/1UXNNoOWAJl0leaYEx4-kgDwpX2TRRjwT

Open the Drive folder for the screen recording and Slack screenshots (`agentCoder`, `agentLOg`, `SprintMainChat`, `sprint-mainChatMemory`, `forge2Kanban`).

---

## What's in here

The Kanban app is the main deliverable — boards, lists, cards, move between columns, tags, members, due dates (overdue cards get a red border). Nothing fancy, just the five features the handbook asked for.

The agent side runs on the same VPS:

- **#sprint-main** — Hermes plans stuff, remembers facts across messages
- **#agent-coder** — Forge2Bot posts status reports (What I Did / What's Left / What Needs Your Call)
- **#agent-log** — cron heartbeat every 10 minutes, no human prompt needed

I used free models only: Gemini 2.5 Flash for Hermes, Ollama `qwen2.5-coder:7b` for OpenClaw, and Groq `llama-3.1-8b-instant` for the Slack bot when I needed faster replies.

---

## Run it locally

**Backend**

```bash
cd backend
cp .env.example .env
touch database/database.sqlite
composer install
php artisan migrate
php artisan serve --port=8000
```

**Frontend**

```bash
cd frontend
npm install
echo 'VITE_API_URL=http://127.0.0.1:8000/api' > .env
npm run dev
```

Production on the VPS uses Caddy in front of `php artisan serve` and a static build of the React app. You don't need any of that to judge the live URL — it should just work in the browser.

---

## Repo layout

- `backend/` — Laravel REST API (SQLite)
- `frontend/` — React + Vite SPA
- `scripts/` — Slack responder + cron heartbeat for `#agent-log`
- `skills/status-report/` — skill file for the status report format
- `slack-export/` — API test evidence
- `ARCHITECTURE.md` — how brain vs hands routing works
- `agent-log.md` — notes from the Slack build sessions

Configs with secrets are redacted (`openclaw.json`, `hermes.config.yaml`).

---

## What I skipped

No login, no drag-and-drop, no dark mode. Kept scope small so the board and the Slack loop both actually work end-to-end.

---

Built by Aman Kumar for Forge2 Edition 1, June 2026.
