# PCI Concursos Scrap Bot

Bot para Telegram desenvolvido em Python que utiliza agentes de IA (CrewAI) para realizar webscraping e buscar informações sobre concursos públicos no site [PCI Concursos](https://www.pciconcursos.com.br/).

## 📋 Sobre o Projeto

Este projeto é um chatbot inteligente que ajuda usuários a encontrar concursos públicos de acordo com suas preferências (região, estado, nível de escolaridade, etc.). O bot utiliza uma equipe de agentes de IA especializados que trabalham em conjunto para:

1. **Planejar a pesquisa** - Identificar os pontos-chave da solicitação do usuário
2. **Coletar dados** - Realizar webscraping no site PCI Concursos
3. **Analisar informações** - Processar e analisar os dados coletados
4. **Resumir conteúdo** - Criar resumos concisos das descobertas
5. **Gerar relatório final** - Compilar um relatório completo em markdown

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **Pyrogram** - Biblioteca para interação com a API do Telegram
- **TgCrypto** - Biblioteca para melhor performance nas operações criptográficas
- **CrewAI** - Framework para criação de equipes de agentes de IA
- **CrewAI Tools** - Ferramentas para os agentes (webscraping, etc.)
- **Scrapfly SDK** - API para webscraping avançado
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **UV** - Gerenciador de dependências e pacotes Python

## 📦 Estrutura do Projeto

```
PCI_Concursos_scrap_bot/
├── src/
│   ├── main.py                          # Ponto de entrada do bot
│   ├── settings.py                      # Configurações e variáveis de ambiente
│   └── handlers/
│       ├── messages.py                  # Handler de mensagens do Telegram
│       ├── messages_text.py            # Textos e validações de mensagens
│       ├── crew_integration.py         # Integração com CrewAI
│       └── crewAgents/
│           ├── knowledge/
│           │   └── user_preference.txt # Preferências do usuário
│           └── src/
│               └── webscrap_concursos/
│                   ├── crew.py         # Configuração da equipe CrewAI
│                   ├── config/
│                   │   ├── agents.yaml # Configuração dos agentes
│                   │   └── tasks.yaml  # Configuração das tarefas
│                   └── tools/
│                       ├── ConcursoScrapeTool.py  # Tool para scraping do PCI Concursos
│                       └── ScrapflyTool.py        # Tool para scraping com Scrapfly
├── output/                              # Arquivos gerados pelos agentes
├── pyproject.toml                       # Configuração do projeto e dependências
├── uv.lock                              # Lock file do UV
└── README.md                            # Este arquivo
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.13 ou superior
- [UV](https://github.com/astral-sh/uv) instalado
- Conta no Telegram
- Conta no Scrapfly (opcional, mas recomendado)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JPKP-Kuhn/PCI_Concursos_Scrap_Bot.git
   cd PCI_Concursos_scrap_bot
   ```

2. **Instale as dependências usando UV:**
   ```bash
   uv sync
   ```

3. **Configure as variáveis de ambiente:**
   
   Copie o arquivo `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edite o arquivo `.env` e preencha com suas credenciais (veja a seção [Credenciais](#-credenciais) abaixo).

4. **Ative o ambiente virtual (se necessário):**
   ```bash
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate      # Windows
   ```

## 🔑 Credenciais

### Credenciais do Telegram

Para obter as credenciais do Telegram, você precisará:

1. **Bot Token e Bot Name:**
   - Inicie uma conversa com [@BotFather](https://t.me/BotFather) no Telegram
   - Envie o comando `/newbot`
   - Siga as instruções para criar um novo bot
   - Você receberá um `BOT_TOKEN` e deverá definir um `BOT_NAME`

2. **API ID e API Hash:**
   - Acesse [https://my.telegram.org](https://my.telegram.org)
   - Faça login com seu número de telefone
   - Acesse "API Development Tools"
   - Crie um novo aplicativo preenchendo os dados obrigatórios
   - Você receberá o `TELEGRAM_API_ID` e `TELEGRAM_API_HASH`

### Credenciais do Scrapfly (Opcional)

1. Acesse [https://scrapfly.io](https://scrapfly.io)
2. Crie uma conta e obtenha sua API Key
3. Adicione a chave no arquivo `.env` como `SCRAPFLY_API_KEY`

> **Nota:** O Scrapfly é opcional, mas recomendado para melhor performance no webscraping. O bot também pode funcionar sem ele, utilizando apenas as ferramentas nativas do CrewAI.

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
# Telegram
BOT_NAME=seu_bot_name
TELEGRAM_API_ID=seu_api_id
TELEGRAM_API_HASH=seu_api_hash
TELEGRAM_BOT_TOKEN=seu_bot_token

# Scrapfly (Opcional)
SCRAPFLY_API_KEY=sua_scrapfly_api_key
```

## 🎮 Como Usar

### Executar o Bot

Após configurar todas as credenciais, execute o bot:

```bash
uv run python src/main.py
```

Ou se estiver com o ambiente virtual ativado:

```bash
python src/main.py
```

### Comandos do Bot

- `/start` - Inicia o bot e exibe mensagem de boas-vindas
- `/help` - Exibe ajuda sobre como usar o bot

### Como Buscar Concursos

Envie uma mensagem de texto ao bot informando:
- **Região ou Estado:** Ex: "Sul", "São Paulo", "Santa Catarina", etc.
- **Nível de Escolaridade:** Ex: "Ensino Médio", "Ensino Superior", "Fundamental", etc.

**Exemplos de mensagens válidas:**
- "Busco concursos em São Paulo para ensino médio"
- "Quero concursos no Sul com ensino superior"
- "Santa Catarina, ensino médio completo"

O bot irá:
1. Validar sua mensagem
2. Processar a solicitação com os agentes de IA
3. Realizar webscraping no site PCI Concursos
4. Analisar e resumir os resultados
5. Enviar um relatório completo em markdown

## 🧪 Testes

### Testar o Bot Localmente

1. **Verifique se todas as dependências estão instaladas:**
   ```bash
   uv sync
   ```

2. **Verifique se o arquivo `.env` está configurado corretamente:**
   ```bash
   cat .env
   ```

3. **Execute o bot:**
   ```bash
   uv run python src/main.py
   ```

4. **Teste no Telegram:**
   - Abra o Telegram e procure pelo seu bot pelo username
   - Envie `/start` para iniciar
   - Envie `/help` para ver as opções
   - Envie uma mensagem com região/estado e escolaridade

### Testar os Agentes CrewAI

Os agentes CrewAI podem ser testados diretamente através da integração no bot. Quando você enviar uma mensagem válida, os agentes serão executados automaticamente.

Os resultados intermediários são salvos na pasta `output/`:
- `content_planner.json` - Plano de pesquisa gerado
- `webscrap.md` - Dados coletados do webscraping
- `data_analysis.md` - Análise dos dados
- `content_resume.md` - Resumo do conteúdo
- `final_report.md` - Relatório final

## 📝 Agentes CrewAI

O projeto utiliza 5 agentes especializados que trabalham em sequência:

1. **Context Planner Agent** - Planeja a pesquisa identificando pontos-chave
2. **Webscrap Agent** - Coleta dados do site PCI Concursos
3. **Data Analysis Agent** - Analisa os dados coletados
4. **Content Resume Agent** - Cria resumos concisos
5. **Final Report Agent** - Compila o relatório final em markdown

Cada agente possui configurações específicas definidas em `src/handlers/crewAgents/src/webscrap_concursos/config/agents.yaml` e `tasks.yaml`.

## 🔧 Desenvolvimento

### Estrutura Baseada em Template

Este projeto utiliza como base o template de bot do Telegram disponível em: [https://github.com/sergio-r1/bot_telegram](https://github.com/sergio-r1/bot_telegram)

### Adicionar Novos Comandos

Para adicionar novos comandos, edite o arquivo `src/handlers/messages.py` e adicione novos handlers.

### Modificar Agentes

Para modificar os agentes CrewAI:
- Edite `src/handlers/crewAgents/src/webscrap_concursos/config/agents.yaml` para modificar agentes
- Edite `src/handlers/crewAgents/src/webscrap_concursos/config/tasks.yaml` para modificar tarefas
- Edite `src/handlers/crewAgents/src/webscrap_concursos/crew.py` para modificar a lógica da equipe

## 📄 Licença

Este projeto é baseado no template [bot_telegram](https://github.com/sergio-r1/bot_telegram) e foi adaptado para incluir funcionalidades de webscraping com CrewAI.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através do email: pedrojoaojpk@gmail.com

---

**Nota:** Este README será atualizado conforme o projeto evolui.

