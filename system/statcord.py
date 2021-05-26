"""
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option
import statcord
import json

class StatcordPost(commands.Cog):
    def __init__(self, client):

        settings = {}

        with open('settings.json','r') as file:
            settings = json.load(file)

        self.client = client
        self.key = settings["statcordkey"]
        self.api = statcord.Client(self.client,self.key)
        self.api.start_loop()


    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        self.api.command_run(ctx)


def setup(client):
    client.add_cog(StatcordPost(client))
"""

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option
import json
from statcord import StatcordClient


class MyStatcordCog(commands.Cog):
    def __init__(self, client):

        settings = {}

        with open('settings.json','r') as file:
            settings = json.load(file)
            
        self.client = client
        self.statcord_client = StatcordClient(client, str(settings["statcordkey"]), self.custom_graph_1)

    def cog_unload(self):
        self.statcord_client.close()

    async def custom_graph_1(self):
        return 1 + 2 + 3


def setup(client):
    client.add_cog(MyStatcordCog(client))
