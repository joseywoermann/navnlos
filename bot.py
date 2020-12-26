import discord
import random
from discord.ext import commands
from discord.ext import tasks
from time import sleep
from itertools import cycle
import datetime
import requests
from bs4 import BeautifulSoup



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents = intents)
client.remove_command('help')


statuss = ['navnlos.tk', '$help']
statusmsg = cycle(statuss)
TOKEN = 'YOU TOKEN HERE'



emote_one = '1️⃣'
emote_two = '2️⃣'
emote_three = '3️⃣'
emote_four = '4️⃣'
emote_five = '5️⃣'
emote_six = '6️⃣'
emote_seven = '7️⃣'
emote_eight = '8️⃣'
emote_nine = '9️⃣'



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
@client.event
async def on_guild_join(guild):

        if guild:

            path = "logs/logs_{}.txt".format(guild.id)

            with open(path, 'a') as f:

                print(datetime.datetime.now().strftime("%d. %m. %Y; %H:%M") + " Joined Server \"" + str(guild.name) + "\" Server-ID: " + str(guild.id), file=f)

@client.event
async def on_guild_remove(guild):

        if guild:

            path = "logs/logs_{}.txt".format(guild.id)

            with open(path, 'a') as f:

                print(datetime.datetime.now().strftime("%d. %m. %Y; %H:%M") + " Left Server \"" + str(guild.name) + "\" Server-ID: " + str(guild.id), file=f)
