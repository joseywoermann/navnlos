import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "invite",
        description = "Add me to your server!",
        #guild_ids = test_guilds
    )
    async def _invite(self, ctx: SlashContext):
        embed = await Invite.make(self, ctx)
        await ctx.send(content=None, embed=embed)


    async def make(self, ctx):
        try:
            invite = "https://nvnls.ml/add"
            embed = discord.Embed(
                title="Add me to your server!",
                url = invite,
                color=0x75e8ee
            )
        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed


def setup(client):
    client.add_cog(Invite(client))
