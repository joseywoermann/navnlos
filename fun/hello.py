import discord
from discord.ext import commands
import logging
from time import sleep
import random

class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        words = ["hello", "hallo", "hi", "hey"]

        if message.content.lower() in words:
            number = random.randint(0, 5)

            if number == 5:
                await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")
                
def setup(client):
    client.add_cog(Hello(client))
