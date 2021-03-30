import discord
from discord.ext import commands
import datetime
import logging

class Day(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def day(self, ctx):

        current_day = datetime.datetime.now().strftime("%A, the %d. of %B, %Y, which is the %j. day of this year")
        msg = f"Today is {current_day}."
        day_embed = discord.Embed(title=str(msg), color=0x75e8ee)

        await ctx.reply(content=None, embed=day_embed)

def setup(client):
    client.add_cog(Day(client))
