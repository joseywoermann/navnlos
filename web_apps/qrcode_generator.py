import discord
from discord.ext import commands
import logging
import qrcode


class URLShort(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['qrcode', 'makeqrcode'])
    @commands.guild_only()
    async def qr(self, ctx, *, url):

        async with ctx.channel.typing():
            img = qrcode.make(url)
            img.save('qrcode.png')
            file = discord.File("qrcode.png", filename="qrcode.png")

            qrcode_embed = discord.Embed(title="QR-code has been generated:", color=0x75e8ee)
            qrcode_embed.set_image(url="attachment://qrcode.png")
            await ctx.reply(file = file, embed=qrcode_embed)

def setup(client):
    client.add_cog(URLShort(client))
