import discord

# Insira o seu token de bot aqui
TOKEN = 'SEU_TOKEN_AQUI'

# Cria uma instância do cliente Discord
intents = discord.Intents.default()
intents.message_content = True  # Habilita a leitura do conteúdo das mensagens
client = discord.Client(intents=intents)

# Evento que é acionado quando o bot está pronto para ser usado
@client.event
async def on_ready():
    print(f'Logado como {client.user}')

# Evento que é acionado quando uma mensagem é recebida
@client.event
async def on_message(message):
    # Ignora mensagens enviadas pelo próprio bot para evitar loops
    if message.author == client.user:
        return

    # Responde à mensagem "!oi"
    if message.content.lower() == '!oi':
        await message.channel.send('Olá para você também!')

    # Responde à mensagem "!ping" com o tempo de resposta do bot
    if message.content.lower() == '!ping':
        await message.channel.send(f'Pong! Latência: {round(client.latency * 1000)}ms')

# Executa o bot com o seu token
client.run(TOKEN)