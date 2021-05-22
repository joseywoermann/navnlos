from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "product",
        description = "Enter a product name.",
        option_type = 3,
        required = True
    )
]

class Price(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "price",
        description = "Use this as a shortcut to get current prices of a product.",
        options = options,
        #guild_ids = test_guilds
    )
    async def _price(self, ctx: SlashContext, product):

        while ' ' in product:
            product = product.replace(' ', '+')

        await ctx.send("https://geizhals.eu/?fs=" + product)

def setup(client):
    client.add_cog(Price(client))
