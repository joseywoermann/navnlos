import discord
from discord.ext import commands

class Slomo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def slomo(self, ctx, delay=15):

        slomo_embed = discord.Embed(title=f"Set slowmode to {delay} seconds", color=discord.Color.dark_red())
        slomo_embed.set_footer(text = "$slomo | @navnløs")

        await ctx.channel.edit(slowmode_delay=delay)
        await ctx.reply(content=None, embed=slomo_embed)


def setup(client):
    client.add_cog(Slomo(client))
