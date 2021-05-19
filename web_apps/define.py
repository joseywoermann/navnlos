import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "query",
        description = "Which word do you want to look up?",
        option_type = 3,
        required = True
    )
]

class Define(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name = "define", description = "Look up a word on urbandictionary.com", options = options, guild_ids = test_guilds)
    async def _define(self, ctx: SlashContext, query):
        embed = await Define.make(self, ctx, query)
        await ctx.send(content=None, embed=embed)


    async def make(self, ctx, query):
        try:
            URL = "https://www.urbandictionary.com/define.php?term=" + str(query)
            page = requests.get(URL)
            fetched_page = BeautifulSoup(page.content, 'html.parser')

            searched_word = fetched_page.find('a', attrs={'class': 'word'})
            meaning = fetched_page.find('div', attrs={'class': 'meaning'})

            if searched_word:
                name_output = str(searched_word.text)
            else:
                name_output = "No results."

            if meaning:
                meaning_output = str(meaning.text)
            else:
                meaning_output = "No results."

            embed = discord.Embed(title=name_output, description=meaning_output, color=0x75e8ee)
            embed.set_footer(text = "powered by urbandictionary.com")

        except Exception as e:
            embed = make_error_embed(e)
        
        finally:
            return embed

def setup(client):
    client.add_cog(Define(client))
