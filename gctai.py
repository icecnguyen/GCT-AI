from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "7972397461:AAFT0lE7p1DjEM5aiky6KedWRff-dnXc8f8"

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("GCT Webdrive: https://icecnguyen.ddns.net")

app.add_handler(CommandHandler("start", start))

app.run_polling()