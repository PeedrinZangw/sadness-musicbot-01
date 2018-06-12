import discord
import secreto
import asyncio
import random


client = discord.Client()
TOKEN = secreto.seu_token()

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")
	await client.change_presence(game=discord.Game(name='Lofi Hip-Hop 24 Horas'))

@client.event
async def on_message(message):
    if message.content.startswith('s1!entrar'):
      try:
        canal = message.author.voice.voice_channel
        await client.join_voice_channel(canal)
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "```Entrando no Canal de VOZ...```")

    if message.content.startswith('s1!sair'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"```ATENÇÃO: O BOT Não está conectado à nenhum canal de VOZ...```")
		  
    if message.content.lower().startswith('s1!teste'):
        await client.send_message(message.channel, "```Mensagem de TESTE...```")

    if message.content.lower().startswith('!moeda'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    if message.content.startswith('!game') and message.author.id == DEIN_USERNAME:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Meu status foi alterado para " + game + "")


client.run(TOKEN)
