import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração do Bot ---
# Você pode usar intents padrão (all_intents = discord.Intents.default())
# ou especificar as intents necessárias para o seu bot.
# Para este exemplo, precisaremos de algumas intents específicas para eventos e mensagens.
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens
intents.members = True          # Necessário para eventos de entrada/saída de membros

# Cria uma instância do Bot
# command_prefix define qual caractere (ou string) o bot vai esperar antes de um comando.
bot = commands.Bot(command_prefix='!', intents=intents)

# --- 1. Evento: Quando o Bot está pronto ---
@bot.event
async def on_ready():
    """
    Este evento é disparado quando o bot se conecta ao Discord e está pronto para uso.
    """
    print(f'Bot conectado como {bot.user.name} (ID: {bot.user.id})')
    print(f'Está em {len(bot.guilds)} servidor(es).')
    print('------')

# --- 2. Evento: Quando um novo membro entra no servidor ---
@bot.event
async def on_member_join(member):
    """
    Este evento é disparado quando um novo membro entra em um servidor onde o bot está.
    Envia uma mensagem de boas-vindas para o canal padrão (geralmente 'geral' ou o primeiro canal de texto).
    """
    print(f'{member.name} entrou no servidor {member.guild.name}.')
    # Tenta encontrar um canal de texto para enviar a mensagem
    # Você pode querer especificar um ID de canal aqui para maior robustez
    for channel in member.guild.text_channels:
        if "geral" in channel.name.lower() or channel == member.guild.system_channel:
            await channel.send(f'Seja bem-vindo(a), {member.mention}! Esperamos que você goste do nosso servidor!')
            break
    else:
        print(f'Não foi possível encontrar um canal padrão para saudar {member.name}.')

# --- 3. Comando Simples: Ping ---
@bot.command(name='ping')
async def ping(ctx):
    """
    Um comando simples que responde com 'Pong!' e a latência do bot.
    Uso: !ping
    """
    latency = round(bot.latency * 1000)  # Latência em milissegundos
    await ctx.send(f'Pong! Minha latência é de {latency}ms.')
    print(f'Comando !ping executado por {ctx.author} no canal {ctx.channel}.')

# --- 4. Comando com Argumento: Olá ---
@bot.command(name='ola')
async def hello(ctx, *, nome: str = "mundo"):
    """
    Um comando que cumprimenta o usuário ou um nome fornecido.
    Uso: !ola [nome]
    Ex: !ola João -> Olá, João!
    Ex: !ola     -> Olá, mundo!
    """
    await ctx.send(f'Olá, {nome}!')
    print(f'Comando !ola executado por {ctx.author} com argumento "{nome}".')

# --- 5. Comando de Embed (Mensagem Embelezada) ---
@bot.command(name='info')
async def info(ctx):
    """
    Envia uma mensagem embed formatada com informações básicas do bot.
    Uso: !info
    """
    embed = discord.Embed(
        title="Informações do Bot",
        description="Este é um bot de exemplo demonstrando funções básicas do `discord.py`.",
        color=discord.Color.blue() # Você pode usar cores pré-definidas ou um valor hexadecimal
    )
    embed.add_field(name="Autor", value=bot.user.name, inline=True)
    embed.add_field(name="Prefixo", value=bot.command_prefix, inline=True)
    embed.add_field(name="Servidores", value=len(bot.guilds), inline=False)
    embed.set_footer(text="Desenvolvido com discord.py")
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None) # Adiciona a imagem de perfil do bot
    await ctx.send(embed=embed)
    print(f'Comando !info executado por {ctx.author}.')

# --- 6. Manipulação de Erros (Exemplo Básico) ---
@bot.event
async def on_command_error(ctx, error):
    """
    Manipulador de erros para comandos.
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Ops! Comando não encontrado. Digite `{bot.command_prefix}help` para ver os comandos disponíveis.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Erro: Você esqueceu de fornecer um argumento necessário. Exemplo: `{bot.command_prefix}ola <seu_nome>`')
    else:
        print(f'Erro no comando {ctx.command}: {error}')
        await ctx.send(f'Ocorreu um erro inesperado ao executar o comando. Tente novamente mais tarde.')

# --- Inicia o Bot ---
# O token do seu bot deve ser mantido em segurança e nunca exposto publicamente.
# Recomendamos usar variáveis de ambiente (como neste exemplo com `dotenv`).
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("Erro: O token do Discord não foi encontrado! Certifique-se de ter um arquivo .env com DISCORD_TOKEN.")
else:
    bot.run(TOKEN)