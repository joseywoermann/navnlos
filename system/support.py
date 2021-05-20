import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed

class Support(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "support",
        description = "Do you need help with the bot?",
        #guild_ids = test_guilds
    )
    async def _support(self, ctx: SlashContext):
        await ctx.send("**Join our official support server!** https://discord.gg/52TbNHPBU9")


def setup(client):
    client.add_cog(Support(client))
