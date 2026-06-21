# Slack Export — Forge2 Qualifier Evidence

Round-trip Slack API tests and agent logs for hackathon submission.

| File | Description |
|------|-------------|
| `01-auth-test.json` | `auth.test` — verifies bot token |
| `02-post-sprint-main.json` | Post message to #sprint-main |
| `03-post-agent-log.json` | Post message to #agent-log |
| `04-read-sprint-main.json` | Read recent #sprint-main history |
| `05-kanban-api-proof.json` | API proof: board, card, move |
| `06-openclaw-log-excerpt.txt` | OpenClaw gateway log excerpts |
| `cron-heartbeat.log` | Autonomous cron post log |

## Screenshots (add before submit)

Create `slack-export/screenshots/` with:
1. Hermes plan in #sprint-main
2. Forge2Bot code reply in #agent-coder
3. Status report (What I Did / What's Left / What Needs Your Call)
4. Memory test across 2 sessions
5. #agent-log autonomous heartbeat
