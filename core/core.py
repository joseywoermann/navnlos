import discord
from discord.ext import commands
import logging

class Core(commands.Cog):

    def __init__(self, client):
        self.client = client
    """
    @commands.Cog.listener()
    """


def setup(client):
    client.add_cog(Core(client))
