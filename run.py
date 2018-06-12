import discord
import secreto
import asyncio
import youtube-dl

client = discord.Client()
TOKEN = secreto.seu_token()

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")
    await client.change_presence(game=discord.Game(name="Lofi Hip-Hop 24 Horas"))

@client.event
async def on_message(message):
    if message.content.startswith('s1!entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "```ERRO: Nenhum canal de voz encontrado.```")
        except Exception as error:
            await client.send_message(message.channel, "```ERRO: {error}```".format(error=error))

    if message.content.startswith('s1!sair'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "```ERRO: Eu não estou conectado em nenhuma sala de VOZ neste momento.```")
        except Exception as Hugo:
            await client.send_message(message.channel, "```ERRO: {haus}```".format(haus=Hugo))

    if message.content.startswith('s1!tocar'):
        try:
            yt_url = message.content[6:]
            channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yt_url)
            players[message.server.id] = player
            player.start()
        except:
            await client.send_message(message.channel, "```Erro.```")

    if message.content.startswith('s1!pausar'):
        try:
            players[message.server.id].pause()
        except:
            pass
    if message.content.startswith('s1!resume'):
        try:
            players[message.server.id].resume()
        except:
            pass


client.run(TOKEN)
