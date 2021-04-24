import discord
from discord.ext import commands
import logging

class NickEdit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def nickedit(self, ctx, mensch: discord.Member, *, newname):

        if newname:
            try:
                nickedit_embed = discord.Embed(
                    title = " ",
                    description = f"Changed nickname of {person.mention}.",
                    colour=discord.Color.dark_red()
                )
                nickedit_embed.set_footer(text = "$nickedit | @navnløs")

                await mensch.edit(nick=newname)
                await ctx.reply(embed = nickedit_embed)
            except:
                pass


def setup(client):
    client.add_cog(NickEdit(client))
