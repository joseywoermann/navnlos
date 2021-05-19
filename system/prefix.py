import discord
from discord.ext import commands

class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content.lower() == "<@707269223281459271>":
            prefix_embed = discord.Embed(title = "Use me with Slash-Commands! `/ping`", color=0x75e8ee)
            await message.reply(embed = prefix_embed)

        elif message.content.lower() == "<@!707269223281459271>":
            prefix_embed = discord.Embed(title = "Use me with Slash-Commands! `/ping`", color=0x75e8ee)
            await message.reply(embed = prefix_embed)
        else:
            pass

def setup(client):
    client.add_cog(Prefix(client))
