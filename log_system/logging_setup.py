import discord
from discord.ext import commands
import logging
from asyncio import sleep

class LoggingSetup(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log_server = self.client.get_guild(737650747432501308)

        channel = discord.utils.get(
            log_server.text_channels,
            name=str(guild.id)
        )

        category = discord.utils.get(
            log_server.categories,
            id = 744643860264910928
        )

        if channel is None:
            channel = await category.create_text_channel(
                str(guild.id),
                reason = f"Log-Channel for \"{guild.name}\"."
            )
            await channel.send(f"This is now the logging-channel for \"{guild.name}\".")


def setup(client):
    client.add_cog(LoggingSetup(client))
