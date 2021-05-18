import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name = "ping", description = "Shows the latency of the bot.", guild_ids = test_guilds)
    async def _ping(self, ctx: SlashContext):
        embed = Ping.make(self, ctx)
        await ctx.send(embed = embed)

    # make the content
    def make(self, ctx):

        embed = discord.Embed(title=f"Pong! {round(self.client.latency * 1000)} milliseconds", colour=0x75e8ee)
        return embed


def setup(client):
    client.add_cog(Ping(client))
