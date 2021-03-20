import discord
from discord.ext import commands, tasks
import logging
from itertools import cycle
import os
import os.path



logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d; %H:%M:%S', level=logging.INFO)

intents = discord.Intents.all()

with open('bot.TOKEN','r') as file:
    TOKEN = file.read()



client = commands.Bot(command_prefix='-', intents = intents)
client.remove_command('help')

statusmessages = ['navnlos.ml', '$help', 'discord.gg/52TbNHPBU9']
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

    if os.path.isfile(f"auto_publisher/{extension}.py"):
        client.load_extension(f"auto_publisher.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"fun/{extension}.py"):
        client.load_extension(f"fun.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"help/{extension}.py"):
        client.load_extension(f"help.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"member_actions/{extension}.py"):
        client.load_extension(f"member_actions.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"moderation/{extension}.py"):
        client.load_extension(f"moderation.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"role_menu/{extension}.py"):
        client.load_extension(f"role_menu.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"system/{extension}.py"):
        client.load_extension(f"system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"tools/{extension}.py"):
        client.load_extension(f"tools.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"web_apps/{extension}.py"):
        client.load_extension(f"web_apps.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"filter/{extension}.py"):
        client.load_extension(f"filter.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"vc_role/{extension}.py"):
        client.load_extension(f"vc_role.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    elif os.path.isfile(f"log_system/{extension}.py"):
        client.load_extension(f"log_system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" loaded")
        await ctx.reply("Extension \"" + str(extension) + "\" loaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")



# command to MANUALLY unload a specific command / event (extension is a command / an event)
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if os.path.isfile(f"auto_publisher/{extension}.py"):
        client.unload_extension(f"auto_publisher.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"fun/{extension}.py"):
        client.unload_extension(f"fun.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"help/{extension}.py"):
        client.unload_extension(f"help.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"member_actions/{extension}.py"):
        client.unload_extension(f"member_actions.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"moderation/{extension}.py"):
        client.unload_extension(f"moderation.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"role_menu/{extension}.py"):
        client.unload_extension(f"role_menu.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"system/{extension}.py"):
        client.unload_extension(f"system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"tools/{extension}.py"):
        client.unload_extension(f"tools.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"web_apps/{extension}.py"):
        client.unload_extension(f"web_apps.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"filter/{extension}.py"):
        client.unload_extension(f"filter.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"vc_role/{extension}.py"):
        client.unload_extension(f"vc_role.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    elif os.path.isfile(f"log_system/{extension}.py"):
        client.unload_extension(f"log_system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" unloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" unloaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")

# command to MANUALLY reload a specific command / event (extension is a command / an event)
@client.command()
@commands.is_owner()
async def reload(ctx, extension):

    if os.path.isfile(f"auto_publisher/{extension}.py"):
        client.unload_extension(f"auto_publisher.{extension}")
        client.load_extension(f"auto_publisher.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"fun/{extension}.py"):
        client.unload_extension(f"fun.{extension}")
        client.load_extension(f"fun.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"help/{extension}.py"):
        client.unload_extension(f"help.{extension}")
        client.load_extension(f"help.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"member_actions/{extension}.py"):
        client.unload_extension(f"member_actions.{extension}")
        client.load_extension(f"member_actions.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"moderation/{extension}.py"):
        client.unload_extension(f"moderation.{extension}")
        client.load_extension(f"moderation.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"role_menu/{extension}.py"):
        client.unload_extension(f"role_menu.{extension}")
        client.load_extension(f"role_menu.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"system/{extension}.py"):
        client.unload_extension(f"system.{extension}")
        client.load_extension(f"system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"tools/{extension}.py"):
        client.unload_extension(f"tools.{extension}")
        client.load_extension(f"tools.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"web_apps/{extension}.py"):
        client.unload_extension(f"web_apps.{extension}")
        client.load_extension(f"web_apps.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"filter/{extension}.py"):
        client.unload_extension(f"filter.{extension}")
        client.load_extension(f"filter.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"vc_role/{extension}.py"):
        client.unload_extension(f"vc_role.{extension}")
        client.load_extension(f"vc_role.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    elif os.path.isfile(f"log_system/{extension}.py"):
        client.unload_extension(f"log_system.{extension}")
        client.load_extension(f"log_system.{extension}")
        logging.warning("Extension \"" + str(extension) + "\" reloaded")
        await ctx.reply("Extension \"" + str(extension) + "\" reloaded")

    else:
        logging.error("Extension \"" + str(extension) + "\" not found.")



# function that AUTOMATICYLLY loads all extensions
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

for filename in os.listdir("./filter"):
    if filename.endswith(".py"):
        client.load_extension(f"filter.{filename[:-3]}")

for filename in os.listdir("./vc_role"):
    if filename.endswith(".py"):
        client.load_extension(f"vc_role.{filename[:-3]}")

for filename in os.listdir("./log_system"):
    if filename.endswith(".py"):
        client.load_extension(f"log_system.{filename[:-3]}")


client.run(TOKEN)
