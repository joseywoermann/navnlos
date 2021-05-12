import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

direct_options = [
    create_option(
        name = "message",
        description = "What do you want to send?",
        option_type = 3,
        required = True
    )
]

global_options = [
    create_option(
        name = "server-id",
        description = "Which server do you want to send the message to?",
        option_type = 4
        required = True
    ),
    create_option(
        name = "channel-id",
        description = "Whhich channel do you want to send the message to?",
        option_type = 4
        required = True
    ).
    create_option(
        name = "message",
        description = "What do you want to send?",
        option_type = 3,
        required = True
    )
]

class BotChat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def sendto(self, ctx, server, channel, *, text):
        target = self.client.get_guild(int(server)).get_channel(int(channel))
        await target.send(str(text))



    @commands.command()
    @commands.is_owner()
    async def sendhere(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(str(text))

def setup(client):
    client.add_cog(BotChat(client))
