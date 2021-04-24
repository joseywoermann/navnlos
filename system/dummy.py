from discord.ext import commands

class Dummy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def dummy(self, ctx):
        print("$dummy got executed")
        pass

def setup(client):
    client.add_cog(Dummy(client))
