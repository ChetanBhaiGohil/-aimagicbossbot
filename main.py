from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, MAX_FREE_TRIES
from ai_services import generate_image
import json
import os

# ફ્રી યૂઝર ડેટા સ્ટોર કરવા
USER_DATA_FILE = "users.json"

# યુઝર ડેટા લોડ કરવું
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# યુઝર ડેટા સાચવવું
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f)

user_data = load_user_data()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to AI Image Bot!\nSend me any prompt (like 'cat in space'), and I’ll send you an AI-generated image.\n\n🆓 First 10 prompts are FREE!\n💰 Upgrade plans coming soon!")

async def handle_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    prompt = update.message.text

    if user_id not in user_data:
        user_data[user_id] = {"count": 0}

    if user_data[user_id]["count"] >= MAX_FREE_TRIES:
        await update.message.reply_text("❌ Free limit reached (10 prompts).\n💳 Upgrade plans will be available soon!")
        return

    await update.message.reply_text("🧠 Generating image...")

    image_url = generate_image(prompt)
    if image_url:
        await update.message.reply_photo(photo=image_url, caption="✅ Done!")
        user_data[user_id]["count"] += 1
        save_user_data(user_data)
    else:
        await update.message.reply_text("⚠️ Something went wrong. Try again later.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_prompt))

    print("🤖 Bot started...")
    app.run_polling()