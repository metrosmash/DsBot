import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_HERE = os.getenv("DISCORD_TOKEN_KEY")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$' , intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def rank_selection(ctx, *ranks):
    saved_keeper_selection = ', '.join(ranks)
    await ctx.send(f'{len(ranks)} arguments: {saved_keeper_selection}')


bot.run(TOKEN_HERE)