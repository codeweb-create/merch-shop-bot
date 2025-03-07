import os
import logging
import openai
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from system_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройка логирования
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [["ℹ️ Доставка и оплата", "❓ Задать вопрос ассистенту"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    user_name = update.message.from_user.first_name or "Дорогой клиент"
    await update.message.reply_text(
        f"{user_name}, 👋 Привет! Я ваш консультант!\nВыбери товар из каталога или задай вопрос.",
        reply_markup=reply_markup
    )

# Функция обработки кнопки "Доставка и оплата"
async def delivery_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🚚 Доставка\n"
        "- Курьером (2-3 дня, 300 ₽)\n"
        "- Самовывоз (г. Москва, ул. Примерная, 1)\n"
        "- Доставка в регионы – рассчитывается индивидуально.\n\n"
        "💳 Оплата\n"
        "- Картой онлайн\n"
        "- Наличными курьеру\n"
        "- Оплата при самовывозе."
    )

# Функция обработки сообщений (ИИ-ассистент)
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return

    user_message = update.message.text or update.message.caption
    user_id = update.message.from_user.id
    
    if not user_message:
        return
    
    # Логируем JSON структуры входящего сообщения для отладки
    logging.info(f"📩 Получено сообщение от {user_id}: {update.message.to_dict()}")
    
    # Обработка запроса к OpenAI
    try:
        logging.info(f"⏳ Запрос в OpenAI от {user_id}: {user_message}")
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        
        if "chat_history" not in context.user_data:
            context.user_data["chat_history"] = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        context.user_data["chat_history"].append({"role": "user", "content": user_message})
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=context.user_data["chat_history"],
            temperature=0.7
        )
        
        reply_text = response.choices[0].message.content.strip() if response.choices else "⚠️ Ошибка OpenAI"
        logging.info(f"✅ Ответ OpenAI для {user_id}: {reply_text}")
        await update.message.reply_text(reply_text)
    except Exception as e:
        logging.error(f"❌ Ошибка OpenAI: {e}")
        await update.message.reply_text("⚠️ Ошибка при обработке запроса, попробуйте позже.")

# Функция запуска бота
def main():
    print("✅ Запуск бота...")  
    try:
        application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.Regex("ℹ️ Доставка и оплата"), delivery_info))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
        application.run_polling()
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    main()
