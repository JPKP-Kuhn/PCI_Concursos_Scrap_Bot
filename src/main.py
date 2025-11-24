from pyrogram.client import Client

from settings import *
from handlers import messages

def build_bot() -> Client:
    bot_app = Client(
        name=BOT_NAME,
        api_id=TELEGRAM_API_ID,
        api_hash=TELEGRAM_API_HASH,
        bot_token=TELEGRAM_BOT_TOKEN
    )
    messages.MessageHandler(bot_app)
    print("Bot iniciado")
    return bot_app


def main():
    bot = build_bot()
    bot.run()


if __name__ == "__main__":
    main()
