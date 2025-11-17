from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

API_URL = "YOUR_GOOGLE_SCRIPT_URL"  # THAY LINK WEB APP

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Nhập: /add nội_dung")
        return

    r = requests.get(API_URL, params={"action": "add", "value": text})
    await update.message.reply_text(r.text)

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Nhập: /get số_dòng")
        return

    row = context.args[0]
    r = requests.get(API_URL, params={"action": "get", "row": row})
    await update.message.reply_text(f"Dòng {row} cột D: {r.text}")

def main():
    app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN").build()
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("get", get))
    app.run_polling()

if __name__ == "__main__":
    main()
