import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed, config
from discord_slash.utils.manage_commands import create_option
import json
import os
from statcord import StatcordClient


class MyStatcordCog(commands.Cog):
    def __init__(self, client):

        self.client = client
        self.statcord_client = StatcordClient(
                client,
                str(config["STATCORD_TOKEN"]),
                self.custom_graph_1
            )

    def cog_unload(self):
        self.statcord_client.close()

    async def custom_graph_1(self):
        return 1 + 2 + 3


def setup(client):
    client.add_cog(MyStatcordCog(client))
