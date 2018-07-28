import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NDcyNTc5NzAyNDI3NzQ2MzA2.Dj1b7g.ImrLfBRHRq2z56YZO5CFWr0dBrU'
client = commands.Bot(command_prefix = 'rw!')

players = {}

@client.event
async def on_ready():
    print('Ratazanas bot - Online')
    await client.change_presence(game=discord.Game(name='discord.gg/nzbG5eR'))
    canal = client.get_channel("467101617762730016")
    msg = "Olá Mundo! :fire:\nAcabei de ser inicializado.\nhttps://i.imgur.com/4yB6I4V.jpg"
    await client.send_message(canal, msg)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconect()

@client.command(pass_context=True)
async def play (ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.event
async def on_member_join(member):
  canal = client.get_channel("467101617762730016")
  regras = client.get_channel("467103656219508736")
  msg = "Bem-vindo {} ao Ratazana's World\nAntes de tudo leia as regras no canal {}\n\nAgora você está seguro com a tropa Ratazana.\nhttps://i.imgur.com/4yB6I4V.jpg".format(member.mention, regras.mention)
  await client.send_message(canal, msg)

@client.event
async def on_membro_join(member):
  canal = client.get_channel("467101617762730016")
  regras = client.get_channel("467103656219508736")
  msg = "Bem-vindo {} ao Ratazana's World\nAntes de tudo leia as regras no canal {}\n\nAgora você está seguro com a tropa Ratazana.\nhttps://i.imgur.com/4yB6I4V.jpg".format(member.mention, regras.mention)
  await client.send_message(member, msg)

client.run(TOKEN)
