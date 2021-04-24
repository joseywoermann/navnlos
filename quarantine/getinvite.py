import discord
from discord.ext import commands

class GetInvite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def getinvite(self, ctx):
        server = self.client.get_guild(792431747123249172)
        channel = server.get_channel(793154908908027975)
        invite = await channel.create_invite()
        
        await ctx.reply(invite)

def setup(client):
    client.add_cog(GetInvite(client))
