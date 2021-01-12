import discord
from discord.ext import commands
from time import sleep
import logging

class BanID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def banid(self, ctx, user_id, *, reason=None):
        user = await self.client.fetch_user(user_id)
        ban_embed = discord.Embed(title=str(user.name) + " wurde gebannt.", color=discord.Color.dark_red())
        ban_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        ban_error_embed = discord.Embed(title="User konnte nicht gebannt werden", color=discord.Color.dark_purple())
        ban_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        user = await client.fetch_user(user_id)

        try:
            await ctx.guild.ban(user, reason=reason)
            await ctx.reply(content=None, embed=ban_embed)

        except:
            await ctx.reply(content=None, embed=ban_error_embed)
            sleep(5)


def setup(client):
    client.add_cog(BanID(client))
