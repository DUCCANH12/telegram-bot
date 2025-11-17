import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8223648375:AAFcMzVJXhNGpLqTnRS4D3aRKbPQHZkeNls"
API_URL = "https://script.google.com/macros/s/AKfycbxiC2TGpuduBUHOcyPxnGo61Oicg_eoJjoGnqAPoI73soR-WXhOh6YzatcCMwFkfzlg/exec"

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Dùng: /add nội_dung")
        return
    value = " ".join(context.args)
    r = requests.get(API_URL, params={"action": "add", "value": value})
    await update.message.reply_text(r.text)

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Dùng: /get số_dòng")
        return
    row = context.args[0]
    r = requests.get(API_URL, params={"action": "get", "row": row})
    await update.message.reply_text(r.text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("get", get))

    app.run_polling()

if __name__ == "__main__":
    main()
