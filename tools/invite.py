import discord
from discord.ext import commands

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['inv'])
    @commands.guild_only()
    async def invite(self, ctx):

        invite = "https://nvnls.ml/add"

        invite_embed = discord.Embed(title="Get navnløs onto your server", url = invite, color=0x75e8ee)
        invite_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        invite_embed.set_footer(text = "$invite | @navnløs")

        await ctx.reply(content=None, embed=invite_embed)

def setup(client):
    client.add_cog(Invite(client))
