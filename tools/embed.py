import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "title",
        description = "Set a title.",
        option_type = 3,
        required = False
    ),
    create_option(
        name = "description",
        description = "Set a description.",
        option_type = 3,
        required = False
    ),
    create_option(
        name = "author",
        description = "Set an author.",
        option_type = 3,
        required = False
    ),
    create_option(
        name = "thumbnail",
        description = "Set a thumbnail.",
        option_type = 3,
        required = False
    ),
    create_option(
        name = "image",
        description = "Set an image.",
        option_type = 3,
        required = False
    )
]

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "makeembed",
        description = "Create and embed.",
        options = options,
        #guild_ids = test_guilds
    )
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def _makeembed(
        self,
        ctx: SlashContext,
        title = discord.Embed.Empty,
        description = discord.Embed.Empty,
        author = discord.Embed.Empty,
        thumbnail = discord.Embed.Empty,
        image = discord.Embed.Empty
    ):
        embed = await Embed.make(self, ctx, title, description, author, thumbnail, image)
        await ctx.send(embed=embed)

    async def make(self, ctx, title, description, author, thumbnail, image):
        try:
            embed = discord.Embed(
                title = title,
                description = description
            )

            if author != discord.Embed.Empty:
                embed.set_author(name = author)
            embed.set_thumbnail(url = thumbnail)
            embed.set_image(url = image)

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Embed(client))
