import discord
from discord.ext import commands
import random

class Admin(commands.Cog):
    """This is a Cog with Admin only commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', hidden=True)  # This command is hidden from the help menu.
    # This is the decorator for commands (inside of cogs).
    @commands.is_owner()
    # Only the owner (or owners) can use the commands decorated with this.
    async def ban(self, ctx, member: discord.User = None, reason=None):
        """
        This command unbans a user from the server.
        :param ctx:
        :param member: The member specified to be kicked
        :param reason: The reason why the User should be kicked (can be empty)
        :return:
        """
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason == None:
            reason = "No Reason Provided"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} has been banned!")

    @commands.command(name='unban', hidden=True)
    @commands.is_owner()
    async def unban(self, ctx, member: discord.User = None, reason=None):
        """
        This command kicks a user from the server.
        :param ctx:
        :param member: The member specified to be unbanned
        :param reason: The reason why the User should be unbanned (can be empty)
        :return:
        """
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot unban yourself")
            return
        await ctx.guild.unban(member, reason=reason)
        await ctx.channel.send(f"{member} has been unbanned!")

    @commands.command(name='kick', hidden=True)
    @commands.is_owner()
    async def kick(self, ctx, member: discord.User = None, reason=None):
        """
        This command kicks a user from the server.
        :param ctx:
        :param member: The member specified to be kicked
        :param reason: The reason why the User should be kicked (can be empty)
        :return:
        """
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself")
            return
        if reason == None:
            reason = "No Reason Provided"
        message = f"You have been kicked from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.kick(member, reason=reason)
        await ctx.channel.send(f"{member} has been kicked!")

# Setup function to add the Cog to the bot
async def setup(bot):
    await bot.add_cog(Admin(bot))