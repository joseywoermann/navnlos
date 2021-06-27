from discord.ext import commands

class On_member_remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, ctx):

        server = ctx.guild
        for membercount_channel in server.channels:
            if membercount_channel.name.startswith("Members:"):
                await membercount_channel.edit(name = f"Members: {server.member_count}")
                break

def setup(client):
    client.add_cog(On_member_remove(client))
