import discord
from discord.ext import commands
import logging
import requests
from bs4 import BeautifulSoup


class Changelog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['cl'])
    @commands.guild_only()
    async def changelog(self, ctx):
        async with ctx.channel.typing():

            URL = "https://github.com/joseywoermann/navnlos/releases/"
            page = requests.get(URL)
            fetched_page = BeautifulSoup(page.content, 'html.parser')

            changelog1 = fetched_page.find('div', attrs={'class': 'markdown-body'})

            if changelog1:
                changelog1_out = str(changelog1.text)
            else:
                changelog1_out = "No dara."

            version1 = fetched_page.find('div', attrs={'class': 'f1 flex-auto min-width-0 text-normal'})

            if version1:
                version1_out = str(version1.text)
            else:
                version1_out = "No data."

            changelog_embed = discord.Embed(title="Changelog for " + version1_out, color=0x75e8ee)
            changelog_embed.add_field(name="Changes:", value=changelog1_out)
            changelog_embed.set_footer(text = "$changelog | @navnløs")

        await ctx.reply(embed=changelog_embed)

def setup(client):
    client.add_cog(Changelog(client))
