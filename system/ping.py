import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['p'])
    async def ping(self, ctx, r=None):

        if r == "precise":
            ping_embed = discord.Embed(title=f"Pong! {(self.client.latency * 1000)} milliseconds", colour=0x75e8ee)
            ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
            ping_embed.set_footer(text = "$ping | @navnløs")

        else:
            ping_embed = discord.Embed(title=f"Pong! {round(self.client.latency * 1000)} milliseconds", colour=0x75e8ee)
            ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
            ping_embed.set_footer(text = "$ping | @navnløs")

        await ctx.reply(content=None, embed=ping_embed)

def setup(client):
    client.add_cog(Ping(client))
