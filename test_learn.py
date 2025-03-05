import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_HERE = os.getenv("DISCORD_TOKEN_KEY")
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Bot is Logged {0.user}'
          .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hello! ')


intents = discord.Intents.default()
intents.message_content = True


client.run(os.getenv('DISCORD_TOKEN_KEY'))

