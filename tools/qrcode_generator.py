import discord
from discord.ext import commands
import qrcode
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "url",
        description = "Enter a URL",
        option_type = 3,
        required = True
    )
]

class QRcode(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "qrcode",
        description = "Generate a QR-code from a URL",
        options = options,
        #guild_ids = test_guilds
    )
    async def _qr(self, ctx: SlashContext, url):
        await QRcode.make(self, ctx, url)
        #await ctx.send(embed = embed)

    async def make(self, ctx, url):
        try:
            img = qrcode.make(url)
            img.save('qrcode.png')
            file = discord.File("qrcode.png", filename="qrcode.png")

            embed = discord.Embed(title="QR-code has been generated:", color=0x75e8ee)
            embed.set_image(url="attachment://qrcode.png")
            await ctx.send(file = file, embed=embed)

        except Exception as e:
            await ctx.send(embed = make_error_embed(e))


def setup(client):
    client.add_cog(QRcode(client))
