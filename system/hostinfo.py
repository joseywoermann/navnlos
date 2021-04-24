import discord
from discord.ext import commands
import logging
import psutil

class HostInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def hostinfo(self, ctx):

        cpu_utilization = psutil.cpu_percent(interval=None)
        cpu_logical_cores = psutil.cpu_count()
        memory = psutil.virtual_memory()
        memory_total = memory.total / 1000000000

        specs_embed = discord.Embed(
            title="System information:",
            color=0x75e8ee
        )

        specs_embed.add_field(
            name = "Number of CPU cores:",
            value = f"{cpu_logical_cores} Cores"
        )

        specs_embed.add_field(
            name = "CPU utilization:",
            value = f"{cpu_utilization}%"
        )
        
        specs_embed.add_field(
            name = "Memory:",
            value = f"{round(memory_total, 0)} GB"
        )

        specs_embed.set_author(
            name=str(ctx.author),
            icon_url=ctx.author.avatar_url
        )

        await ctx.reply(embed=specs_embed)

def setup(client):
    client.add_cog(HostInfo(client))
