class MessagesText:
    DEFAULT_RESPONSE = "Sem suporte, use /help para saber como eu posso te ajudar."

    START_RESPONSE = f"Sou o bot que te ajuda a buscar por novos concursos públicos, do que você precisa? Digite /help para ver as opções disponíveis."

    HELP_RESPONSE = f"""
    - Primeiro, me informe qual a região, 'Norte', 'Sul', que você está buscando concursos, depois o seu estado, 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', etc.
    - Também preciso saber qual a sua escolaridade, por exemplo, 'Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', etc.
    """
 
    def get_greeting(self, username: str | None = None) -> str:
        """Retorna a mensagem de saudação com o username do usuário.
        
        Args:
            username: Nome de usuário do Telegram (opcional)
            
        Returns:
            Mensagem de saudação formatada
        """
        FIRST_MESSAGE = (
            "Utilizo como base o site https://www.pciconcursos.com.br/ para buscar concursos\n"
            "Comandos suportados /start e /help\n"
            "Apenas suporto mensagens de texto\n"
        )
        if username:
            message = f"Olá, {username}!\n" + FIRST_MESSAGE
            return message
        return "Olá, Novo Usuário!\n" + FIRST_MESSAGE

