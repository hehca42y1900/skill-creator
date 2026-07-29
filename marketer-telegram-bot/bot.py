import asyncio
import logging
import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

MODEL = "claude-sonnet-5"
MAX_TOKENS = 8000
TELEGRAM_MESSAGE_LIMIT = 4096
MAX_HISTORY_MESSAGES = 30  # обрезаем историю, чтобы не разгонять стоимость до бесконечности

SYSTEM_PROMPT = (Path(__file__).parent / "system.txt").read_text(encoding="utf-8")
WELCOME_MESSAGE = (
    "Здравствуйте! Я маркетолог-ассистент. Могу помочь с анализом конкурентов, "
    "исследованием целевой аудитории, разработкой стратегии продвижения, поиском "
    "новых точек роста и практическим планом продвижения.\n\n"
    "Опишите ваш бизнес и что вас интересует — комплексный анализ или конкретный вопрос. "
    "Команда /reset очищает историю диалога."
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("marketer_bot")

anthropic_client = anthropic.Anthropic()  # берёт ANTHROPIC_API_KEY / ant auth login

# История переписки по каждому чату: chat_id -> список сообщений в формате Anthropic API.
# Хранится в памяти процесса — при перезапуске бота обнуляется.
chat_histories: dict[int, list[dict]] = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_histories.pop(update.effective_chat.id, None)
    await update.message.reply_text(WELCOME_MESSAGE)


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_histories.pop(update.effective_chat.id, None)
    await update.message.reply_text("История диалога очищена.")


def call_claude(messages: list[dict]) -> anthropic.types.Message:
    """Синхронный вызов Claude API — выполняется в отдельном потоке, чтобы не блокировать event loop."""
    return anthropic_client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=[{"type": "web_search_20260209", "name": "web_search"}],
        messages=messages,
    )


def split_for_telegram(text: str) -> list[str]:
    """Режет длинный ответ на части не длиннее лимита Telegram, стараясь резать по абзацам."""
    if len(text) <= TELEGRAM_MESSAGE_LIMIT:
        return [text]

    chunks: list[str] = []
    remaining = text
    while len(remaining) > TELEGRAM_MESSAGE_LIMIT:
        split_at = remaining.rfind("\n\n", 0, TELEGRAM_MESSAGE_LIMIT)
        if split_at <= 0:
            split_at = TELEGRAM_MESSAGE_LIMIT
        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()
    if remaining:
        chunks.append(remaining)
    return chunks


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user_text = update.message.text

    history = chat_histories.setdefault(chat_id, [])
    history.append({"role": "user", "content": user_text})
    del history[:-MAX_HISTORY_MESSAGES]  # оставляем только последние N сообщений
    if history and history[0]["role"] != "user":
        # Claude API требует, чтобы первое сообщение было от user
        del history[0]

    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

    try:
        response = await asyncio.to_thread(call_claude, history)
    except anthropic.APIStatusError as e:
        logger.exception("Anthropic API error")
        await update.message.reply_text(f"Ошибка при обращении к Claude API: {e.message}")
        return
    except anthropic.APIConnectionError:
        logger.exception("Anthropic connection error")
        await update.message.reply_text("Не удалось связаться с Claude API. Попробуйте ещё раз.")
        return

    history.append({"role": "assistant", "content": response.content})

    reply_text = "".join(block.text for block in response.content if block.type == "text")
    if not reply_text:
        reply_text = "Не удалось получить текстовый ответ. Попробуйте переформулировать запрос."

    for chunk in split_for_telegram(reply_text):
        await update.message.reply_text(chunk)


def main() -> None:
    telegram_token = os.environ["TELEGRAM_BOT_TOKEN"]

    application = Application.builder().token(telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Marketer bot starting (model=%s)", MODEL)
    application.run_polling()


if __name__ == "__main__":
    main()
