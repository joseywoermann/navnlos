from discord.ext import commands
from time import sleep

class AutoPublisher(commands.Cog):

    def __init__(self, client):
        self.client = client


    async def publisher(message):
        sleep(1)
        await message.publish()

    @commands.Cog.listener()
    async def on_message(self, message):

        target_channels = [654347445517549578, 737715494198706286, 741033879032430834, 720674929540071564, 724946319818489946, 685080746410639411, 700345472300089366,739033895365771334, 738838305722073221, 738844667084406814, 738840347656060968]

        if message.channel.id in target_channels:
            await AutoPublisher.publisher(message)


def setup(client):
    client.add_cog(AutoPublisher(client))
