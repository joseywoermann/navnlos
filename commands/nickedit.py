import discord
from discord.ext import commands
import logging

class NickEdit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def nickedit(self, ctx, mensch: discord.Member, newname):

        if newname:

            try:
                await mensch.edit(nick=newname)

            except:
                await ctx.reply("Nickname konnte nicht geändert werden.")

        else:
            pass


def setup(client):
    client.add_cog(NickEdit(client))
