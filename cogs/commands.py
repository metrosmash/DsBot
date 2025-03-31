import discord
from discord.ext import commands
import random
class Commands(commands.Cog):
    """This is a cog that sets a lists of commands to be used for the bot. """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message):
        """This command outputs the string that is being passed as argument.

        Args:
            self
            ctx
            *, message (this sets the 'consume rest' behaviour for arguments)
        """

        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Sends a message with bot's latency in ms in the channel where the command has been invoked.

        Note:
            `bot.latency` outputs the latency in seconds.
        """
        await ctx.send(f'🏓 {round(self.bot.latency * 1000)} ms.')

# Setup function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(Commands(bot))