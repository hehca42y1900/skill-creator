# Маркетолог-ассистент — Telegram-бот

Telegram-бот на [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot),
использующий Claude API (`claude-sonnet-5`) с system prompt маркетолог-ассистента
(анализ конкурентов, ЦА, УТП, каналы продвижения — см. `.claude/skills/marketer-assistant/`
в корне репозитория).

## Установка

```bash
cd marketer-telegram-bot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Настройка

1. Получите токен бота у [@BotFather](https://t.me/BotFather) в Telegram
   (команда `/newbot`).
2. Получите `ANTHROPIC_API_KEY` в [console.anthropic.com](https://console.anthropic.com).
3. Скопируйте `.env.example` в `.env` и впишите оба значения:

```bash
cp .env.example .env
```

```
TELEGRAM_BOT_TOKEN=...
ANTHROPIC_API_KEY=...
```

## Запуск

```bash
python bot.py
```

Бот работает через long polling — держите процесс запущенным (локально,
на сервере или в screen/tmux/systemd-сервисе).

## Как пользоваться

- `/start` — приветствие и очистка истории диалога.
- `/reset` — очистить историю текущего диалога, не начиная бота заново.
- Обычное сообщение — бот отвечает как маркетолог-ассистент: даёт краткий
  экспресс-отчёт и предлагает углубиться в детали или план внедрения.

## Особенности реализации

- **История диалога хранится в памяти процесса** (по `chat_id`), обрезается
  до последних 30 сообщений. При перезапуске бота история теряется. Для
  постоянного хранения (например, в Postgres/SQLite) — вынесите
  `chat_histories` в отдельный модуль с персистентным хранилищем.
- **Веб-поиск конкурентов** подключён через встроенный серверный инструмент
  Claude `web_search` — Claude сам решает, когда искать.
- **Длинные ответы** режутся на части по границам абзацев, чтобы уложиться в
  лимит Telegram на длину сообщения (4096 символов).
- Ответ идёт одним сообщением после обработки (без стриминга по токенам) —
  для Telegram это ощутимо надёжнее, чем стриминг через `edit_message_text`
  на каждый токен (упирается в rate limit Telegram API).

## Что можно добавить дальше

- Постоянное хранилище истории диалогов (Postgres/SQLite/Redis) вместо
  словаря в памяти.
- Промпт-кэширование (`cache_control`) на system prompt — снижает стоимость
  повторных обращений одного пользователя.
- Деплой как systemd-сервис / Docker-контейнер / на webhook вместо polling
  для продакшена с высокой нагрузкой.
