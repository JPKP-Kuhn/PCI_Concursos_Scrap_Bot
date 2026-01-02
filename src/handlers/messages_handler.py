from pyrogram.client import Client
from pyrogram import filters
# For basic messages
from .messages_text import MessagesText
from .crew_integration import CrewaiIntegration

__all__ = ["MessageHandler"]


class MessageHandler(MessagesText):
    def __init__(self, client: Client):
        self.app = client
        self.setup_handlers()


    async def _send_long_message(self, message, content, chunk_size: int = 4096) -> None:
        """
        Send a message to Telegram respecting the 4096 character limit.
        If the content is longer, it will be split into multiple messages.
        """
        # Garante que o conteúdo é string, independente do tipo retornado pelos agentes
        text = str(content) if content is not None else ""

        # Se a mensagem couber em um único envio, já retorna
        if len(text) <= chunk_size:
            await message.reply(text)
            return

        # Caso contrário, envia em partes
        for start in range(0, len(text), chunk_size):
            await message.reply(text[start:start + chunk_size])


    def setup_handlers(self) -> None:
        # Command handlers
        self.app.on_message(filters.command('start'))(self.handle_start)
        self.app.on_message(filters.command('help'))(self.handle_help)

        # Text handler, only text
        self.app.on_message(filters.text & ~filters.command(["start", "help"]))(self.handle_text)

        # Unsupported message types (photos, audio, stickers, etc.)
        self.app.on_message(
            (filters.photo | filters.video | filters.audio | filters.voice | filters.sticker | filters.animation | filters.document)
            )(self.handle_unsupported)



    # Command handlers
    async def handle_start(self, client: Client, message):
        """Handle the start command."""
        username = message.chat.username if message.chat else None
        greeting = self.get_greeting(username)
        print(f"Start called by {message.chat.username}")
        await message.reply(greeting)
        await message.reply(self.START_RESPONSE.format("start"))

    async def handle_help(self, client: Client, message):
        """Handle the help command."""
        print(f"Help called by {message.chat.username}")
        await message.reply(self.HELP_RESPONSE.format("help"))


    # Text handlers
    async def handle_text(self, client: Client, message):
        """Handle the text message."""
        if message.text:
            print(message.from_user.username, message.text)
            username = message.chat.username if message.chat else "usuário"
            user_id = message.from_user.id

            if (self.verify_message(message.text)):
                try:
                    # Start the crewai integration for webscrping
                    await message.reply("Realizando a busca...")
                    crew = CrewaiIntegration(username, message.text, user_id)
                    result = crew._run()

                    await message.reply("Busca concluída! Processando resultados...")
                    print("CrewAI terminou")
                    await self._send_long_message(message, result)
                    await self._send_long_message(message, 'terminou teste')
                    
                except Exception as e:
                    print(f"Erro ao executar crew: {e}")
                    await message.reply(f"Ocorreu um erro durante a busca: {str(e)}")

            else:
                await message.reply(f"Você precisa me informar seu estado e escolaridade para realizar a busca\nUse /help para ajudar")


    async def handle_unsupported(self, client: Client, message):
        """Handle unsupported message types like images or audio."""
        username = message.from_user.username if message.from_user else "usuário"
        print(f"Unsupported message type from {username}")
        await message.reply(self.DEFAULT_RESPONSE)
