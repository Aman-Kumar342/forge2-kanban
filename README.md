# Forge2 Qualifier — Kanban Board

Tiny Trello-style Kanban built for Forge2 Edition 1 qualifier.

## Live URL

https://forge2.69.62.76.226.sslip.io

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
