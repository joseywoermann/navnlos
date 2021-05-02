import discord
from discord.ext import commands

class create_role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if  not discord.utils.get(guild.roles, name="in voicechat"):
            await guild.create_role(name = "in voicechat", reason = "This role is assigned to people that are in voice channels. DO NOT CHANGE THE NAME (unless you don't want this feature)!")

def setup(client):
    client.add_cog(create_role(client))
