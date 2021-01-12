# Preset am Beispiel $ping
import discord
from discord.ext import commands
import logging
import random

class Question(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def question(self, ctx, *, question):

        response = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Wahrscheinlich nicht']
        response_embed = discord.Embed(title="Deine Frage: \"" + str(question) + "\" Die Antwort: " + str(random.choice(response)), color=discord.Color.gold())
        response_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.reply(content=None, embed=response_embed)

def setup(client):
    client.add_cog(Question(client))
