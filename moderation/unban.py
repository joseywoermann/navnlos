import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "user",
        description = "Enter the user you want to unban. Example: jcw05#1331",
        option_type = 3,
        required = True
    )
]

class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "unban",
        description = "Remove the ban from a user.",
        options = options,
        #guild_ids = test_guilds
    )
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def _unban(self, ctx: SlashContext, user):
        embed = await Unban.make(self, ctx, user)
        await ctx.send(embed=embed)


    async def make(self, ctx, user):
        try:
            embed = discord.Embed(
                title=f"Removed ban from {user}.",
                color=discord.Color.dark_red()
            )
            banned_users = await ctx.guild.bans()
            user_name, user_discriminator = user.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (user_name, user_discriminator):
                    await ctx.guild.unban(user)

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Unban(client))
