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

class ChnageNickname(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def changenickname(self, ctx, member: discord.Member, *, newname):
        embed = await ChnageNickname.make(self, ctx, member, newname)
        await ctx.reply(embed = embed)

    @cog_ext.cog_slash(name = "change-nickname", description = "Change a member's nickname.", options = options, guild_ids = test_guilds)
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def _changenickname(self, ctx: SlashContext, member: discord.Member, newname):
        embed = await ChnageNickname.make(self, ctx, member, newname)
        await ctx.send(embed = embed)

    async def make(self, ctx, member: discord.Member, newname):

        try:
            embed = discord.Embed(
                title = discord.Embed.Empty,
                description = discord.Embed.Empty,
                colour=discord.Color.dark_red()
            )
            embed.set_footer(text = "$nickedit | @navnløs")
            embed.set_author(name = f"Changed nickname of {member} to {newname}.")

            await member.edit(nick=newname)


        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed


def setup(client):
    client.add_cog(ChnageNickname(client))
