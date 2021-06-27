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


class AnimalFact(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_subcommand(
        base="animal",
        name="fact",
        options=options,
        #guild_ids=test_guilds
    )
    async def animal_AnimalPhoto(self, ctx: SlashContext, species):
        embed = await AnimalFact.make(self, ctx, species)
        await ctx.send(embed=embed)

    async def make(self, ctx, species):
        try:

            res = requests.get(f"https://some-random-api.ml/facts/{species}")
            data = res.json()

            embed = discord.Embed(
                title="Did you know that...",
                description=data["fact"],
                color=0x75e8ee
            )
            embed.set_footer(text="data provided by some-random-api.ml")

        except Exception as e:
            embed = make_error_embed(e)
        finally:
            return embed


def setup(client):
    client.add_cog(AnimalFact(client))
