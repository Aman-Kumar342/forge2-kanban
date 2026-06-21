# Architecture

## System overview

```
Human (Slack)
    │
    ├── #sprint-main ──► Hermes (brain) ── Gemini 2.5 Flash
    │                         │
    │                         └── plans & delegates
    │
    ├── #agent-coder ──► OpenClaw / Forge2Bot (hands) ── Ollama qwen2.5-coder:7b
    │                         │
    │                         └── writes code in /home/aman/forge2
    │
    └── #agent-log ◄── Hermes cron + shell heartbeat (every 10m)
```

## Agents

| Agent | Role | Model | Channel |
|-------|------|-------|---------|
| Hermes | Brain — planning, memory, delegation | `google/gemini-2.5-flash` | #sprint-main |
| OpenClaw (Forge2Bot) | Hands — file edits, coding | `ollama/qwen2.5-coder:7b` | #agent-coder |

**Why Ollama for coding?** Groq free tier limits context to ~12k tokens; OpenClaw sessions exceeded 38k. Ollama runs locally on the VPS with no rate limits.

## Slack channels

| Channel | ID | Purpose |
|---------|-----|---------|
| #sprint-main | C0BC3GR325P | Human ↔ Hermes planning |
| #agent-coder | C0BBL75J5AB | Coding tasks ↔ Forge2Bot |
| #agent-log | C0BBVAUNJSF | Autonomous cron output |

## Memory & skills

- **Memory:** `~/.hermes/memories/MEMORY.md` — cross-session project facts
- **Skill:** `skills/status-report/SKILL.md` — three-section status format:
  - **What I Did** / **What's Left** / **What Needs Your Call**

## Autonomous cron

1. **Hermes cron:** `forge2-progress` — every 10m, delivers to `#agent-log`
2. **Shell fallback:** `scripts/agent-log-heartbeat.sh` — crontab every 10m

## Kanban app

| Layer | Tech | Path |
|-------|------|------|
| API | Laravel 13, SQLite | `backend/` |
| UI | React 19, Vite | `frontend/` |
| Proxy | Caddy TLS | forge2.69.62.76.226.sslip.io |

### API endpoints

- `GET/POST /api/boards`
- `POST /api/lists/{id}/cards`
- `PATCH /api/cards/{id}`
- `POST /api/cards/{id}/move`
- `POST /api/boards/{id}/members`
- `POST /api/boards/{id}/tags`
- `POST /api/cards/{id}/tags/{tagId}`

## Deployment (VPS)

```bash
# API
cd backend && php artisan serve --host=127.0.0.1 --port=8000

# Frontend (production build)
cd frontend && npx serve -s dist -l 5174
```

Caddy reverse-proxies HTTPS → ports 8000 (API) and 5174 (UI).
