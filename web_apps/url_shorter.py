import discord
from discord.ext import commands
import requests
import json

class URLShort(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['shorturl'])
    @commands.guild_only()
    async def short(self, ctx, long_url):

        async with ctx.channel.typing():
            settings = {}

            with open('settings.json','r') as file:
                settings = json.load(file)

            res = requests.post('https://api.short.io/links', {
                  'domain': 'nvnls.ml',
                  'originalURL': long_url,
            }, headers = {
                  'authorization': settings["shortio"]
            }, json=True)

            res.raise_for_status()
            data = res.json()

            #print(data)
            shorted_url = data["shortURL"]

            short_embed = discord.Embed(title="Your short URL:", description=shorted_url, color=0x75e8ee)
            await ctx.reply(content=None, embed=short_embed)

def setup(client):
    client.add_cog(URLShort(client))
