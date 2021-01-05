import discord
from discord.ext import commands
import logging

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):

        invite = "https://discord.gg/KVbdvK8"

        invite_embed = discord.Embed(title="Invitelink zum MisteriCraft-Communityserver:\n" + str(invite), color=discord.Color.gold())
        invite_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(content=None, embed=invite_embed)

def setup(client):
    client.add_cog(Invite(client))
