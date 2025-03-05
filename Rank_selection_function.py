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

bot = commands.Bot(command_prefix='$' , intents=intents)



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

# This Handles the P2P game of Rank selection for this bot
@bot.command()
async def rank_selection(ctx, *ranks):
    player1_selection = ', '.join(ranks)
    await ctx.send(f"You have selected {player1_selection} from rank 1 to 10")
    await ctx.send("Player2 please guess one of the ranks selected by Player1 ")
    message = await bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
    player2_predict = message.content
    if player2_predict in player1_selection:
        await ctx.send(f"You got {player2_predict} correct ")
    else:
        await ctx.send("You did not get the answer correct ")


@bot.command()
async def guess(ctx):
    answer = random.randint(1, 10)
    await ctx.send('Guess a number between 1 and 10.')
    player_guess = await bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
    if player_guess == answer:
        await ctx.send("WoW You are Correct ")
    else:
        await ctx.send(f"You are Wrong the answer is : {answer}. Please Try Again")





bot.run(TOKEN_HERE)