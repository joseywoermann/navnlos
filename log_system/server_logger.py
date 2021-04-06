import discord
from discord.ext import commands
import logging
from asyncio import sleep

class Join_leave_notification(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        owner = self.client.get_user(586206645592391711)
        await owner.send(f"Joined ***{guild.name}*** ({guild.id}).")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        owner = self.client.get_user(586206645592391711)
        await owner.send(f"Left ***{guild.name}*** ({guild.id}).")

def setup(client):
    client.add_cog(Join_leave_notification(client))
