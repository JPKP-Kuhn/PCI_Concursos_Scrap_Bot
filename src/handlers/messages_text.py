class MessagesText:
    """Classe Responsável por alguns padrões de mensagem e verificações"""

    DEFAULT_RESPONSE = "Sem suporte, use /help para saber como eu posso te ajudar."

    START_RESPONSE = f"Sou o bot que te ajuda a buscar por novos concursos públicos, do que você precisa? Digite /help para ver as opções disponíveis."

    HELP_RESPONSE = """
        - Primeiro, me informe qual a região, 'Norte', 'Sul', que você está buscando concursos, depois o seu estado, 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', etc;\n- Também preciso saber qual a sua escolaridade, por exemplo, 'Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', etc.\n
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

    def verify_message(self, message: str) -> bool:
        """Verifica se a mensagem está de acordo com as exigências do bot.
        Proteção para não usar o crewai

        Args:
            message: Mensagem enviada pelo usuário

        Returns:
            True se message especifica um estado e um nível de escolaridade
            False se não possuir nada de acordo com o exigido
        """
        message = message.lower()

        regioes = ['norte', 'sul', 'centro-oeste', 'centrooeste', 'centro oeste' 'nordeste', 'sudeste']
        estados = [
            'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma',
            'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn',
            'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to',

            'acre', 'alagoas', 'amapá', 'amazonas', 'bahia', 'ceará',
            'distrito federal', 'espírito santo', 'goiás', 'maranhão',
            'mato grosso', 'mato grosso do sul', 'minas gerais', 'pará',
            'paraíba', 'paraná', 'pernambuco', 'piauí', 'rio de janeiro',
            'rio grande do norte', 'rio grande do sul', 'rondônia', 'roraima',
            'santa catarina', 'são paulo', 'sergipe', 'tocantins'
        ]

        niveis_escolaridade = [
            "fundamental", "fundamental completo", "fundamental incompleto",
            "medio", "médio", "médio completo", "médio incompleto",
            "superior", "superior completo", "superior incompleto",
            "tecnico", "técnico"
        ]

        # Verifica região ou estado
        contem_regiao = any(r in message for r in regioes)
        contem_estado = any(e in message for e in estados)

        # Verifica escolaridade
        contem_escolaridade = any(s in message for s in niveis_escolaridade)

        return (contem_regiao or contem_estado) and contem_escolaridade

    def extract_state_abbreviation(self, message: str) -> str | None:
        """Extrai a sigla do estado da mensagem do usuário.
        
        Args:
            message: Mensagem enviada pelo usuário
            
        Returns:
            Sigla do estado (ex: 'SP', 'RJ', 'MG') ou None se não encontrar
        """
        message = message.lower()
        
        # Mapeamento de nomes de estados para siglas
        estado_to_sigla = {
            'ac': 'AC', 'acre': 'AC',
            'al': 'AL', 'alagoas': 'AL',
            'ap': 'AP', 'amapá': 'AP', 'amapa': 'AP',
            'am': 'AM', 'amazonas': 'AM',
            'ba': 'BA', 'bahia': 'BA',
            'ce': 'CE', 'ceará': 'CE', 'ceara': 'CE',
            'df': 'DF', 'distrito federal': 'DF',
            'es': 'ES', 'espírito santo': 'ES', 'espirito santo': 'ES',
            'go': 'GO', 'goiás': 'GO', 'goias': 'GO',
            'ma': 'MA', 'maranhão': 'MA', 'maranhao': 'MA',
            'mt': 'MT', 'mato grosso': 'MT',
            'ms': 'MS', 'mato grosso do sul': 'MS',
            'mg': 'MG', 'minas gerais': 'MG',
            'pa': 'PA', 'pará': 'PA', 'para': 'PA',
            'pb': 'PB', 'paraíba': 'PB', 'paraiba': 'PB',
            'pr': 'PR', 'paraná': 'PR', 'parana': 'PR',
            'pe': 'PE', 'pernambuco': 'PE',
            'pi': 'PI', 'piauí': 'PI', 'piaui': 'PI',
            'rj': 'RJ', 'rio de janeiro': 'RJ',
            'rn': 'RN', 'rio grande do norte': 'RN',
            'rs': 'RS', 'rio grande do sul': 'RS',
            'ro': 'RO', 'rondônia': 'RO', 'rondonia': 'RO',
            'rr': 'RR', 'roraima': 'RR',
            'sc': 'SC', 'santa catarina': 'SC',
            'sp': 'SP', 'são paulo': 'SP', 'sao paulo': 'SP',
            'se': 'SE', 'sergipe': 'SE',
            'to': 'TO', 'tocantins': 'TO',
        }
        
        # Busca pela sigla ou nome completo do estado
        for estado, sigla in estado_to_sigla.items():
            if estado in message:
                return sigla
        
        return None
