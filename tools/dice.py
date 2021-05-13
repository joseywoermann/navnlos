import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option
import random


options = [
    create_option(
        name = "limit",
        description = "The upper limit of the range.",
        option_type = 4,
        required = False
    )
]

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def dice(self, ctx, arg=6):
        embed = await Dice.make(self, ctx, arg)
        await ctx.reply(embed = embed)

    @cog_ext.cog_slash(name = "dice", description = "Generate a random number", options = options, guild_ids = test_guilds)
    async def _dice(self, ctx: SlashContext, limit = 6):
        async with ctx.channel.typing():
            embed = await Dice.make(self, ctx, limit)
        await ctx.send(embed=embed)

    async def make(self, ctx, limit):
        try:
            number = random.randint(1, limit)
            embed = discord.Embed(
                title = number
            )
        except Exception as e:
            embed = await make_error_embed(e)
        finally:
            return embed


def setup(client):
    client.add_cog(Dice(client))
