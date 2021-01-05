import discord
from discord.ext import commands
import logging
from time import sleep

class On_message(commands.Cog):

    def __init__(self, client):
        self.client = client




    async def publisher(message):
        sleep(10)
        await message.publish()

    @commands.Cog.listener()
    async def on_message(self, message):

        server = message.guild

        if message.channel.id == 654347445517549578:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 656591472124231761:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 737715494198706286:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 741033879032430834:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 720674929540071564:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 724946319818489946:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 685080746410639411:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 700345472300089366:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 739033895365771334:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 738838305722073221:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 738844667084406814:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        elif message.channel.id == 738840347656060968:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        # testchannel
        elif message.channel.id == 795018273632682014:
            """
            publisher_thread = threading.Thread(target=publisher, args=(message))
            publisher_thread.start()
            """
            await On_message.publisher(message)

        """
        if client.user.mentioned_in(message):
            await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")
        """
        if message.content.lower() == "hello":
            await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")

        if message.content.lower() == "hallo":
            await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")

        else:
            pass
        """
        with open('./assets/banned_words.txt') as myfile:
            if message.content.lower() in myfile.read():
                await message.channel.purge(limit=1)
                await message.channel.send("Dieses Wort ist auf diesem Server verboten.")
        """
        #await self.client.process_commands(message)


def setup(client):
    client.add_cog(On_message(client))
