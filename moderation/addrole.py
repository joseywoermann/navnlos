import discord
from discord.ext import commands

class AddRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["ar"])
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def addrole(self, ctx, person: discord.Member, *, role_name):

        guild = ctx.message.guild
        role = discord.utils.get(guild.roles, name=role_name)
        
        addrole_embed = discord.Embed(
            title=" ",
            description=f"The role {role.mention} has been added from {person.mention}",
            color=discord.Color.dark_red()
        )
        addrole_embed.set_footer(text = "$addrole | @navnløs")

        try:
            await person.add_roles(role)
            await ctx.reply(content=None, embed=addrole_embed)
        except:
            print("error")


def setup(client):
    client.add_cog(AddRole(client))
