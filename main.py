import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import tracemalloc

tracemalloc.start()

load_dotenv()
TOKEN_HERE = os.getenv("DISCORD_TOKEN_KEY")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents= intents, description="A bot by metro to serve "
                                                                    "the metro Guild")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    try:
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py'):
                await bot.load_extension(f'cogs.{cog[:-3]}')
        print("Cog loaded: my_cog")
    except Exception as e:
        print(f"Failed to load cog my_cog: {e}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Wrong command. Please try $help for more  information")

# @bot.event
# # This is the decorator for events (outside of cogs).
# async def on_ready():
#     """This coroutine is called when the bot is connected to Discord.
#     Note:
#         `on_ready` doesn't take any arguments.
#
#     Documentation:
#     https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready
#     """
#     print(f'{bot.user.name} is online and ready!')



@bot.command()
#This is the decorator for commands (outside of cogs).
async def greet(ctx):
    """This coroutine sends a greeting message when called by the command.
    Note:
        All commands must be preceded by the bot prefix.
    """
    await ctx.send(f'Hello {ctx.message.author.mention}!')
    #The bot send a message on the channel that is being invoked in and mention the invoker.


# Run the bot with your token
bot.run(TOKEN_HERE)