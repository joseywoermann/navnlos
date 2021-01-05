import discord
from discord.ext import commands
import logging
from time import sleep

class On_member_join(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        server = ctx.guild
        if server.id == 304191437652623360:
            member_count_channel = self.client.get_channel(732309561293275198)
            member_count = server.member_count
            await member_count_channel.edit(name="Member: " + str(member_count))
        else:
            pass

def setup(client):
    client.add_cog(On_member_join(client))
