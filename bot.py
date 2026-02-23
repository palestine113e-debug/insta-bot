import os
import telebot

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك 👋\nللاشتراك اكتب: اشتراك")

@bot.message_handler(func=lambda message: message.text == "اشتراك")
def subscribe(message):
    bot.reply_to(message, "تم استلام طلبك ✅")
    bot.send_message(ADMIN_ID, f"طلب جديد من @{message.from_user.username}")

bot.polling()
