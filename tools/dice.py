import discord
from discord.ext import commands
import random

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def dice(self, ctx, arg=6):

        dice_result = random.randint(1, arg)
        dice_embed = discord.Embed(title=f"Random number between 1 and {arg}:\n\n=> {dice_result}", color=0x75e8ee)
        dice_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        dice_embed.set_footer(text = "$dice | @navnløs")

        await ctx.reply(content=None, embed=dice_embed)

def setup(client):
    client.add_cog(Dice(client))
