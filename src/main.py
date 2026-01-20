from pyrogram.client import Client

from settings import *
from handlers import messages_handler

# Start the telegram bot
def build_bot() -> Client:
    bot_app = Client(
        name=BOT_NAME,               # type: ignore
        api_id=TELEGRAM_API_ID,      # type: ignore
        api_hash=TELEGRAM_API_HASH,  # type: ignore
        bot_token=TELEGRAM_BOT_TOKEN # type: ignore
    )
    messages_handler.MessageHandler(bot_app)
    print("Bot iniciado") # Message to know if the bot was started
    return bot_app


def main():
    bot = build_bot()
    bot.run()


if __name__ == "__main__":
    main()
