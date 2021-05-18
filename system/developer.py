import discord
from discord.ext import commands

class Developer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['dev'])
    async def developer(self, ctx):
        dev_embed = discord.Embed(
            description="[Twitter](https://twitter.com/joseywoermann/) - [Website](https://joseywoermann.ml/) - [GitHub](https://github.com/joseywoermann/)\n\n" +
            "[Discord](https://discord.gg/SchJckc) - [Reddit](https://reddit.com/u/joseywoermann/) - [Instagram](https://instagram.com/joseywoermann/)",
            colour=0x75e8ee
        )
        await ctx.reply(embed = dev_embed)


def setup(client):
    client.add_cog(Developer(client))
