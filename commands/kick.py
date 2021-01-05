import discord
from discord.ext import commands
import logging

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, person: discord.Member, *, reason=None):

        kick_embed = discord.Embed(title=str(person) + " wurde gekickt.", colour=discord.Color.dark_red())
        kick_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        kick_error_embed = discord.Embed(title="User konnte nicht gekickt werden.", colour=discord.Color.dark_purple())
        kick_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


        await ctx.channel.purge(limit=1)
        try:

            await person.kick(reason=reason)
            await ctx.send(content=None, embed=kick_embed)


        except:

            await ctx.send(content=None, embed=kick_error_embed)
            sleep(5)
            await ctx.channel.purge(limit=1)


def setup(client):
    client.add_cog(Kick(client))
