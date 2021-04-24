from discord.ext import commands

class Bot_Chat(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.command()
    @commands.is_owner()
    async def sendto(self, ctx, server, channel, *, text):
        target = self.client.get_guild(int(server)).get_channel(int(channel))
        await target.send(str(text))
        
        
        
    @commands.command()
    @commands.is_owner()
    async def sendhere(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(str(text))

def setup(client):
    client.add_cog(Bot_Chat(client))
