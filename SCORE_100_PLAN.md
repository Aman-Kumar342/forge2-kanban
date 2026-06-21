# Forge2 Qualifier — 100/100 Score Plan

> **Deadline:** 6:00 PM IST, Saturday 21 June 2026  
> **Live URL:** https://forge2.69.62.76.226.sslip.io  
> **VPS:** aman@69.62.76.226  
> **Repo:** /home/aman/forge2

Master checklist to score **100/100** on Forge2 Edition 1 qualifier.

---

## Scoring rubric (100 pts)

| Category | Pts | Requirement | Status |
|----------|-----|-------------|--------|
| Agent setup | 18 | OpenClaw + Hermes on free models | DONE |
| Chat loop | 22 | Human → plan → code → status in Slack | NEEDS live thread + screenshots |
| Kanban app | 25 | Laravel API + React, 5 features, live URL | DONE |
| Memory + skill + cron | 12 | Memory, SKILL.md, autonomous #agent-log | DONE |
| Human-in-the-loop | 10 | All activity visible in Slack | NEEDS screenshots |
| Free stack | 5 | Ollama / Groq / Gemini only | DONE |
| Repo & docs | 8 | README, ARCHITECTURE, logs, commits, public repo | NEEDS GitHub push + video |

**Estimated score now: ~85-90/100** (before GitHub, video, Slack screenshots)

---

## DONE (verified)

### Agent setup (18/18)
- OpenClaw gateway active, model: ollama/qwen2.5-coder:7b
- Hermes gateway active, model: google/gemini-2.5-flash
- Slack: #sprint-main, #agent-coder, #agent-log
- Redacted configs: openclaw.json, hermes.config.yaml

### Kanban app (25/25)
- Laravel 13 + SQLite API at /api/*
- React + Vite SPA, live HTTPS URL
- All 5 features: boards/lists/cards, move, edit, tags, members+due dates
- Proof: slack-export/05-kanban-api-proof.json

### Memory + skill + cron (12/12)
- Hermes memory: ~/.hermes/memories/MEMORY.md
- Skill: skills/status-report/SKILL.md
- Hermes cron: forge2-progress every 10m → #agent-log
- Shell cron: scripts/agent-log-heartbeat.sh every 10m
- Slack round-trip: slack-export/*.json

### Free stack (5/5)
- Ollama local for OpenClaw (unlimited)
- Gemini free for Hermes planning
- Groq available as backup

### Repo docs (5/8)
- README.md, ARCHITECTURE.md, agent-log.md
- .env.example (no secrets)
- Incremental commits (see git log)

---

## YOU MUST DO (blocks 100/100)

### 1. Public GitHub repo (DQ if private at deadline)

```bash
ssh aman@69.62.76.226
cd /home/aman/forge2
git remote add origin https://github.com/YOUR_USERNAME/forge2-kanban.git
git push -u origin main
```

### 2. Demo video (60-90 sec)

Record:
1. Live Kanban URL — create board, card, move, tag, member, due date
2. Slack #sprint-main Hermes plan
3. Slack #agent-coder Forge2Bot reply
4. Slack #agent-log heartbeat

Upload to YouTube/Loom. Add link to README under Demo Video.

### 3. Live chat-loop in Slack

**#sprint-main:**
```
@Forge2Bot Plan: Add dark mode toggle to Kanban frontend. Break into steps for coder.
```

**#agent-coder:**
```
@Forge2Bot Implement step 1: add dark mode CSS variable and toggle in App.tsx
```

**#agent-coder (status):**
```
@Forge2Bot status report
```
Expect: **What I Did / What's Left / What Needs Your Call**

**Memory test (2 sessions in #sprint-main):**
Session 1: `@Forge2Bot Remember: my demo board is "Forge2 Kanban", deadline 6 PM IST.`
Session 2: `@Forge2Bot What demo board name did I tell you?`

Screenshot all → save to slack-export/screenshots/

### 4. Submit form before 6 PM IST

- Public GitHub URL
- Live URL: https://forge2.69.62.76.226.sslip.io
- Demo video link

---

## 60-minute timeline

| Min | Task | Who |
|-----|------|-----|
| 0-5 | Verify live URL | Auto DONE |
| 5-10 | Create public GitHub repo + push | YOU |
| 10-25 | Slack chat-loop + screenshots | YOU |
| 25-35 | Record demo video | YOU |
| 35-40 | Add video link to README, push | YOU |
| 40-45 | Memory test in Slack | YOU |
| 45-50 | Verify #agent-log heartbeat | Auto DONE |
| 50-60 | Submit form | YOU |

---

## Verification commands

```bash
systemctl --user is-active openclaw-gateway hermes-gateway
ollama list
curl -s https://forge2.69.62.76.226.sslip.io/api/boards | head -c 200
crontab -l | grep heartbeat
export PATH=$HOME/.local/bin:$PATH && hermes cron list
git log --oneline
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Forge2Bot silent | Wait 30s for Ollama; journalctl --user -u openclaw-gateway -f |
| Hermes 429 | Wait 1 min; use #agent-coder for coding |
| Live URL down | php artisan serve + npx serve -s dist |
