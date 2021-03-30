import discord
from discord.ext import commands
import logging
from time import sleep

class NSFW_filter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        with open('assets/nsfw_words.txt') as file:
            nsfw_words = file.read().splitlines()
            if any(word in message.content.lower() for word in nsfw_words):
                await message.delete()
                await message.channel.send("Your message has been deleted because it contained banned words.")

def setup(client):
    client.add_cog(NSFW_filter(client))
