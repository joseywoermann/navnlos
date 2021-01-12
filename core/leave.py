import discord
from discord.ext import commands
import logging

class Leave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    @commands.guild_only()
    async def leave(self, ctx, id=None):

        jcw05 = self.client.get_user(586206645592391711)

        if id:
            server = client.get_guild(int(id))

        else:
            server = ctx.guild

        await server.leave()

        await jcw05.send("Left ***" + str(server.name) + "***. Server-ID: " + str(server.id))

def setup(client):
    client.add_cog(Leave(client))
