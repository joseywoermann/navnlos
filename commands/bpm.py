import discord
from discord.ext import commands
import logging

class BPM(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def bpm(self, ctx, *, search_term):

        while ' ' in search_term:
            search_term = search_term.replace(' ', '-')

        await ctx.send("https://songbpm.com/searches/" + search_term)
def setup(client):
    client.add_cog(BPM(client))