"""

async def publisher(message):
    sleep(10)
    await message.publish()

@client.event
async def on_message(message):

    server = message.guild

    if message.channel.id == 654347445517549578:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 656591472124231761:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 737715494198706286:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 741033879032430834:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 720674929540071564:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 724946319818489946:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 685080746410639411:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 700345472300089366:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 739033895365771334:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 738838305722073221:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 738844667084406814:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    elif message.channel.id == 738840347656060968:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    # testchannel
    elif message.channel.id == 731935585828339854:
        """
        publisher_thread = threading.Thread(target=publisher, args=(message))
        publisher_thread.start()
        """
        await publisher(message)

    """
    if client.user.mentioned_in(message):
        await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")
    """
    if message.content.lower() == "hello":
        await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")

    if message.content.lower() == "hallo":
        await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")

    else:
        pass

    with open('banned_words.txt') as myfile:
        if message.content.lower() in myfile.read():
            await message.channel.purge(limit=1)
            await message.channel.send("Dieses Wort ist auf diesem Server verboten.")

    await client.process_commands(message)


    if message.content.startswith("$"):

        if server.id == 304191437652623360:

            log_channel = client.get_channel(751879355344617582)

            log_embed = discord.Embed(title=message.content, description="Channel: **{0.channel.name}** Channel-ID: [{0.channel.id}]".format(message))
            log_embed.set_author(name="User: " + message.author.name + "#" + str(message.author.discriminator) + " ID: " + str(message.author.id), icon_url=message.author.avatar_url)
            log_embed.set_footer(text=message.created_at.strftime("%Y; %m. %d., %H:%M:%S") + " Server: " + str(message.channel.guild) + " / " + str(message.guild.id))

            await log_channel.send(content=None, embed=log_embed)

        else:

            log_channel = client.get_channel(751879443810615487)

            log_embed = discord.Embed(title=message.content, description=" Channel: **{0.channel.name}** Channel-ID: [{0.channel.id}]".format(message))
            log_embed.set_author(name="User: " + message.author.name + "#" + str(message.author.discriminator) + " ID: " + str(message.author.id), icon_url=message.author.avatar_url)
            log_embed.set_footer(text=message.created_at.strftime("%Y; %m. %d., %H:%M:%S") + " Server: " + str(message.channel.guild) + " / " + str(message.guild.id))

            await log_channel.send(content=None, embed=log_embed)

    else:
        pass

    await client.process_commands(message)




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.event
async def on_ready():

    change_status.start()

    print('Bot is active')



@tasks.loop(seconds=20)
async def change_status():

    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(statusmsg)))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.event
async def on_member_join(ctx):

    server = ctx.guild

    if server.id == 304191437652623360:

        member_count_channel = client.get_channel(732309561293275198)
        member_count = server.member_count

        await member_count_channel.edit(name="Member: " + str(member_count))

    else:

        pass



@client.event
async def on_member_remove(ctx):

    server = ctx.guild

    if server.id == 304191437652623360:

        member_count_channel = client.get_channel(732309561293275198)
        member_count = server.member_count

        await member_count_channel.edit(name="Member: " + str(member_count))

    else:

        pass



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------Info-Rolemenu------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.event
async def on_raw_reaction_add(payload):
    print(payload.emoji.name)
    error_channel = client.get_channel(719996916674592768)
    message_id = payload.message_id

    if message_id == 721461113866289252:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'ls19':

            role = discord.utils.get(guild.roles, name='farmingsimulator')

        elif payload.emoji.name == 'minecraft':

            role = discord.utils.get(guild.roles, name='minecraft')

        elif payload.emoji.name == 'simunews':

            role = discord.utils.get(guild.roles, name='simulator')

        elif payload.emoji.name == 'funfacts':

            role = discord.utils.get(guild.roles, name='funfacts')

        elif payload.emoji.name == 'kaenguru':

            role = discord.utils.get(guild.roles, name='kaenguru')

        elif payload.emoji.name == 'epicdealz':

            role = discord.utils.get(guild.roles, name='epicgames')

        elif payload.emoji.name == 'redstonia':

            role = discord.utils.get(guild.roles, name='mistericraft')

        else:

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:

                await  member.add_roles(role)

            else:

                await error_channel.send("Rolemenu-Error: Member not found.")

        else:

            await error_channel.send("Rolemenu-Error: Role not found.")



#------regeln-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    error_channel = client.get_channel(719996916674592768)
    message_id = payload.message_id

    if message_id == 722547238840172675:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'check':

            role = discord.utils.get(guild.roles, name='verifiziert')

        else:

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:

                await  member.add_roles(role)

            else:

                await error_channel.send("Rolemenu-Error: Member not found.")

        else:

            await error_channel.send("Rolemenu-Error: Role not found.")


@client.event
async def on_raw_reaction_remove(payload):

    error_channel = client.get_channel(719996916674592768)
    message_id = payload.message_id

    if message_id == 721461113866289252:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'ls19':

            role = discord.utils.get(guild.roles, name='farmingsimulator')

        elif payload.emoji.name == 'minecraft':

            role = discord.utils.get(guild.roles, name='minecraft')

        elif payload.emoji.name == 'simunews':

            role = discord.utils.get(guild.roles, name='simulator')

        elif payload.emoji.name == 'funfacts':

            role = discord.utils.get(guild.roles, name='funfacts')

        elif payload.emoji.name == 'kaenguru':

            role = discord.utils.get(guild.roles, name='kaenguru')

        elif payload.emoji.name == 'epicdealz':

            role = discord.utils.get(guild.roles, name='epicgames')

        elif payload.emoji.name == 'redstonia':

            role = discord.utils.get(guild.roles, name='mistericraft')

        else:

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:

                await  member.remove_roles(role)

            else:

                await error_channel.send("Rolemenu-Error: Member not found.")

        else:

            await error_channel.send("Rolemenu-Error: Role not found.")



#------regeln-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    error_channel = client.get_channel(719996916674592768)
    message_id = payload.message_id

    if message_id == 722547238840172675:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'check':

            role = discord.utils.get(guild.roles, name='verifiziert')

        else:

            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:

                await  member.remove_roles(role)

            else:

                await error_channel.send("Rolemenu-Error: Member not found.")

        else:

            await error_channel.send("Rolemenu-Error: Role not found.")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.command(aliases=['h'])
@commands.guild_only()
async def help(ctx, arg = None):

    await ctx.channel.purge(limit=1)

    if arg == None:

        help_embed = discord.Embed(title="Commands", colour=discord.Color.gold())
        help_embed.add_field(name="$invite/$inv", value="Invitelink zum MisteriCraft-Communityserver")
        help_embed.add_field(name="$question/$q", value="Beantwortet Ja/Nein-Fragen")
        help_embed.add_field(name="$ping/$p", value="Latenz des Bots")
        help_embed.add_field(name="$info/$i", value="Bot-Information")
        help_embed.add_field(name="$changelog/$cl", value="Zeigt den Changelog")
    #    help_embed.add_field(name="$time/$z", value="Gibt die aktuelle Zeit aus.")
        help_embed.add_field(name="$day/$t", value="Gibt das aktuelle Datum an")
        help_embed.add_field(name="$help/$h", value="Selbsterklaerend")
        help_embed.add_field(name="$repeat/$rep", value="Sendet deine Nachricht als Embed")
        help_embed.add_field(name="$poll", value="Umfrage mit bis zu 9 Antworten. Woerter mit `_` trennen: `$poll Ja? Ja Definitiv_nicht`")
        help_embed.add_field(name="$wiki", value="Wikipedia-Suche")
        help_embed.add_field(name="$price", value="Preisvergleich für angegebenes Produkt")
        help_embed.add_field(name="$define", value="Definiert ein Wort")
        help_embed.add_field(name="$bpm", value="Tempo fuer einen angegebenen Song")
        help_embed.add_field(name="$dummy", value="Tut absolut garnichts")
        help_embed.add_field(name="$userinfo", value="Zeigt informationen ueber einen User")
        help_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.send(content=None, embed=help_embed)

    else:

        if arg == "invite":
            await ctx.send("```Invite: $invite```")

        elif arg == "question":
            await ctx.send("```Question: $question <DEINE FRAGE>```")

        elif arg == "ping":
            await ctx.send("```Ping: $ping```")

        elif arg == "info":
            await ctx.send("```Info: $info```")

        elif arg == "changelog":
            await ctx.send("```Changelog: $changelog```")

        elif arg == "day":
            await ctx.send("```Day: $day```")

        elif arg == "help":
            await ctx.send("```Help: $help <COMMAND> | Command optional```")

        elif arg == "repeat":
            await ctx.send("```Repeat: $repeat <DEINE NACHRICHT```")

        elif arg == "poll":
            await ctx.send("```Poll: $poll <DEINE FRAGE> <ANTWORTMOEGLICHKEI 1> <ANTWORTMOEGLICHKEI 2> ... <ANTWORTMOEGLICHKEI 9> | Mindestens 2 Antwortmoeglichkeiten```")

        elif arg == "wiki":
            await ctx.send("```Wiki: $wiki <SUCHBEGRIFF>```")

        elif arg == "price":
            await ctx.send("```Price: $price <SUCHBEGRIFF>```")

        elif arg == "define":
            await ctx.send("```Define: $define <SUCHBEGRIFF>```")

        elif arg == "bpm":
            await ctx.send("```BPM: $bpm <SONG>```")

        elif arg == "userinfo":
            await ctx.send("```Userinfo: $userinfo <USERMENTION (@user)>```")

        else:
            pass





@client.command(aliases=['mh'])
@commands.has_permissions(manage_messages=True)
@commands.guild_only()
async def modhelp(ctx):

    help_embed = discord.Embed(title="Commands exklusiv fuer Moderatoren", colour=discord.Color.gold())
    help_embed.add_field(name="$clear/$c", value="Loescht die angegebene Anzahl an Nachrichten.")
    help_embed.add_field(name="$kick/$k", value="Kickt einen User.")
    help_embed.add_field(name="$ban/$b", value="Bannt einen User")
    help_embed.add_field(name="$banid", value="Bannt einen User mithilfe der ID. User, die nicht auf dem Server sind, koennen so gebannt werden.")
    help_embed.add_field(name="$unban/$ub", value="Entbannt einen User")
    help_embed.add_field(name="$addrole/$ar", value="Fuegt einem User eine Rolle hinzu")
    help_embed.add_field(name="$removerole/$rr", value="Entfernt einem User eine Rolle")
    help_embed.add_field(name="$slomo", value="Setzt den Slowmode fuer den Kannal auf die angegebene Sekundenzahl")
    help_embed.add_field(name="$channeledit/$edit", value="Aendert den Namen / Beschreibung eines Channels")
    help_embed.add_field(name="$nickedit/$nick", value="Aendert den Nickname eines Users")
    help_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=help_embed)



@client.command(aliases=['i', 'about'])
@commands.guild_only()
async def info(ctx):

    info_embed = discord.Embed(title="Information", description="Version 1.5.2 by jcw05#1331\nhttp://navnlos.tk/", color=discord.Color.lighter_grey())
    info_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=info_embed)



@client.command(aliases=['cl'])
@commands.guild_only()
async def changelog(ctx):

    changelog_embed = discord.Embed(title="Changelog for version 1.5.2", color=discord.Color.lighter_grey())
    changelog_embed.add_field(name="Allgemein:", value="Bugfixes")




    changelog_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=changelog_embed)



@client.command(aliases=['q'])
@commands.guild_only()
async def question(ctx, *, question):

    response = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Wahrscheinlich nicht']
    response_embed = discord.Embed(title="Deine Frage: \"" + str(question) + "\" Die Antwort: " + str(random.choice(response)), color=discord.Color.gold())
    response_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=response_embed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['inv'])
@commands.guild_only()
async def invite(ctx):

    invite = "https://discord.gg/KVbdvK8"

    invite_embed = discord.Embed(title="Invitelink zum MisteriCraft-Communityserver:\n" + str(invite), color=discord.Color.gold())
    invite_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=invite_embed)




@client.command(aliases=['rep'])
@commands.guild_only()
async def repeat(ctx, *, text):

    repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())
    repeat_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=repeat_embed)


"""
@client.command(aliases=['z'])
async def time(ctx):

    current_time = datetime.datetime.now().strftime("%H:%M")
    message = f"Es ist {current_time} Uhr."
    time_embed = discord.Embed(title=message, color=discord.Color.gold())

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=time_embed)
"""


@client.command(aliases=['t'])
@commands.guild_only()
async def day(ctx):

    current_day = datetime.datetime.now().strftime("%A, der %d. %B %Y, der %j. Tag dieses Jahres")
    message = f"Heute ist {current_day}."
    day_embed = discord.Embed(title=str(message), color=discord.Color.gold())
    day_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=day_embed)



@client.command(aliases=['d'])
@commands.guild_only()
async def dice(ctx, arg=6):

    dice_result = random.randint(1, arg)
    dice_embed = discord.Embed(title="Zufällige Zahl zwischen 1 und " + str(arg) + ":\n\nErgebnis: __" + str(dice_result) + "__", color=discord.Color.gold())
    dice_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=dice_embed)



@client.command(aliases=['p'])
@commands.guild_only()
async def ping(ctx, r=None):

    if r == "precise":
        ping_embed = discord.Embed(title=f"Pong! {(client.latency * 1000)} Millisekunden", colour=discord.Color.gold())
        ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    else:
        ping_embed = discord.Embed(title=f"Pong! {round(client.latency * 1000)} Millisekunden", colour=discord.Color.gold())
        ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=ping_embed)



@client.command()
@commands.guild_only()
async def wiki(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://wikipedia.org/w/index.php?search=" + search_term)



@client.command(aliases = ['preis'])
@commands.guild_only()
async def price(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://geizhals.de/?fs=" + search_term)



@client.command(aliases = ['def'])
@commands.guild_only()
async def define(ctx, *, search_term):

    URL = "https://www.urbandictionary.com/define.php?term=" + str(search_term)
    page = requests.get(URL)
    fetched_page = BeautifulSoup(page.content, 'html.parser')

    searched_word = fetched_page.find('a', attrs={'class': 'word'})
    meaning = fetched_page.find('div', attrs={'class': 'meaning'})

    if searched_word:
        name_output = str(searched_word.text)
    else:
        name_output = "No results."
    if meaning:
        meaning_output = str(meaning.text)
    else:
        meaning_output = "No results."

    define_embed = discord.Embed(title=name_output, description=meaning_output)
    await ctx.send(content=None, embed=define_embed)



@client.command()
@commands.guild_only()
async def bpm(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '-')

    await ctx.send("https://songbpm.com/searches/" + search_term)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['arep'])
@commands.has_permissions(manage_messages=True)
@commands.guild_only()
async def anonymrepeat(ctx, *, text):

    repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=repeat_embed)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
@commands.guild_only()
async def poll(ctx, question=None, response0=None, response1=None, response2=None, response3=None, response4=None, response5=None, response6=None, response7=None, response8=None):

    await ctx.channel.purge(limit=1)

    if question:

        while '_' in question:
            question = question.replace('_',' ')

        print("q=1")

        if response0:#

            while '_' in response0:
                response0 = response0.replace('_',' ')

            print("a=1")

            if response1:#

                while '_' in response1:
                    response1 = response1.replace('_',' ')

                print("a=2")

                if response2:#

                    while '_' in response2:
                        response2 = response2.replace('_',' ')

                    print("a=3")

                    if response3:#

                        while '_' in response3:
                            response3 = response3.replace('_',' ')

                        print("a=4")

                        if response4:#

                            while '_' in response4:
                                response4 = response4.replace('_',' ')

                            print("a=5")

                            if response5:#

                                while '_' in response5:
                                    response5 = response5.replace('_',' ')

                                print("a=6")

                                if response6:#

                                    while '_' in response6:
                                        response6 = response6.replace('_',' ')

                                    print("a=7")

                                    if response7:#

                                        while '_' in response7:
                                            response7 = response7.replace('_',' ')

                                        print("a=8")

                                        if response8:#

                                            while '_' in response8:
                                                response8 = response8.replace('_',' ')

                                            print("a=9")

                                            #await ctx.send(response0 + response1 + response2 + response3 + response4 + response5 + response6 + response7 + response8)

                                            poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6) + "\n:eight: " + str(response7) + "\n:nine: " + str(response8), color=discord.Color.orange())
                                            poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                            msg = await ctx.send(content=None, embed=poll_embed)

                                            await msg.add_reaction(emote_one)
                                            await msg.add_reaction(emote_two)
                                            await msg.add_reaction(emote_three)
                                            await msg.add_reaction(emote_four)
                                            await msg.add_reaction(emote_five)
                                            await msg.add_reaction(emote_six)
                                            await msg.add_reaction(emote_seven)
                                            await msg.add_reaction(emote_eight)
                                            await msg.add_reaction(emote_nine)

                                        else:

                                            #await ctx.send(response0 + response1 + response2 + response3 + response4 + response5 + response6 + response7)

                                            poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6) + "\n:eight: " + str(response7), color=discord.Color.orange())
                                            poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                            msg = await ctx.send(content=None, embed=poll_embed)

                                            await msg.add_reaction(emote_one)
                                            await msg.add_reaction(emote_two)
                                            await msg.add_reaction(emote_three)
                                            await msg.add_reaction(emote_four)
                                            await msg.add_reaction(emote_five)
                                            await msg.add_reaction(emote_six)
                                            await msg.add_reaction(emote_seven)
                                            await msg.add_reaction(emote_eight)

                                    else:

                                        #await ctx.send(response0 + response1 + response2 + response3 + response4 + response5 + response6)

                                        poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6), color=discord.Color.orange())
                                        poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                        msg = await ctx.send(content=None, embed=poll_embed)

                                        await msg.add_reaction(emote_one)
                                        await msg.add_reaction(emote_two)
                                        await msg.add_reaction(emote_three)
                                        await msg.add_reaction(emote_four)
                                        await msg.add_reaction(emote_five)
                                        await msg.add_reaction(emote_six)
                                        await msg.add_reaction(emote_seven)

                                else:

                                    #await ctx.send(response0 + response1 + response2 + response3 + response4 + response5)

                                    poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5), color=discord.Color.orange())
                                    poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                    msg = await ctx.send(content=None, embed=poll_embed)

                                    await msg.add_reaction(emote_one)
                                    await msg.add_reaction(emote_two)
                                    await msg.add_reaction(emote_three)
                                    await msg.add_reaction(emote_four)
                                    await msg.add_reaction(emote_five)
                                    await msg.add_reaction(emote_six)

                            else:

                                #await ctx.send(response0 + response1 + response2 + response3 + response4)

                                poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4), color=discord.Color.orange())
                                poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                msg = await ctx.send(content=None, embed=poll_embed)

                                await msg.add_reaction(emote_one)
                                await msg.add_reaction(emote_two)
                                await msg.add_reaction(emote_three)
                                await msg.add_reaction(emote_four)
                                await msg.add_reaction(emote_five)

                        else:

                            #await ctx.send(response0 + response1 + response2 + response3)

                            poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3), color=discord.Color.orange())
                            poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                            msg = await ctx.send(content=None, embed=poll_embed)

                            await msg.add_reaction(emote_one)
                            await msg.add_reaction(emote_two)
                            await msg.add_reaction(emote_three)
                            await msg.add_reaction(emote_four)


                    else:

                        #await ctx.send(response0 + response1 + response2)

                        poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2), color=discord.Color.orange())
                        poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                        msg = await ctx.send(content=None, embed=poll_embed)

                        await msg.add_reaction(emote_one)
                        await msg.add_reaction(emote_two)
                        await msg.add_reaction(emote_three)

                else:

                    #await ctx.send(response0 + response1)

                    poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1), color=discord.Color.orange())
                    poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                    msg = await ctx.send(content=None, embed=poll_embed)

                    await msg.add_reaction(emote_one)
                    await msg.add_reaction(emote_two)


            else:
                poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmoeglichkeiten haben.", color=discord.Color.dark_purple())
                poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
                await ctx.send(content=None, embed=poll_error_embed)

        else:
            poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmoeglichkeiten haben.", color=discord.Color.dark_purple())
            poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.send(content=None, embed=poll_error_embed)
    else:
        poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmoeglichkeiten und eine Frage haben.", color=discord.Color.dark_purple())
        poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(content=None, embed=poll_error_embed)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
@commands.is_owner()
async def setstatus(ctx, *, newstatus):

    await ctx.channel.purge(limit=1)
    statuss.append(newstatus)
    setstatus_embed = discord.Embed(title=str(newstatus) + " zu Botstatus hinzugefuegt.")
    await ctx.send(embed=setstatus_embed)



@client.command()
@commands.is_owner()
@commands.guild_only()
async def leave(ctx, id=None):

    owner = ctx.message.author

    if id:

        server = client.get_guild(int(id))

    else:
        server = ctx.guild

    await server.leave()

    await owner.send("Left ***" + str(server.name) + "***. Server-ID: " + str(server.id))

#

@client.command()
@commands.is_owner()
async def stop(ctx):

    stop_embed = discord.Embed(title="Bot gestoppt", color = discord.Color.green())

    try:
        shuttingdowngif = await ctx.send("https://tenor.com/view/pc-computer-shutting-down-off-windows-computer-gif-17192330")
        sleep(5)
        await shuttingdowngif.delete()
        await ctx.send(content=None, embed=stop_embed)
        await client.logout()

    except:

        print("nope")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.command(aliases=['ui'])
async def userinfo(ctx, person: discord.Member):

    rollen = ''
    for role in person.roles:
        if not role.is_default():
            rollen += '{} \r\n'.format(role.mention)


    userinfo_embed = discord.Embed(title=str(person))
    userinfo_embed.add_field(name="Joined am", value=person.joined_at.strftime("%d.%m.%Y um %H:%M:%S"))
    userinfo_embed.add_field(name="Joined Discord am:", value=person.created_at.strftime("%d.%m.%Y um %H:%M:%S"))
    userinfo_embed.add_field(name="Status", value=str(person.status))
    userinfo_embed.add_field(name="Rollen", value=rollen)
    userinfo_embed.add_field(name="ID", value=str(person.id))
    userinfo_embed.add_field(name="top role", value=person.top_role)
    #userinfo_embed.add_field(name="Nitro", value=str(person.nitro))
    userinfo_embed.set_thumbnail(url=person.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=userinfo_embed)

"""
@client.command()
async def serverinfo(ctx):

    server = ctx.guild

    serverinfo_embed = discord.Embed(title=str(server.name))
    serverinfo_embed.add_field(name="AFK-Timeout in Minuten", value=server.afk_timeout / 60)
    serverinfo_embed.add_field(name="ID", value=server.id)
    serverinfo_embed.add_field(name="Owner", value=server.owner.name)
    serverinfo_embed.add_field(name="Anzahl der Member", value=server.member_count)
    serverinfo_embed.add_field(name="Erstellt am", value=server.created_at.strftime("%d.%m.%Y um %H:%M:%S"))
    #serverinfo_embed.add_field(name="Invites", value=server.)
    serverinfo_embed.set_thumbnail(url=server.icon_url)

    await ctx.send(content=None, embed=serverinfo_embed)
