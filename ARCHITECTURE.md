# Architecture

## Agents

- **Hermes (brain)** — plans in `#sprint-main`, uses Gemini 2.5 Flash
- **OpenClaw / Forge2Bot (hands)** — codes in `#agent-coder`, uses Ollama qwen2.5-coder locally (unlimited, no rate limits)

## Slack channels

| Channel | Purpose |
|---------|---------|
| #sprint-main | Human → Hermes planning |
| #agent-coder | Hermes/OpenClaw coding tasks |
| #agent-log | Autonomous cron output |

## Model routing

Hermes uses Gemini free tier for planning. OpenClaw uses local Ollama to avoid Groq/Gemini rate limits during coding.

## App

- `/backend` — Laravel REST API, SQLite
- `/frontend` — React Vite SPA
