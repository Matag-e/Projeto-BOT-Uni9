import discord
from discord.ext import commands
import random
from discord.voice_client import VoiceClient
import youtube_dl





intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
intents.voice_states = True
intents.typing = True
intents.presences = True


testing = True

client = commands.Bot(command_prefix = ".", case_insensitive = True, intents=intents)

bot = commands.Bot(command_prefix=".",case_insensitive = True, intents=intents)

voice_client = commands.Bot(command_prefix = ".", case_insensitive = True, intents=intents)



client.remove_command('help')

@bot.event
async def on_ready():
    print('Bot está pronto!')
    await bot.change_presence(activity=discord.Game(name='Eae Tudo Bem? Use .help para te ajudar a me usar ^^'), status=discord.Status.online)
  
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(title="Informações do Usuário", color=member.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nome", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Cargo mais alto", value=member.top_role.mention, inline=True)
    embed.add_field(name="Entrou em", value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} mensagens foram apagadas.")    


@client.command() #permite o usuario rolar um dados de quantos lados ele quiser
async def d(ctx,numeros):
    variante = random.randint(1,int(numeros))
    await ctx.send(f'Você tirou : {variante} 🎲')

    
@client.command() # comando de kick, acaca por expulsar o membro dando possibilidade dele voltar ser necessario
async def kick(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.kick_members:
        msg = f'{ctx.author.mention} expulsou {membro.mention} por {motivo}'
        await membro.kick()
     
@client.command() # comando de ban, acaba banindo o usuario do servidor e impedindo sua volta
async def ban(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.ban_members:
        msg = f'{ctx.author.mention} baniu {membro.mention} por {motivo}'
        await membro.ban()


# Comando para conectar o bot a um canal de voz
@client.command()
async def join(ctx):
    global voice_client
    channel = ctx.author.voice.channel
    voice_client = await channel.connect()

# Comando para desconectar o bot do canal de voz
@client.command()
async def leave(ctx):
    global voice_client
    await voice_client.disconnect()

# Comando para reproduzir uma música
@client.command()
async def play(ctx, url):
    global voice_client
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        'verbose': True  # Opção verbose
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, method='fallback').to_audio_source()
        voice_client.play(source)
# Comando para pausar a reprodução de música
@client.command()
async def pause(ctx):
    global voice_client
    voice_client.pause()

# Comando para retomar a reprodução de música
@client.command()
async def resume(ctx):
    global voice_client
    voice_client.resume()

# Comando para parar a reprodução de música
@client.command()
async def stop(ctx):
    global voice_client
    voice_client.stop()


@client.command()
async def calc(ctx, *, expression):
    try:
        # Avalia a expressão matemática usando a função eval() do Python
        result = eval(expression)
        await ctx.send(f"\n```python\n🤓👆 {expression} = {result} \n```")
    except:
        await ctx.send("Erro ao avaliar a expressão. Verifique se a expressão é válida.")

@client.command() #comando para redirecionar usuarios aos serviços de suporte
async def link(ctx):
    await ctx.send(f'este link te levará ao site de suporte da equipe de desenvolvedores :  \
        \n https://bot-discordu9.netlify.app/')

@client.command()
async def dev(ctx):
    await ctx.send(' Vinicius Santos  \n RA : 423103791 \
                \n\n Pedro Henrique \n RA : 422104708 \
                \n\n Victor Kawan \n RA : 420202997\
                \n\n Carlos Augusto Ramos Da Silva \n RA : 423104993 \
                \n\n Mateus Santos Silva \n RA: 423101191 \
                \n\n Igor Araujo \n RA : 423104813')

@client.command()
async def help(ctx):
    await ctx.send (f'```\n COMANDOS GERAIS :\
        \n\n Comando para realizar um calculo = .calc (Ex : .calc 2+2) 📒\
        \n\n (simbolos : +(adição),-(subtração), * (multiplicação), /  (divisão), ** (potencia)) \
        \n\n Comando para o usuário utilizar o rolamento de dado para o lado que ele desejar = .d+num que desejar (.D 6 )🎲\
        \n\n Comando de penalização, serve para expulsar um usuário por um certo periodo de tempo = .kick ❎️\
        \n\n Comando de banimento, serve para banir o usuario do servidor impedindo o seu retorno = .ban  ❌️\
        \n\n Comando de informação de usuario, ele é usado para divulgar informações sobre o usuario escolhido tal como seu id, nome e foto da seguinte forma = .userinfo @usuario. 📝\
        \n\n comando de limpeza de chat, serve para limpar o excesso de mensagens em um chat = .clear (numero de linhas a apagar) 🚮\
        \n\n comando que irá levar para o site de suporte = .link 📶\
        \n ============================================================= \
        \n\n COMANDOS DE MUSICA :\
        \n\n Comando para reproduzir uma música = .play ▶️\
        \n Comando para pausar a reprodução de música = .pause ⏸️\
        \n Comando para retomar a reprodução de música = .resume 🔄\
        \n Comando para parar a reprodução de música = .stop ⏯️\
        \n Comando para conectar o bot a um canal de voz = .join ⏺️\
        \n Comando para desconectar o bot do canal de voz = .leave ⛔️\
        ```')



client.run('OTMxNzY3MTY3NzE4OTI0Mjg4.Gn22D7.uBrvX9gacwkhr4_37_X65lYm0ud_7KPyhCoM_E')


