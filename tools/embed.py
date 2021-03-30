import discord
from discord.ext import commands
import logging

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['embed'])
    @commands.guild_only()
    async def repeat(self, ctx, *, text):

        repeat_embed = discord.Embed(description=str(text), color=discord.Color.gold())
        repeat_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        repeat_embed.set_footer(text = "$embed | @navnløs")

        await ctx.channel.purge(limit = 1)
        await ctx.send(content=None, embed=repeat_embed)

def setup(client):
    client.add_cog(Embed(client))
