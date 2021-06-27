import discord
from discord.ext import commands
import requests
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option, create_choice

options = [
    create_option(
        name="species",
        description="Select a species.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="cat",
                value="cat"
            ),
            create_choice(
                name="dog",
                value="dog"
            ),
            create_choice(
                name="red panda",
                value="red panda"
            ),
            create_choice(
                name="panda",
                value="panda"
            ),
            create_choice(
                name="koala",
                value="koala"
            )
        ]
    )
]


class AnimalPhoto(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_subcommand(
        base="animal",
        name="photo",
        options=options,
        #guild_ids=test_guilds
    )
    async def animal_AnimalPhoto(self, ctx: SlashContext, species):
        embed = await AnimalPhoto.make(self, ctx, species)
        await ctx.send(embed=embed)

    async def make(self, ctx, species):
        try:
            if species == "cat":
                url = "https://api.thecatapi.com/v1/images/search"

            if species == "dog":
                url = "https://dog.ceo/api/breeds/image/random"

            if species == "red panda":
                url = "https://some-random-api.ml/img/red_panda"

            if species == "panda":
                url = "https://some-random-api.ml/img/panda"

            if species == "koala":
                url = "https://some-random-api.ml/img/koala"

            res = requests.get(url)
            data = res.json()

            embed = discord.Embed(
                title="Here you go!",
                color=0x75e8ee
            )

            if species == "cat":
                embed.set_image(url=data[0]["url"])

            if species == "dog":
                embed.set_image(url=data["message"])

            if species == "red panda":
                embed.set_image(url=data["link"])

            if species == "panda":
                embed.set_image(url=data["link"])

            if species == "koala":
                embed.set_image(url=data["link"])

            embed.set_footer(text="images provided by some-random-api.ml")

        except Exception as e:
            embed = make_error_embed(e)
        finally:
            return embed


def setup(client):
    client.add_cog(AnimalPhoto(client))
