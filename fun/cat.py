import discord
from discord.ext import commands
import requests
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option, create_choice

options = [
    create_option(
        name = "species ",
        description = "Select a species.",
        option_type = 3,
        required = True,
        choices = [
            create_choice(
                name = "cat",
                value = "cat"
            ),
            create_choice(
                name = "dog",
                value = "dog"
            )
        ]
    )
]

class Animal(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "animal-photo",
        description = "Get a random animal picture.",
        options = options,
        #guild_ids = test_guilds
    )
    async def _photo(self, ctx: SlashContext, species):
        embed = await Animal.make(self, ctx, species)
        await ctx.send(content=None, embed=embed)


    async def make(self, ctx, species):
        try:
            if species == "cat":
                url = "https://api.thecatapi.com/v1/images/search"
            if species == "dog":
                url = "https://dog.ceo/api/breeds/image/random"

            res = requests.get(url)
            data = res.json()

            embed = discord.Embed(
                title="Here you go!",
                color=0x75e8ee
            )
            if species == "cat":
                embed.set_image(url = data[0]["url"])
            if species == "dog":
                embed.set_image(url = data["message"])
        

        except Exception as e:
            embed = make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Animal(client))
