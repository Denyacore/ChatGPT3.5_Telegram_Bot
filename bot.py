import os
import signal
import time
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()

# Здесь введите свой API-ключ
bot_token = os.getenv('BOT_TOKEN')
# Здесь введите свой API-ключ OpenAI
api_key = os.getenv('OPENAI_API_KEY')

# Создаем объект бота
bot = telegram.Bot(token=bot_token)

# Создаем объект updater и передаем ему токен бота
updater = Updater(token=bot_token, use_context=True)

# Инициализируем API OpenAI с помощью ключа API
openai.api_key = api_key

# Создаем функцию-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm ChatGPT! How can I help you?")

# Создаем функцию-обработчик команды /clear
def clear(update, context):
    # Очищаем историю сообщений
    context.chat_data.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Start new dialogue.")

# Создаем функцию-обработчик текстовых сообщений
def echo(update, context):
    # Получаем текст сообщения пользователя
    user_message = update.message.text

    # Получаем историю сообщений из контекста
    messages = context.chat_data.get('messages', [])
    
    # Добавляем сообщение пользователя в историю
    messages.append({"role": "user", "content": user_message})
    
    # Сохраняем историю сообщений в контекст
    context.chat_data['messages'] = messages

    # Получаем ответ от ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        max_tokens=3072,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

    # Получаем текст ответа от ChatGPT
    chatgpt_response = completion.choices[0]['message']

    # Добавляем ответ ChatGPT в историю
    messages.append({"role": "system", "content": chatgpt_response['content']})

    # Сохраняем историю сообщений в контекст
    context.chat_data['messages'] = messages
    
    # Отправляем ответ от ChatGPT пользователю
    context.bot.send_message(chat_id=update.effective_chat.id, text=chatgpt_response['content'])

# Регистрируем обработчики команд и текстовых сообщений
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('clear', clear))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота Telegram
updater.start_polling()

# Добавляем обработчик сигнала SIGINT для возможности остановки бота сочетанием Ctrl+C
def stop_handler(signum, frame):
    print("Stopping bot...")
    updater.stop()
    print("Bot stopped.")
    exit(0)

signal.signal(signal.SIGINT, stop_handler)
print("Bot started. Press Ctrl+C to stop.")

# Ожидаем сигнал SIGINT в бесконечном цикле
while True:
    time.sleep(1)  # Задержка в 1 секунду