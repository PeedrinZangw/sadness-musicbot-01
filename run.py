import discord
import asyncio
import random
import secreto

client = discord.Client()
TOKEN = secreto.seu_token()
DEIN_USERNAME = "376830307321511966"

@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await client.change_presence(game=discord.Game(name="Lofi Hip-Hop 24 Horas"))


@client.event
async def on_message(message):
    if message.content.lower().startswith('s1!teste'):
        await client.send_message(message.channel, "```Mensagem de TESTE...```")

    if message.content.lower().startswith('s1!moeda'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '??')
        if choice == 2:
            await client.add_reaction(message, '??')

    if message.content.startswith('s1!status') and message.author.id == DEIN_USERNAME:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Meu status foi alterado para " + game + "")



client.run('TOKEN')