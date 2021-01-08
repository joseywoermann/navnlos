import discord
from discord.ext import commands, tasks
#from discord.ext import tasks
import logging
from itertools import cycle
import os
import os.path



logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d; %H:%M:%S', level=logging.INFO)

intents = discord.Intents.all()
TOKEN = 'YOUR TOKEN HERE'

client = commands.Bot(command_prefix='$', intents = intents)
client.remove_command('help')

statusmessages = ['navnlos.tk', '$help']
statusmsg = cycle(statusmessages)



@client.event
async def on_ready():
    change_status.start()
    logging.info("Bot is online.")

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(statusmsg)))



# command to MANUALLY load a specific command / event (extension is a command / an event)
@client.command()
@commands.is_owner()
async def load(ctx, extension):

    if os.path.isfile(f"commands/{extension}.py"):
        client.load_extension(f"commands.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"events/{extension}.py"):
        client.load_extension(f"events.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"core/{extension}.py"):
        client.load_extension(f"core.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")



# command to MANUALLY unload a specific command / event (extension is a command / an event)
@client.command()
@commands.is_owner()
async def unload(ctx, extension):

    if os.path.isfile(f"commands/{extension}.py"):
        client.unload_extension(f"commands.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"events/{extension}.py"):
        client.unload_extension(f"events.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"core/{extension}.py"):
        client.unload_extension(f"core.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")



# command to MANUALLY reload a specific command / event (extension is a command / an event)
@client.command()
@commands.is_owner()
async def reload(ctx, extension):

    if os.path.isfile(f"commands/{extension}.py"):
        client.unload_extension(f"commands.{extension}")
        client.load_extension(f"commands.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"events/{extension}.py"):
        client.unload_extension(f"events.{extension}")
        client.load_extension(f"events.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"core/{extension}.py"):
        client.unload_extension(f"core.{extension}")
        client.load_extension(f"core.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")



# function that AUTOMATICYLLY loads all extensions
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        client.load_extension(f"commands.{filename[:-3]}")

for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        client.load_extension(f"events.{filename[:-3]}")

for filename in os.listdir("./core"):
    if filename.endswith(".py"):
        client.load_extension(f"core.{filename[:-3]}")

for filename in os.listdir("./kgh_notifier"):
    if filename.endswith(".py"):
        client.load_extension(f"kgh_notifier.{filename[:-3]}")

client.run(TOKEN)
