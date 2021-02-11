import discord
from discord.ext import commands
import logging
from asyncio import sleep

class Join_leave_notification(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        owner = self.client.get_user(586206645592391711)
        await owner.send("Joined server \"" + str(ctx.name) + "\" (" + str(ctx.id) + ")")

def setup(client):
    client.add_cog(Join_leave_notification(client))
