import discord
from discord.ext import commands
import logging

from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime

class Notifier(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("KGH-Notifier active")

        URL = "http://kreisgymnasium-halle.de/"
        refresh_time = 5 #How often the notifier should check whether or not something has changed in seconds.

        while True:

            page = requests.get(URL)
            old_page = BeautifulSoup(page.content, 'html.parser')
            old_content = old_page.find('div', attrs={'class': 'site-main'})

            sleep(refresh_time)

            page = requests.get(URL)
            new_page = BeautifulSoup(page.content, 'html.parser')
            new_content = new_page.find('div', attrs={'class': 'site-main'})

            if old_content == new_content:
                logging.info("KGH-Notifier: Nothing changed")

            else:
                logging.warning("KGH-Notifier: Something changed")
                jcw05 = self.client.get_user(586206645592391711)
                await jcw05.send("KGH-Notifier: Something changed (http://kreisgymnasium-halle.de/)")



def setup(client):
    client.add_cog(Notifier(client))
