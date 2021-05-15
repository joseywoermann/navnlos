import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['p'])
    async def ping(self, ctx, arg=None):
        embed = Ping.make(self, ctx, arg)
        await ctx.reply(embed = embed)

    @cog_ext.cog_slash(name = "ping", description = "Shows the latency of the bot.", guild_ids = test_guilds)
    async def _ping(self, ctx: SlashContext, arg = None):
        embed = Ping.make(self, ctx, arg)
        await ctx.send(embed = embed)

    # make the content
    def make(self, ctx, arg):

        embed = discord.Embed(title=f"Pong! {round(self.client.latency * 1000)} milliseconds", colour=0x75e8ee)
        embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        return embed


def setup(client):
    client.add_cog(Ping(client))
