import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "member",
        description = "Which member do you want to remove the role from?",
        option_type = 6,
        required = True
    ),
    create_option(
        name = "role",
        description = "Which role do you want to remove?",
        option_type = 8,
        required = True
    )

]
class RemoveRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "removerole",
        description = "Remove a role from a member",
        options = options,
        #guild_ids = test_guilds
    )
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def _removerole(self, ctx: SlashContext, member, role):
        embed = await RemoveRole.make(self, ctx, member, role)
        await ctx.send(embed = embed)


    async def make(self, ctx, member: discord.Member, pRole: discord.Role):
        try:
            guild = ctx.guild

            embed = discord.Embed(
                title=" ",
                description=f"The role {pRole.mention} has been removed from {member.mention}",
                color=discord.Color.dark_red()
            )
            await member.remove_roles(pRole)

        except Exception as e:
            embed = await make_error_embed(e)
        finally:
            return embed


def setup(client):
    client.add_cog(RemoveRole(client))
