import discord
from discord.ext import commands
import logging

class Developer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def developer(self, ctx):
        dev_embed = discord.Embed(description="[Twitter](https://twitter.com/joseywoermann/) - [Website](http://joseywoermann.tk/) - [GitHub](https://github.com/joseywoermann/)\n\n[Discord](https://discord.gg/SchJckc) - [Reddit](https://reddit.com/u/joseywoermann/) - [](https://github.com/joseywoermann/)", colour=discord.Colour.dark_grey())
        """
        dev_embed.add_field(name = "Twitter", value = "[Click here](https://twitter.com/joseywoermann/)")
        dev_embed.add_field(name = "Instagram", value = "[Click here](https://instagram.com/joseywoermann/)")
        """
        dev_embed.set_author(name=ctx.message.author,icon_url=ctx.author.avatar_url)
        await ctx.send(embed = dev_embed)


def setup(client):
    client.add_cog(Developer(client))
