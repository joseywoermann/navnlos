import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

class SlashError(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx: SlashContext, ex):
        embed = await make_error_embed(ex)
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(SlashError(client))
