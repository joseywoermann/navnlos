"""
import discord
from discord.ext import commands
from time import sleep

class BanID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def banid(self, ctx, user_id, *, reason=None):
        user = await self.client.fetch_user(user_id)

        ban_embed = discord.Embed(
            title="Banned the following user:",
            description = f"{user.mention}",
            color=discord.Color.dark_red()
        )
        ban_embed.set_footer(text = "$banid | @navnløs")

        ban_error_embed = discord.Embed(title="User couldn't be banned.", color=discord.Color.dark_purple())

        user = await self.client.fetch_user(user_id)

        try:
            await ctx.guild.ban(user, reason=f"{reason} | banned by {ctx.author}")
            await ctx.reply(content=None, embed=ban_embed)

        except:
            await ctx.reply(content=None, embed=ban_error_embed)
            sleep(5)


def setup(client):
    client.add_cog(BanID(client))
"""


import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option


options = [
    create_option(
        name = "id",
        description = "Who do you want to ban?",
        option_type = 3,
        required = True
    ),
    create_option(
        name = "reason",
        description = "Why do you want to ban this member?",
        option_type = 3,
        required = False
    )
]

class BanID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def banid(self, ctx, id, *, reason=None):
        embed = await BanID.make(self, ctx, id, reason)
        await ctx.send(embed = embed)


    @cog_ext.cog_slash(name = "banid", description = "Bans a member by ID", options = options, guild_ids = test_guilds)
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def _banid(self, ctx: SlashContext, id, reason = None):
        embed = await BanID.make(self, ctx, id, reason)
        await ctx.send(embed = embed)


    async def make(self, ctx, user_id, reason):
        try:
            user = await self.client.fetch_user(int(user_id))
            embed = discord.Embed(
                title="Banned the following user:",
                description = f"{user.mention}",
                color=discord.Color.dark_red()
            )
            embed.set_footer(text = "$ban | @navnløs")
            await user.ban(reason=f"{reason} | banned by {ctx.author}")

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(BanID(client))
