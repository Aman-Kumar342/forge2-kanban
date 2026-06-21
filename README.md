# Forge2 Qualifier — Kanban Board

Tiny Trello-style Kanban built for Forge2 Edition 1 qualifier.

## Live URL

https://forge2.69.62.76.226.sslip.io

## Demo Video

> **TODO:** Add your 60–90 second screen recording link here after upload.
> See `SCORE_100_PLAN.md` for what to record.

## Score Plan

See **[SCORE_100_PLAN.md](./SCORE_100_PLAN.md)** for the full 100/100 checklist.

## Stack

| Component | Tool | Model |
|-----------|------|-------|
| Brain | Hermes | Gemini 2.5 Flash (free) |
| Hands | OpenClaw (Forge2Bot) | Ollama qwen2.5-coder:7b (local, free) |
| Comms | Slack | #sprint-main, #agent-coder, #agent-log |
| Backend | Laravel 13 + SQLite | — |
| Frontend | React + Vite | — |

## Run locally

### API
```bash
cd backend
cp .env.example .env
touch database/database.sqlite
composer install
php artisan migrate
php artisan serve --port=8000
```

### Frontend
```bash
cd frontend
npm install
echo 'VITE_API_URL=http://127.0.0.1:8000/api' > .env
npm run dev
```

## Features

- Boards → Lists → Cards
- Move cards between lists
- Edit card title + description
- Colored tags on cards
- Assign members
- Due dates with overdue highlighting

## Agent workflow

1. Human posts goal in **#sprint-main** → Hermes plans
2. Coding tasks go to **#agent-coder** → Forge2Bot (OpenClaw) implements
3. **#agent-log** receives autonomous heartbeat every 10 minutes
4. Status updates use `skills/status-report/SKILL.md` format

## Repo structure

| Path | Purpose |
|------|---------|
| `backend/` | Laravel REST API |
| `frontend/` | React Vite SPA |
| `skills/status-report/` | Agent skill for status reports |
| `slack-export/` | Slack API round-trip evidence |
| `scripts/` | Autonomous cron heartbeat |
| `openclaw.json` | Redacted OpenClaw config |
| `hermes.config.yaml` | Redacted Hermes config |
| `agent-log.md` | Slack conversation excerpts |
| `ARCHITECTURE.md` | System design |
