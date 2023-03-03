# ChatGPT3.5 Telegram Bot by [Denyacore](https://github.com/Denyacore)

A bot for communicating with [ChatGPT](chat.openai.com). 

The [gpt-3.5-turbo model](https://platform.openai.com/docs/guides/chat) is taken as a basis.

## Tech Stack

**Client:** Python 3.7
- openai 0.27.0
- telegram 0.0.1
- pipreqs 0.4.11
- python-dotenv 0.21.1
- python-telegram-bot 13.5

## Deployment

To deploy this project run

Clone the repository and go to it on the command line:

```
https://github.com/Denyacore/ChatGPT3.5_Telegram_Bot.git
```

```
cd ChatGPT3.5_Telegram_Bot
```

Create a file .env

Fill it with content:
```
BOT_TOKEN = 'YOUR TG BOT TOKEN'
OPENAI_API_KEY = 'YOUR OPENAI API KEY'
```
Your TG TOKEN https://t.me/BotFather (@BotFather)

Your OpenAI key https://platform.openai.com/account/api-keys

Create and activate a virtual environment:

```
python3 -3.7 -m venv env
        or
py -3.7 -m venv venv
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
                or
py -m pip install --upgrade pip
```

Install dependencies from a file *requirements.txt* :

```
pip install -r requirements.txt
```

Launch Bot
```
py bot.py
```

Write something to your bot in telegram