#!/usr/bin/env bash
# Autonomous heartbeat for Forge2 qualifier — posts to #agent-log
set -euo pipefail
BOT=$(grep '^SLACK_BOT_TOKEN=' "$HOME/.hermes/.env" | cut -d= -f2-)
TS=$(date -u +"%Y-%m-%d %H:%M UTC")
MSG="🤖 Forge2 autonomous heartbeat ($TS) — Kanban live: https://forge2.69.62.76.226.sslip.io | Board API OK | Cron active"
curl -s -X POST https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer $BOT" \
  -H "Content-Type: application/json" \
  -d "{\"channel\":\"C0BBVAUNJSF\",\"text\":\"$MSG\"}" \
  >> /home/aman/forge2/slack-export/cron-heartbeat.log 2>&1
