import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):

        embed = discord.Embed(
            title="Slash Commands are here!",
            description="Support for the regular commands has been dropped, please use Slash Commands from now on.",
        )

        await ctx.reply(embed=embed)

    @cog_ext.cog_slash(
        name="help",
        description="You don't need this. Use Slash Commands.",
        guild_ids=test_guilds,
    )
    async def _help(self, ctx: SlashContext):
        embed = discord.Embed(
            title="Type `/` to see all available commands.",
            description="A full list of features is available in the [navnløs-wiki](https://github.com/joseywoermann/navnlos/wiki).",
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
