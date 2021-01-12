import discord
from discord.ext import commands
import logging

class Price(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['preis'])
    @commands.guild_only()
    async def price(self, ctx, *, search_term):

        while ' ' in search_term:
            search_term = search_term.replace(' ', '+')

        await ctx.reply("https://geizhals.de/?fs=" + search_term)

def setup(client):
    client.add_cog(Price(client))
