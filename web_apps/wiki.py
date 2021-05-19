from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "topic",
        description = "Enter a topic, name etc.",
        option_type = 3,
        required = True
    )
]

class Wiki(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "wikipedia",
        description = "Use this as a shortcut to get to the Wikipedia article.",
        options = options,
        guild_ids = test_guilds
    )
    async def _wikipedia(self, ctx: SlashContext, topic):

        while ' ' in topic:
            topic = topic.replace(' ', '+')

        await ctx.send("https://wikipedia.org/w/index.php?search=" + topic)

def setup(client):
    client.add_cog(Wiki(client))