"""



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
@commands.guild_only()
async def clear(ctx, amount_typed=1, arg=' '):


    clear_pin_embed = discord.Embed(title=str(amount_typed) + " Nachricht(en) wurden geloescht.", color=discord.Color.dark_red())
    clear_pin_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    clear_overflow_embed = discord.Embed(title="Du darfst maximal 1000 Nachrichten gleichzeitig loeschen.")
    clear_overflow_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    amount = amount_typed + 1

    if amount <= 1001:

        if arg == 'pin':

            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=clear_pin_embed)
            sleep(1)
            await ctx.channel.purge(limit=1)

        else:

            deleted = await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)

            clear_embed = discord.Embed(title='{} Nachrichten geloescht.'.format(len(deleted)-1), color=discord.Color.dark_red())
            clear_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

            await ctx.send(embed=clear_embed)
            sleep(1)
            await ctx.channel.purge(limit=1)

    else:

        await ctx.send(content=None, embed=clear_overflow_embed)
        sleep(1)
        await ctx.channel.purge(limit=2)



@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
@commands.guild_only()
async def kick(ctx, person: discord.Member, *, reason=None):

    kick_embed = discord.Embed(title=str(person) + " wurde gekickt.", colour=discord.Color.dark_red())
    kick_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    kick_error_embed = discord.Embed(title="User konnte nicht gekickt werden.", colour=discord.Color.dark_purple())
    kick_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


    await ctx.channel.purge(limit=1)
    try:

        await person.kick(reason=reason)
        await ctx.send(content=None, embed=kick_embed)


    except:

        await ctx.send(content=None, embed=kick_error_embed)
        sleep(5)
        await ctx.channel.purge(limit=1)



@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
@commands.guild_only()
async def ban(ctx, person: discord.Member, *, reason=None):

    ban_embed = discord.Embed(title=str(person) + " wurde gebannt.", color=discord.Color.dark_red())
    ban_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    ban_error_embed = discord.Embed(title="User konnte nicht gebannt werden", color=discord.Color.dark_purple())
    ban_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


    await ctx.channel.purge(limit=1)
    try:

        await person.ban(reason=reason)
        await ctx.send(content=None, embed=ban_embed)


    except:

        await ctx.send(content=None, embed=ban_error_embed)
        sleep(5)
        await ctx.channel.purge(limit=1)



@client.command()
@commands.has_permissions(ban_members=True)
@commands.guild_only()
async def banid(ctx, user_id, *, reason=None):
    user = await client.fetch_user(user_id)
    ban_embed = discord.Embed(title=str(user.name) + " wurde gebannt.", color=discord.Color.dark_red())
    ban_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    ban_error_embed = discord.Embed(title="User konnte nicht gebannt werden", color=discord.Color.dark_purple())
    ban_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)



    await ctx.channel.purge(limit=1)
    try:

        await ctx.guild.ban(user, reason=reason)
        await ctx.send(content=None, embed=ban_embed)


    except:

        await ctx.send(content=None, embed=ban_error_embed)
        sleep(5)
        await ctx.channel.purge(limit=1)


    user = await client.fetch_user(user_id)




@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
@commands.guild_only()
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    unban_embed = discord.Embed(title=str(member) + " wurde entbannt.", color=discord.Color.dark_red())
    unban_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


    await ctx.channel.purge(limit=1)

    for ban_entry in banned_users:

        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):

            try:

                await ctx.guild.unban(user)
                await ctx.send(content=None, embed=unban_embed)

            except:

                return



@client.command(aliases=['nick'])
@commands.has_permissions(manage_nicknames=True)
@commands.guild_only()
async def nickedit(ctx, mensch: discord.Member, newname):

    await ctx.channel.purge(limit=1)
    if newname:

        try:

            await mensch.edit(nick=newname)

        except:

            pass #errormessage einfuegen

    else:
        pass



@client.command(aliases=['edit'])
@commands.has_permissions(manage_channels=True)
@commands.guild_only()
async def channeledit(ctx, thing, *, newattribut):

    await ctx.channel.purge(limit=1)
    if thing == "name":

        if newattribut:

            try:

                await ctx.channel.edit(name=newattribut)

            except:

                ctx.send("Kanalname konnte nicht geaendert werden.")

        else:

            ctx.send("Bitte spezifiziere einen neuen Kanalnamen.")


    elif thing == "topic":

        if newattribut:

            try:

                await ctx.channel.edit(topic=newattribut)

            except:

                ctx.send("Kanalbeschreibung konnte nicht geaendert werden.")
        else:

            ctx.send("Bitte spezifiziere eine neue Kanalbeschreibung.")


    else:

        await ctx.send("Bitte \"name\" oder \"topic\" angeben.")


@client.command()
@commands.has_permissions(manage_channels=True)
@commands.guild_only()
async def slomo(ctx, delay):

    slomo_embed = discord.Embed(title="Slowmode auf " + str(delay) + " Sekunden gesetzt.", color=discord.Color.dark_red())
    slomo_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.send(content=None, embed=slomo_embed)



@client.command(aliases=['ar'])
@commands.has_permissions(manage_roles=True)
@commands.guild_only()
async def addrole(ctx, person: discord.Member, *, role):

    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    addrole_embed = discord.Embed(title="Rolle __" + str(roles) + "__ zu " + str(person) + " hinzugefuegt")
    addrole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)

    try:

        await person.add_roles(roles)
        await ctx.send(content=None, embed=addrole_embed)

    except:

        return


@client.command(aliases=['rr'])
@commands.has_permissions(manage_roles=True)
@commands.guild_only()
async def removerole(ctx, person: discord.Member, *, role):

    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    removerole_embed = discord.Embed(title="Rolle __" + str(roles) + "__ von " + str(person) + " entfernt")
    removerole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)

    try:

        await person.remove_roles(roles)
        await ctx.send(content=None, embed=removerole_embed)

    except:

        return



@client.command()
@commands.guild_only()
async def dummy(ctx):
    await ctx.channel.purge(limit=1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

client.run(TOKEN)
