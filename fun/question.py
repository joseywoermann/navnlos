import discord
from discord.ext import commands
import random
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option


options = [
    create_option(
        name = "question",
        description = "Your question",
        option_type = 3,
        required = True
    )
]

class Question(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name = "question", description = "navnløs can answer your Yes/No questions.", options = options, guild_ids = test_guilds)
    async def _question(self, ctx: SlashContext, *, question):
        embed = Question.make(self, ctx, question)
        await ctx.send(embed = embed)

    def make(self, ctx, question):
        response = ['Yes', 'No', 'Maybe', 'Likely', 'Probably not']
        embed = discord.Embed(title=str(random.choice(response)), color=0x75e8ee)
        embed.set_footer(text = "$question | @navnløs")
        return embed

def setup(client):
    client.add_cog(Question(client))
