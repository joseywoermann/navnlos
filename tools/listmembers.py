import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "role",
        description = "Select a role.",
        option_type = 8,
        required = True
    )
]

class HasRole(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name = "hasrole", description = "List all members with this role", options = options, guild_ids = test_guilds)
    async def _hasrole(self, ctx: SlashContext, role):
        embed = await HasRole.make(self, ctx, role)
        await ctx.send(embed = embed)


    async def make(self, ctx, role):
        try:
            server = ctx.guild
            members = []
            for member in server.members:
                if role in member.roles:
                    members.append('{}'.format(member.mention))
            if int(len(members)) > 75:
                embed = discord.Embed(title = "Users with this role:", description = "Too many members to display.")
            else:
                embed = discord.Embed(title = "Users with this role:", description = ',\n'.join(members))

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(HasRole(client))
