import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_HERE = os.getenv("DISCORD_TOKEN_KEY")



def handle_user_messages(msg) ->str:
    message = msg.lower() #Converts all inputs to lower case
    if(message == "hi"):
        return "Hi there"
    if(message == "hello"):
        return "Hello user. Welcome"


async def processMessage(message, user_message):
        try:
            botfeedback = handle_user_messages(user_message)
            await message.channel.send(botfeedback)
        except Exception as error:
            print(error)


def runBot():
    discord_token = TOKEN_HERE
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        await processMessage(message, 'hi')

    client.run(discord_token)


