import discord
from discord import option
from discord.ext import commands
from discord.commands import SlashCommandGroup


def has_permission(permission: str):
    async def predicate(ctx: discord.ApplicationContext):
        return permission in ctx.channel.permissions_for(ctx.author)
    return commands.check(predicate)


class ServerAdministration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    srv = SlashCommandGroup("server")

    @srv.command()
    @has_permission("ban_members")
    async def ban(self, ctx: discord.ApplicationContext, user: discord.User, reason: str="None."):
        """Ban a member from the server."""
        await ctx.guild.ban(user, reason=reason)
        await ctx.respond("The user has been banned.")

    @srv.command()
    @has_permission("kick_members")
    async def kick(self, ctx: discord.ApplicationContext, user: discord.User, reason: str="None."):
        """Kick a member from the server."""
        await ctx.guild.kick(user, reason=reason)
        await ctx.respond("The user has been kicked.")


def setup(bot):
    bot.add_cog(ServerAdministration(bot))
