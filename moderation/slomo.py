import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "delay",
        description = "How long should the delay be?",
        option_type = 4,
        required = True
    )
]

class SlowMode(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "slowmode",
        description = "Enable slowmode in the current channel.",
        options = options,
        #guild_ids = test_guilds
    )
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def _slowmode(self, ctx: SlashContext, delay):
        embed = await SlowMode.make(self, ctx, delay)
        await ctx.send(embed=embed)


    async def make(self, ctx, delay):
        try:
            embed = discord.Embed(
                title = f"Set slowmode to {delay} seconds",
                color = discord.Color.dark_red()
            )
            await ctx.channel.edit(slowmode_delay=delay)

        except Exception as e:
            embed = await make_error_embed(e)
        finally:
            return embed


def setup(client):
    client.add_cog(SlowMode(client))
