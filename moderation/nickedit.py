import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "member",
        description = "Whose nickname do you want to change?",
        option_type = 6,
        required = True
    ),
    create_option(
        name = "newname",
        description = "What should the new nickname be?",
        option_type = 3,
        required = True
    )
]

class ChangeNickname(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "change-nickname",
        description = "Change a member's nickname.",
        options = options,
        guild_ids = test_guilds
    )
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def _changenickname(self, ctx: SlashContext, member: discord.Member, newname):
        embed = await ChangeNickname.make(self, ctx, member, newname)
        await ctx.send(embed = embed)

    async def make(self, ctx, member: discord.Member, newname):

        try:
            embed = discord.Embed(
                title = discord.Embed.Empty,
                description = f"**Changed nickname of {member.mention} to {newname}**.", # TODO: improve design
                colour=discord.Color.dark_red()
            )
            await member.edit(nick=newname)


        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed


def setup(client):
    client.add_cog(ChangeNickname(client))
