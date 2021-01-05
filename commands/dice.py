import discord
from discord.ext import commands
import logging
import random

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def dice(self, ctx, arg=6):

        dice_result = random.randint(1, arg)
        dice_embed = discord.Embed(title="Zufällige Zahl zwischen 1 und " + str(arg) + ":\n\nErgebnis: __" + str(dice_result) + "__", color=discord.Color.gold())
        dice_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(content=None, embed=dice_embed)

def setup(client):
    client.add_cog(Dice(client))
