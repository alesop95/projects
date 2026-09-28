# telegram-bot

- **Repository**: [alesop95/telegram-bot](https://github.com/alesop95/telegram-bot)
- **Technologies**: Python, API Bot di Telegram
- **Period**: 09/2025 - 06/2026, paused

A Telegram bot built on python-telegram-bot with two persistence backends, SQLite for local runs and PostgreSQL for cloud deployment, chosen through separate entry points (`main.py` and `main_cloud.py`) instead of a runtime switch. It offers formatted custom messages with inline buttons, reusable templates, five selectable chat themes, per-user settings (notifications, language, time zone) and usage statistics for the user and the administrator, aiming to replicate part of Telegram Premium's personalization features without a subscription. It includes a small health-check endpoint, Docker and docker-compose files, deployment configs for Railway and Render and a GitHub Actions workflow.

Scheduled messages are flagged by the bot itself as in development, so the feature set described in the README is only partly active. Handlers, database access and configuration are kept separate.
