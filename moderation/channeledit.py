from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds
from discord_slash.utils.manage_commands import create_option


options = [
    create_option(
        name = "name",
        description = "Enter the new name",
        option_type = 3,
        required = True
    )
]

class ChannelEdit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def channeledit(self, ctx, *, new_name):
        embed = await ChannelEdit.make(self, ctx, new_name)
        await ctx.send(embed = embed)


    @cog_ext.cog_slash(name = "channeledit", description = "Change the name of this channel", options = options, guild_ids = test_guilds)
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def _channeledit(self, ctx: SlashContext, name):
        embed = await ChannelEdit.make(self, ctx, name)
        await ctx.send(embed = embed)


    async def make(self, ctx, new_name):
        try:
            await ctx.channel.edit(name=new_name)
            embed = discord.Embed(title = "Channel name updated!")

        except Exception as e:
            embed = await make_error_embed(e)
            return embed


def setup(client):
    client.add_cog(ChannelEdit(client))
