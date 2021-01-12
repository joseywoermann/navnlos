import discord
from discord.ext import commands
import logging

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def embed(self, ctx, *, text):

        repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())
        repeat_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.reply(content=None, embed=repeat_embed)

def setup(client):
    client.add_cog(Embed(client))
