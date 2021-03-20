import discord
from discord.ext import commands
import logging

class ChannelEdit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def channeledit(self, ctx, *, new_name):
        
        await ctx.channel.purge(limit=1)
        if new_name:
            try:
                await ctx.channel.edit(name=new_name)
                ctx.send("Channel name updated!")
            except:
                pass

def setup(client):
    client.add_cog(ChannelEdit(client))
