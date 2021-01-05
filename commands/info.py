# Preset am Beispiel $ping
import discord
from discord.ext import commands
import logging

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def info(self, ctx):

        info_embed = discord.Embed(title="Information", description="Version 2.0.1 by jcw05#1331\nhttp://navnlos.tk/", color=discord.Color.lighter_grey())
        info_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=info_embed)

def setup(client):
    client.add_cog(Info(client))
