import discord
from discord.ext import commands
import logging

class RemoveRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["rr"])
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def removerole(self, ctx, person: discord.Member, *, role):

        guild = ctx.message.guild
        roles = discord.utils.get(guild.roles, name=role)
        removerole_embed = discord.Embed(title="Rolle __" + str(roles) + "__ von " + str(person) + " entfernt")
        removerole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        try:
            await person.remove_roles(roles)
            await ctx.reply(content=None, embed=removerole_embed)
        except:
            return


def setup(client):
    client.add_cog(RemoveRole(client))
