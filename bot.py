import os
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ["BOT_TOKEN"]
URL = os.environ.get("WEB_APP_URL", "https://anvargpt-tech.github.io/uchrashuv-app/uchrashuv_app%20(1).html")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btn = [[InlineKeyboardButton("💌 Uchrashuv taklifini ochish", web_app=WebAppInfo(url=URL))]]
    await update.message.reply_text(
        "💕 Salom! Senga maxsus taklif bor...\n\nQuyidagi tugmani bos! 👇",
        reply_markup=InlineKeyboardMarkup(btn)
    )

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
