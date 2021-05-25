import discord
from discord.ext import commands
import requests
import json
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "url",
        description = "Provide a URL you want to shorten",
        option_type = 3,
        required = True
    )
]

class URLShort(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "shorturl",
        description = "Makes a long URL short.",
        options = options,
        #guild_ids = test_guilds
    )
    async def short(self, ctx: SlashContext, url):
        embed = await URLShort.make(self, ctx, url)
        await ctx.send(embed = embed)

    async def make(self, ctx, url):
        try:
            settings = {}

            with open('settings.json','r') as file:
                settings = json.load(file)

            res = requests.post('https://api.short.io/links', {
                  'domain': 'nvnls.ml',
                  'originalURL': url,
            }, headers = {
                  'authorization': settings["shortio"]
            }, json=True)

            res.raise_for_status()
            data = res.json()
            shorted_url = data["shortURL"]

            embed = discord.Embed(
                title="Your short URL:",
                description=shorted_url,
                color=0x75e8ee
            )

        except Exception as e:
            embed = make_error_embed(e)
        finally:
            return embed

def setup(client):
    client.add_cog(URLShort(client))
