import discord
from discord.ext import commands

import logging

class AddRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["ar"])
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def addrole(self, ctx, person: discord.Member, *, role):
        guild = ctx.message.guild
        roles = discord.utils.get(guild.roles, name=role)
        addrole_embed = discord.Embed(title="Rolle __" + str(roles) + "__ zu " + str(person) + " hinzugefuegt")
        addrole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)

        try:
            await person.add_roles(roles)
            await ctx.send(content=None, embed=addrole_embed)
        except:
            return


def setup(client):
    client.add_cog(AddRole(client))
