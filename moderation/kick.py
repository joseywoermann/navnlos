import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "member",
        description = "Who do you want to kick?",
        option_type = 6,
        required = True
    ),
    create_option(
        name = "reason",
        description = "Why do you want to kick this member?",
        option_type = 3,
        required = False
    )
]

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name = "kick", description = "Kick a member", options = options, guild_ids = test_guilds)
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def _kick(self, ctx: SlashContext, member: discord.Member, reason = None):
        embed = await Kick.make(self, ctx, member, reason)
        await ctx.send(embed = embed)


    async def make(self, ctx, member, reason):
        try:
            embed = discord.Embed(
                title = "Kicked the following user:",
                description = f"{member.mention}",
                colour=discord.Color.dark_red()
            )
            await member.kick(reason=f"{reason} | kicked by {ctx.author}")

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Kick(client))
