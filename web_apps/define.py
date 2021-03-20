import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import logging

class Define(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['def'])
    @commands.guild_only()
    async def define(self, ctx, *, search_term):

        URL = "https://www.urbandictionary.com/define.php?term=" + str(search_term)
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

        define_embed = discord.Embed(title=name_output, description=meaning_output, color=0x75e8ee)
        await ctx.reply(content=None, embed=define_embed)

def setup(client):
    client.add_cog(Define(client))
