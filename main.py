import discord
from discord.ext import commands, tasks
import logging
from itertools import cycle
import os
import os.path
import json
from discord_slash import SlashCommand
import random
import sentry_sdk

settings = {}

with open('settings.json','r') as file:
    settings = json.load(file)

# Sentry-stuff
sentry_sdk.init(
    settings["sentry_url"],
    traces_sample_rate=1.0
)

# CONFIGURATION
logging.basicConfig(
    format='%(asctime)s: %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d; %H:%M:%S',
    level=logging.INFO
)

intents = discord.Intents.all()



test_guilds = settings["test_guilds"]

client = commands.Bot(command_prefix=settings["prefix"], intents = intents)
client.remove_command('help')
slash = SlashCommand(client, sync_commands = True)

statusmessages = ['navnlos.ml', '$help', 'nvnls.ml/support', '$info']
statusmsg = cycle(statusmessages)

""" a universal embed used in all try...except blocks"""

error_msgs = [
    "Something really bad happened!",
    "That shouldn't have happened",
    "So you've caused an error...",
    "That didn't go so well..."
]

async def make_error_embed(exception):
    embed = discord.Embed(
        title = str(random.choice(error_msgs)),
        description = f"```\n{exception}```",
        color = discord.Color.red()
    )
    return embed
# END OF CONFIGURATION STUFF

@client.event
async def on_ready():
    change_status.start()
    logging.info("Bot is online.")

@tasks.loop(seconds=20)
async def change_status():

    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=next(statusmsg)
        )
    )

"""
@client.command()
@commands.is_owner()
async def load(ctx, extension):

    try:
        client.load_extension(extension)
        await ctx.reply(f"Extension `{str(extension)}` loaded")
    except Exception as e:
        await ctx.reply(f"```{e}```")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):

    try:
        client.unload_extension(extension)
        await ctx.reply(f"Extension `{str(extension)}` unloaded")
    except Exception as e:
        await ctx.reply(f"```{e}```")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):

    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        await ctx.reply(f"Extension `{str(extension)}` reloaded")
    except Exception as e:
        await ctx.reply(f"```{e}```")
"""

# load all cogs
for filename in os.listdir("./auto_publisher"):
    if filename.endswith(".py"):
        client.load_extension(f"auto_publisher.{filename[:-3]}")

for filename in os.listdir("./fun"):
    if filename.endswith(".py"):
        client.load_extension(f"fun.{filename[:-3]}")

for filename in os.listdir("./help"):
    if filename.endswith(".py"):
        client.load_extension(f"help.{filename[:-3]}")

for filename in os.listdir("./member_actions"):
    if filename.endswith(".py"):
        client.load_extension(f"member_actions.{filename[:-3]}")

for filename in os.listdir("./moderation"):
    if filename.endswith(".py"):
        client.load_extension(f"moderation.{filename[:-3]}")

for filename in os.listdir("./role_menu"):
    if filename.endswith(".py"):
        client.load_extension(f"role_menu.{filename[:-3]}")

for filename in os.listdir("./system"):
    if filename.endswith(".py"):
        client.load_extension(f"system.{filename[:-3]}")

for filename in os.listdir("./tools"):
    if filename.endswith(".py"):
        client.load_extension(f"tools.{filename[:-3]}")

for filename in os.listdir("./web_apps"):
    if filename.endswith(".py"):
        client.load_extension(f"web_apps.{filename[:-3]}")
"""
for filename in os.listdir("./filter"):
    if filename.endswith(".py"):
        client.load_extension(f"filter.{filename[:-3]}")
"""
for filename in os.listdir("./vc_role"):
    if filename.endswith(".py"):
        client.load_extension(f"vc_role.{filename[:-3]}")

for filename in os.listdir("./log_system"):
    if filename.endswith(".py"):
        client.load_extension(f"log_system.{filename[:-3]}")

if __name__ == "__main__":
    client.run(settings["discord"])
