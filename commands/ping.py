import discord
from discord.ext import commands
import logging

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx, r=None):

        if r == "precise":
            ping_embed = discord.Embed(title=f"Pong! {(self.client.latency * 1000)} Millisekunden", colour=discord.Color.gold())
            ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        else:
            ping_embed = discord.Embed(title=f"Pong! {round(self.client.latency * 1000)} Millisekunden", colour=discord.Color.gold())
            ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.reply(content=None, embed=ping_embed)

def setup(client):
    client.add_cog(Ping(client))
