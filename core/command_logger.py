import discord
from discord.ext import commands
import logging
from time import sleep

class CommandLogger(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        server = message.guild

        if message.content.startswith("$"):

            if server.id == 304191437652623360:

                log_channel = self.client.get_channel(751879355344617582)

                log_embed = discord.Embed(title=message.content, description="Channel: **{0.channel.name}** Channel-ID: [{0.channel.id}]".format(message))
                log_embed.set_author(name="User: " + message.author.name + "#" + str(message.author.discriminator) + " ID: " + str(message.author.id), icon_url=message.author.avatar_url)
                log_embed.set_footer(text=message.created_at.strftime("%Y; %m. %d., %H:%M:%S") + " Server: " + str(message.channel.guild) + " / " + str(message.guild.id))

                await log_channel.send(content=None, embed=log_embed)

            else:

                log_channel = self.client.get_channel(751879443810615487)

                log_embed = discord.Embed(title=message.content, description=" Channel: **{0.channel.name}** Channel-ID: [{0.channel.id}]".format(message))
                log_embed.set_author(name="User: " + message.author.name + "#" + str(message.author.discriminator) + " ID: " + str(message.author.id), icon_url=message.author.avatar_url)
                log_embed.set_footer(text=message.created_at.strftime("%Y; %m. %d., %H:%M:%S") + " Server: " + str(message.channel.guild) + " / " + str(message.guild.id))

                await log_channel.send(content=None, embed=log_embed)



def setup(client):
    client.add_cog(CommandLogger(client))
