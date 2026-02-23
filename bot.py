import os
import telebot

# جلب المتغيرات من Render Environment
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

# مجموعة لتخزين المستخدمين المشتركين
subscribed_users = set()

# رسالة الترحيب عند /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك 👋\nللاشتراك اكتب: اشتراك")

# التعامل مع الاشتراك
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id

    if message.text.strip() == "اشتراك":
        if user_id not in subscribed_users:
            subscribed_users.add(user_id)
            bot.send_message(user_id, "تم استلام طلبك ✅\nأرسل الآن 30 فيديو.\nلا تنسَ كتابة اسم حسابك.")
            
            # إرسال إشعار للـ ADMIN مع حماية من الرسائل لنفسه
            if user_id != ADMIN_ID:
                try:
                    bot.send_message(ADMIN_ID, f"طلب جديد من @{message.from_user.username}")
                except Exception as e:
                    print(f"تعذر إرسال الإشعار للـ ADMIN: {e}")
        else:
            bot.send_message(user_id, "أنت مشترك بالفعل ✅\nأرسل الآن الفيديوهات.")
    else:
        bot.send_message(user_id, "اكتب كلمة اشتراك للبدء.")

# تشغيل البوت
bot.polling()
