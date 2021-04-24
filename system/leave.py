from discord.ext import commands

class Leave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    @commands.guild_only()
    async def leave(self, ctx, id=None):

        if id:
            server = self.client.get_guild(int(id))
            
        else:
            server = ctx.guild

        await server.leave()


def setup(client):
    client.add_cog(Leave(client))
