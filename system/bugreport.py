import discord
from discord.ext import commands
import logging
import json
from github import Github
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option


options = [
    create_option(
        name="title",
        description="Set a short title.",
        option_type=3,
        required=True
    ),
    create_option(
        name="description",
        description="Explain what isn't working in more detail.",
        option_type=3,
        required=False
    )
]

class BugReport(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "bugreport",
        description = "Something isn't working? Create a bugreport!",
        options = options,
        #guild_ids = test_guilds
    )
    async def _bugreport(self, ctx: SlashContext, title, description = None):

        embed = BugReport.make(self, ctx, title, description)
        await ctx.send(embed = embed)


    def make(self, ctx, pTitle, pBody):
        settings = {}

        with open('settings.json','r') as file:
            settings = json.load(file)

        g = Github(settings["github"])
        repo = g.get_repo("joseywoermann/navnlos")

        if pBody:
            i = repo.create_issue(
                title=pTitle,
                body = pBody + " (Issue created by Discord-User `" + str(ctx.author) + "`)",
                assignee="joseywoermann",
            )
        else:
            i = repo.create_issue(
                title=pTitle,
                body = "(Issue created by Discord-user `" + str(ctx.author) + "`)",
                assignee="joseywoermann",
            )

        embed = discord.Embed(title = "Bugreport created!", description = "[All bugreports](https://github.com/joseywoermann/navnlos/issues)")
        logging.info(str(ctx.author) + " created an issue.")
        return embed


def setup(client):
    client.add_cog(BugReport(client))
