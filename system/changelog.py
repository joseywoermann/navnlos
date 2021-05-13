import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option
import requests
from bs4 import BeautifulSoup


class Changelog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['cl'])
    @commands.guild_only()
    async def changelog(self, ctx):
        async with ctx.channel.typing():
            embed = await Changelog.make(self, ctx)
        await ctx.reply(embed=embed)

    @cog_ext.cog_slash(name = "changelog", description = "Show the changes in the latest release.", guild_ids = test_guilds)
    async def _changelog(self, ctx: SlashContext):
        async with ctx.channel.typing():
            embed = await Changelog.make(self, ctx)
        await ctx.send(embed=embed)


    async def make(self, ctx):
        try:
            URL = "https://github.com/joseywoermann/navnlos/releases/"
            page = requests.get(URL)
            fetched_page = BeautifulSoup(page.content, 'html.parser')

            changelog1 = fetched_page.find('div', attrs={'class': 'markdown-body'})

            if changelog1:
                changelog1_out = str(changelog1.text)
            else:
                changelog1_out = "No data."

            version1 = fetched_page.find('div', attrs={'class': 'f1 flex-auto min-width-0 text-normal'})

            if version1:
                version1_out = str(version1.text)
            else:
                version1_out = "No data."

            embed = discord.Embed(title=f"Changelog for {version1_out}", color=0x75e8ee)
            embed.add_field(name="Changes:", value=changelog1_out)
            embed.set_footer(text = "$changelog | @navnløs")

        except Exception as e:
            embed = await make_error_embed(e)
        finally:
            return embed

def setup(client):
    client.add_cog(Changelog(client))
