from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

class Leave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    @commands.guild_only()
    async def leave(self, ctx, id=None):
        try:
            if id:
                server = self.client.get_guild(int(id))

            else:
                server = ctx.guild
            await ctx.channel.purge(limit=1)
            await server.leave()

        except Exception as e:
            await ctx.send(embed = await make_error_embed(e))

def setup(client):
    client.add_cog(Leave(client))
