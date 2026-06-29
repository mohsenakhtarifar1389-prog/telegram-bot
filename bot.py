import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 توکن از Render میاد
TOKEN = os.environ.get("8952875701:AAFHuL7qXIW3pAApIq_zTTm9xmf8mnvKO9Y")

# 👤 آیدی ادمین (اینو عوض کن)
ADMIN_ID = 8815017184

user_state = {}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [["❓ سوال دارم"]]

    await update.message.reply_text(
        "سلام 👋\nبه ربات پشتیبانی خوش اومدی",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# مدیریت پیام‌ها
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    text = update.message.text

    if text == "❓ سوال دارم":
        user_state[user_id] = True
        await update.message.reply_text("سوالتو بنویس 👇")
        return

    if user_state.get(user_id):

        user = update.message.from_user

        msg = f"""
📩 سوال جدید

👤 نام: @{user.username}
🆔 ID: {user.id}

❓ سوال:
{text}
"""

        await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

        await update.message.reply_text("ارسال شد ✅")

        user_state[user_id] = False


# اجرای ربات
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
