import discord
from discord.ext import commands
import logging

class RemoveRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["rr"])
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def removerole(self, ctx, person: discord.Member, *, role_name):

        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name=role_name)
        removerole_embed = discord.Embed(
            title=" ",
            description=f"The role {role.mention} has been removed from {person.mention}",
            color=discord.Color.dark_red()
        )
        removerole_embed.set_footer(text = "$removerole | @navnløs")

        try:
            await person.remove_roles(role)
            await ctx.reply(content=None, embed=removerole_embed)
        except:
            print("error")


def setup(client):
    client.add_cog(RemoveRole(client))
