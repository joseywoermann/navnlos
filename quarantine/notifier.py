import discord
from discord.ext import commands, tasks
import logging

from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime
import threading
import asyncio

class Notifier(commands.Cog):

    def __init__(self, client):
        self.client = client


    @tasks.loop(seconds=60)
    async def kgh_notifier(self):

        logging.info("KGH-Notifier active")


        URL = "http://kreisgymnasium-halle.de/"
        refresh_time = 60 #How often the notifier should check whether or not something has changed in seconds.

        page = requests.get(URL)
        old_page = BeautifulSoup(page.content, 'html.parser')
        old_content = old_page.find('div', attrs={'class': 'repositories'})

        await asyncio.sleep(refresh_time)

        page = requests.get(URL)
        new_page = BeautifulSoup(page.content, 'html.parser')
        new_content = new_page.find('div', attrs={'class': 'repositories'})

        if old_content == new_content:
            logging.info("KGH-Notifier: Nothing changed")
            #return 0

        else:
            logging.warning("KGH-Notifier: Something changed")
            jcw05 = self.client.get_user(586206645592391711)
            await jcw05.send("KGH-Notifier: Something changed (http://kreisgymnasium-halle.de/)")


            #channel = self.client.get_channel(797388212199882782)
            #await channel.send("<@&797387882204758027>, ein neuer Artikel wurde veröffentlicht. http://kreisgymnasium-halle.de/")


    kgh_notifier.start()



def setup(client):
    client.add_cog(Notifier(client))
