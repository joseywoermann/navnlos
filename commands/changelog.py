# Preset am Beispiel $ping
import discord
from discord.ext import commands
import logging

class Changelog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def changelog(self, ctx):

        changelog_embed = discord.Embed(title="Changelog for version 1.6.1", color=discord.Color.lighter_grey())
        changelog_embed.add_field(name="Commands:", value="Aliases entfernt um Bug zu fixen")
        changelog_embed.add_field(name="Commands:", value="$developer hinzugefügt")
        changelog_embed.add_field(name="Allgemein:", value="Bugfixes")

        changelog_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=changelog_embed)

def setup(client):
    client.add_cog(Changelog(client))
