import discord
import os


print (str(os.environ.get('DISCORD_TOKEN')))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
discord_token = str(os.environ.get('DISCORD_TOKEN'))

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, world!')

client.run(discord_token)