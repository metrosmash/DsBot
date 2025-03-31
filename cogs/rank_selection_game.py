import discord
from discord.ext import commands
import random

class Rank_selection(commands.Cog):
    """This Cog works for a simple rank selection game and also a guess game """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rank_selection')
    async def rank_selection(self, ctx, rank1: int = None, rank2: int = None, rank3: int = None, rank4: int = None):
        """
        This command starts a rank selection game using the initial selection as basis for the game
        :param ctx:
        :param rank1:
        :param rank2:
        :param rank3:
        :param rank4:
        :return:
        """
        if rank1 is None or rank2 is None or rank3 is None or rank4 is None:
            await ctx.send("You must provide exactly 4 ranks. Usage: $rank_selection <rank1> <rank2> <rank3> <rank4>")
            return

        player1_selection = [rank1, rank2, rank3, rank4]
        await ctx.send(f"You have selected {player1_selection} from rank 1 to 10")
        await ctx.send("Player2 please guess one of the ranks selected by Player1")

        try:
            message = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
            player2_predict = int(message.content)
        except TimeoutError:
            return await ctx.send(f'Sorry, you took too long to answer.')

        if player2_predict in player1_selection:
            await ctx.send(f"You got {player2_predict} correct")
        else:
            await ctx.send("You did not get the answer correct")

    @rank_selection.error
    async def rank_selection_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must provide exactly 4 ranks. Usage: $rank_selection <rank1> <rank2> <rank3> <rank4>")



    @commands.command(name='guess')
    async def guess(self, ctx):
        """
        This command starts a guess game with the computer user chooses from (1-10)
        :param ctx:
        :return:
        """
        answer = random.randint(1, 10)
        message = 'Guess a number between 1 and 10.'
        embed = discord.Embed(title="Guess Game", description=message, color=0x00ff00)
        await ctx.send(embed=embed)

        try:
            player_guess = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
        except TimeoutError:
            return await ctx.send(f'Sorry, you took too long to answer .')

        if player_guess == answer:
            await ctx.send("WoW You are Correct ")
        else:
            await ctx.send(f" You are Wrong the answer is: {answer}. Please Try Again")


async def setup(bot):
    await bot.add_cog(Rank_selection(bot))