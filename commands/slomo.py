import discord
from discord.ext import commands
import logging

class Slomo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def slomo(self, ctx, delay):

        slomo_embed = discord.Embed(title="Slowmode auf " + str(delay) + " Sekunden gesetzt.", color=discord.Color.dark_red())
        slomo_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.channel.edit(slowmode_delay=delay)
        await ctx.send(content=None, embed=slomo_embed)


def setup(client):
    client.add_cog(Slomo(client))
