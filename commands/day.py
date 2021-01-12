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

        current_day = datetime.datetime.now().strftime("%A, der %d. %B %Y, der %j. Tag dieses Jahres")
        message = f"Heute ist {current_day}."
        day_embed = discord.Embed(title=str(message), color=discord.Color.gold())
        day_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.reply(content=None, embed=day_embed)

def setup(client):
    client.add_cog(Day(client))
