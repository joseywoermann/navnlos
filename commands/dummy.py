import discord
from discord.ext import commands
import logging

class Dummy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def dummy(self, ctx):
        await ctx.channel.purge(limit=1)


def setup(client):
    client.add_cog(Dummy(client))
