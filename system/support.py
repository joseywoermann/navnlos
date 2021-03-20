import discord
from discord.ext import commands
import logging

class Support(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def support(self, ctx, r=None):

        ping_embed = discord.Embed(title=f"Join the official support-server: https://discord.gg/52TbNHPBU9", colour=0x75e8ee)
        ping_embed.set_footer(text = "$support | @navnløs")

        await ctx.reply(content=None, embed=ping_embed)

def setup(client):
    client.add_cog(Support(client))
