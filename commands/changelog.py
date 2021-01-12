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

        changelog_embed = discord.Embed(title="Changelog for version 2.0.2", color=discord.Color.lighter_grey())
        changelog_embed.add_field(name="Allgemein:", value="Kritische Sicherheitslücke geschlossen")
        changelog_embed.add_field(name="Allgemein:", value="discord.py auf Version 1.6.0 geupdated")

        changelog_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.reply(embed=changelog_embed)

def setup(client):
    client.add_cog(Changelog(client))
