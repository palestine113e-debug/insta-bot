import telebot
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك 👋\n\nهذه خدمة جدولة محتوى إنستغرام.\n\nللاشتراك اكتب: اشتراك")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "اشت
