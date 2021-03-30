# Preset am Beispiel $ping
import discord
from discord.ext import commands
import logging
import random

class Question(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['q', 'ask'])
    @commands.guild_only()
    async def question(self, ctx, *, question):

        response = ['Yes', 'No', 'Maybe', 'Likely', 'Probably not']
        response_embed = discord.Embed(title=str(random.choice(response)), color=0x75e8ee)
        response_embed.set_footer(text = "$question | @navnløs")
        await ctx.reply(content=None, embed=response_embed)

def setup(client):
    client.add_cog(Question(client))
