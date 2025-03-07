import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN_HERE = os.getenv("DISCORD_TOKEN_KEY")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def Help(ctx):
    await ctx.send("""
Hello this Bot is a rank selection bot to play select 4 ranks in 1 to 10 
Commands: \n
$rank_selection rank1 ....
(NOTE: input the rank selected after the command leaving space between them )
This rank selection game can be played between two people (Essentially its P2P ) \n
$guess:
in this guess game  the computer selects a random number in between 1 and 10 then the player tries to 
predict it.
                  
                    """)



@bot.command()
async def rank_selection(ctx, rank1: int = None, rank2: int = None, rank3: int = None, rank4: int = None):
    if rank1 is None or rank2 is None or rank3 is None or rank4 is None:
        await ctx.send("You must provide exactly 4 ranks. Usage: $rank_selection <rank1> <rank2> <rank3> <rank4>")
        return

    player1_selection = [rank1, rank2, rank3, rank4]
    await ctx.send(f"You have selected {player1_selection} from rank 1 to 10")
    await ctx.send("Player2 please guess one of the ranks selected by Player1")

    try:
        message = await bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
        player2_predict = int(message.content)
    except TimeoutError:
        return await ctx.send(f'Sorry, you took too long to answer.')

    if player2_predict in player1_selection:
        await ctx.send(f"You got {player2_predict} correct")
    else:
        await ctx.send("You did not get the answer correct")

@rank_selection.error
async def rank_selection_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You must provide exactly 4 ranks. Usage: $rank_selection <rank1> <rank2> <rank3> <rank4>")


@bot.command()
async def guess(ctx):
    answer = random.randint(1, 10)
    await ctx.send('Guess a number between 1 and 10.')
    try:
        player_guess = await bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
    except TimeoutError:
        return await ctx.send(f'Sorry, you took too long to answer .')
    if player_guess == answer:
        await ctx.send("WoW You are Correct ")
    else:
        await ctx.send(f" You are Wrong the answer is: {answer}. Please Try Again")


bot.run(TOKEN_HERE)