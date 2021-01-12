import discord
from discord.ext import commands
import logging
from time import sleep

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, person: discord.Member, *, reason=None):

        ban_embed = discord.Embed(title=str(person) + " wurde gebannt.", color=discord.Color.dark_red())
        ban_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        ban_error_embed = discord.Embed(title="User konnte nicht gebannt werden", color=discord.Color.dark_purple())
        ban_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


        await ctx.channel.purge(limit=1)
        try:

            await person.ban(reason=reason)
            await ctx.reply(content=None, embed=ban_embed)


        except:

            await ctx.reply(content=None, embed=ban_error_embed)
            sleep(5)


def setup(client):
    client.add_cog(Ban(client))
