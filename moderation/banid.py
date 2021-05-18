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
            await ctx.guild.ban(user, reason=f"{reason} | banned by {ctx.author}")

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(BanID(client))
