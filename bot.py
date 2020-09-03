import discord
import random
from discord.ext import commands
from discord.ext import tasks
from time import sleep
from itertools import cycle
import datetime



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


client = commands.Bot(command_prefix='$')
client.remove_command('help')
status = cycle(['bit.ly/navnlos', '$help'])

TOKEN = 'YOUR TOKEN HERE'


#test123



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



@client.event
async def on_guild_join(guild):

        if guild:

            path = "logs_{}.txt".format(guild.id)

            with open(path, 'a') as f:

                print(datetime.datetime.now().strftime("%d. %m. %Y; %H:%M") + " Joined Server \"" + str(guild.name) + "\" Server-ID: " + str(guild.id), file=f)

@client.event
async def on_guild_remove(guild):

        if guild:

            path = "logs_{}.txt".format(guild.id)

            with open(path, 'a') as f:

                print(datetime.datetime.now().strftime("%d. %m. %Y; %H:%M") + " Left Server \"" + str(guild.name) + "\" Server-ID: " + str(guild.id), file=f)




@client.event
async def on_message(message):


    if message.content.lower() == "hello":
        await message.channel.send("https://tenor.com/view/penguin-hello-hi-heythere-cutie-gif-3950966")

    server = message.guild

    if server:

#        if message.content.startswith("-"):

        path = "logs_{}.txt".format(server.id)
        #cmds = ['addrole', 'amazon', 'anonymrepeat', 'ban', 'changelog', 'channeledit', 'clear', 'createinvite', 'credits', 'day', 'dice', 'help', 'info', 'invite', 'kick', 'leave', 'maps', 'modhelp', 'nickedit', 'ping', 'poll', 'price', 'question', 'removerole', 'repeat', 'serverinfo', 'slomo', 'test', 'unban', 'userinfo', 'wiki']

            #if cmds in message.content.lower():

        with open(path, 'a') as f:

            print("Date: {0.created_at}     Server: {0.channel.guild} Server-ID: [{0.guild.id}]     Channel: {0.channel.name} Channel-ID: [{0.channel.id}]     User: {0.author.name}#{0.author.discriminator} [ID: {0.author.id}]     Message: {0.content} [Message-ID: {0.id}]".format(message), file=f)

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

    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.command(aliases=['h'])
async def help(ctx, arg=None):

    help_embed = discord.Embed(title="Commands", colour=discord.Color.gold())
    help_embed.add_field(name="$invite/$inv", value="Sends/creates an invite-links to this server")
    help_embed.add_field(name="$question/$q", value="Answers your most crucial yes/no questions")
    help_embed.add_field(name="$ping/$p", value="Shows the bots latency")
    help_embed.add_field(name="$info/$i", value="Shows some information about navnlos")
    help_embed.add_field(name="$changelog/$cl", value="Shows the changelog")
#    help_embed.add_field(name="$time/$z", value="Gibt die aktuelle Zeit aus.")
    help_embed.add_field(name="$day/$t", value="Shows the date (point of reference: UTC)")
    help_embed.add_field(name="$help/$h", value="so I really have to comment on that?")
    help_embed.add_field(name="$repeat/$rep", value="makes an embed containing your message")
    help_embed.add_field(name="$poll", value="creates a poll with up to 9 answers. Attention: if the question /an answer is made up of more than one word, you have to use `_`between those. example `$poll Hello_there! Hi Go_away`")
    help_embed.add_field(name="$wiki", value="searches Wikipedia")
    help_embed.add_field(name="$maps", value="shows the location you are searching for on google maps [For some reason, this only works on PC]")
    help_embed.add_field(name="$amazon", value="searches àmazon.com`")
    help_embed.add_field(name="$duden", value="searches the \"duden\"")
    help_embed.add_field(name="$price", value="returns the best price for the thing you´re looking for (Only )")
    help_embed.add_field(name="$define", value="defines a thing. Powered by https://urbandictionary.com")
    help_embed.add_field(name="$credits", value="Shows the credits (incomplete)")
    help_embed.add_field(name="$dummy", value="does absulutely nothing")
    help_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    if arg == "dir":
        author = ctx.message.author
    else:
        author = ctx


    await ctx.channel.purge(limit=1)
    await author.send(content=None, embed=help_embed)



@client.command(aliases=['mh'])
@commands.has_permissions(manage_messages=True)
async def modhelp(ctx, arg=None):

    help_embed = discord.Embed(title="Commands exklusiv fuer Moderatoren", colour=discord.Color.gold())
    help_embed.add_field(name="$clear/$c", value="Deletes the specified amount of messages in the channel. with `pin`, you can also delete the pinned messages example:`$clear 100 pin`")
    help_embed.add_field(name="$kick/$k", value="Kicks a user. Example: `$kick @jcw05`")
    help_embed.add_field(name="$ban/$b", value="Bans a user")
    help_embed.add_field(name="$unban/$ub", value="Unbans a user. Example: `$unban jcw05#1331`")
    help_embed.add_field(name="$addrole/$ar", value="Adds a role to a user. Example: `$addrole @jcw05 rolexyz`")
    help_embed.add_field(name="$removerole/$rr", value="Removes a role from a user. Example: `$removerole @jcw05 rolexyz`")
    help_embed.add_field(name="$slomo", value="Sets the Slow-Mode. Example: `$slomo 60`- 1 minute; `$slomo 0`- no more slow-mode")
    help_embed.add_field(name="$channeledit/$edit", value="Edits the name/topic of a channel. Example: `$edit name xyz`/`$edit topic xyz`")
    help_embed.add_field(name="$nickedit/$nick", value="Changes the nickname of a user. Example: `$nickedit @jcw05 new-nickname-here`")
    help_embed.add_field(name="$nbanid", value="Bans a user via his ID. Using this command, you can ban users who have never joined your server, or have left the server. Using this method, you can create a \"blacklist\" of users, that you don´t want on your server.")
#    help_embed.add_field(name="$lock", value="Entzieht ALLEN Usern, ausser Moderatoren, die Berechtigung, nachrichten zu schreiben.")
    help_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    if arg == "dir":
        author = ctx.message.author
    else:
        author = ctx


    await ctx.channel.purge(limit=1)
    await author.send(content=None, embed=help_embed)



@client.command(aliases=['i', 'about'])
async def info(ctx):

    info_embed = discord.Embed(title="Information", description="Version 1.4.1 by jcw05#1331\nhttps://bit.ly/navnlos", color=discord.Color.lighter_grey())
    info_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=info_embed)



@client.command(aliases=['cl'])
async def changelog(ctx):

    changelog_embed = discord.Embed(title="Changelog for version 1.4.1", color=discord.Color.lighter_grey())
    changelog_embed.add_field(name="Bugfixes:", value="Fixed a bug, that every answer, that is not the first one, was indented on mobile devices.")



    changelog_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=changelog_embed)



@client.command(aliases=['q'])
async def question(ctx, *, question):

    response = ['yes', 'no', 'maybe', 'probably', 'probably not']
    response_embed = discord.Embed(title="Your question: \"" + str(question) + "\" The answer: " + str(random.choice(response)), color=discord.Color.gold())
    response_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=response_embed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['inv'])
async def invite(ctx, temp=None):


    if ctx.guild.id != 304191437652623360:

        if temp == "temp":

            invite = await ctx.channel.create_invite(max_age=43200)

            invite_embed = discord.Embed(title="12-hour-invite:\n" + str(invite), color=discord.Color.gold())
            invite_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(content=None, embed=invite_embed)

        else:

            invite = await ctx.channel.create_invite(max_age=0)

            invite_embed = discord.Embed(title="invite:\n" + str(invite), color=discord.Color.gold())
            invite_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(content=None, embed=invite_embed)

    else:

        pass

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=invite_embed)




@client.command(aliases=['rep'])
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
async def day(ctx):

    current_day = datetime.datetime.now().strftime("%A, the %d. of %B %Y, which is the %jth day of the year")
    message = f"It is {current_day}."
    day_embed = discord.Embed(title=str(message), color=discord.Color.gold())
    day_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=day_embed)



@client.command(aliases=['d'])
async def dice(ctx, arg=6):

    dice_result = random.randint(1, arg)
    dice_embed = discord.Embed(title=dice_result, color=discord.Color.gold())
    dice_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=dice_embed)



@client.command(aliases=['p'])
async def ping(ctx, r=None):

    if r == "precise":
        ping_embed = discord.Embed(title=f"Pong! {(client.latency * 1000)} milliseconds", colour=discord.Color.gold())
        ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    else:
        ping_embed = discord.Embed(title=f"Pong! {round(client.latency * 1000)} milliseconds", colour=discord.Color.gold())
        ping_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)


    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=ping_embed)



@client.command()
async def wiki(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://wikipedia.org/w/index.php?search=" + search_term)



@client.command(aliases = ['amzn'])
async def amazon(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://www.amazon.com/s?k=" + search_term)



@client.command(aliases = ['preis'])
async def price(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://geizhals.de/?fs=" + search_term)



@client.command(aliases = ['locate'])
async def maps(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://google.com/maps/search/" + search_term)



@client.command(aliases = ['def'])
async def define(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://www.urbandictionary.com/define.php?term=" + search_term)



@client.command()
async def duden(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://www.duden.de/suchen/dudenonline/" + search_term)




@client.command()
async def credits(ctx):
    credits_embed = discord.Embed(title="Credits")
    credits_embed.add_field(name="General help:", value="https://discordpy.readthedocs.io/en/latest/api.html")
    credits_embed.add_field(name="Reference for `$time`und `$date`:", value="https://strftime.org/")
    credits_embed.add_field(name="Get the ID of a mention:", value="https://stackoverflow.com/questions/53026087/how-to-get-id-of-a-mentioned-user-discord-py")
    credits_embed.add_field(name="Command-Reference:", value="https://discordpy.readthedocs.io/en/latest/ext/commands/api.html")
    credits_embed.add_field(name="Specific channel:", value="https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-send-a-message-to-a-specific-channel")
    credits_embed.add_field(name="Some commands:", value="https://www.youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ")
    credits_embed.add_field(name="Embeds:", value="https://youtu.be/RwAqp26s9aE")
    credits_embed.add_field(name="Embed-generator:", value="https://cog-creators.github.io/discord-embed-sandbox/")
    credits_embed.add_field(name="Rolemenus:", value="https://youtu.be/MgCJG8kkq50")
    credits_embed.add_field(name="*Actually being able to use them:*:", value="https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working")
#    credits_embed.add_field(name="reference for `$userinfo`und `$clear`:", value="https://www.youtube.com/watch?v=Ml0mzupoHuU")
    credits_embed.add_field(name="Hoster:", value="https://www.heroku.com/")
#    credits_embed.add_field(name="", value="")
#    credits_embed.add_field(name="", value="")
    credits_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)



    await ctx.send(content=None, embed=credits_embed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['arep'])
@commands.has_permissions(manage_messages=True)
async def anonymrepeat(ctx, *, text):

    repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=repeat_embed)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
async def poll(ctx, question=None, response0=None, response1=None, response2=None, response3=None, response4=None, response5=None, response6=None, response7=None, response8=None):

    await ctx.channel.purge(limit=1)




    if question:#

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
                poll_error_embed = discord.Embed(title="Error", description="Please specify at least 2 answers", color=discord.Color.dark_purple())
                poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
                await ctx.send(content=None, embed=poll_error_embed)

        else:
            poll_error_embed = discord.Embed(title="Error", description="Please specify at least 2 answers", color=discord.Color.dark_purple())
            poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
            await ctx.send(content=None, embed=poll_error_embed)
    else:
        poll_error_embed = discord.Embed(title="Error", description="Please specify at least 2 answers and a question", color=discord.Color.dark_purple())
        poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(content=None, embed=poll_error_embed)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@client.command()
@commands.is_owner()
async def leave(ctx, id=None):

    owner = ctx.message.author

    if id:

        server = client.get_guild(int(id))

    else:
        server = ctx.guild

    await server.leave()

    await owner.send("Left ***" + str(server.name) + "***. Server-ID: " + str(server.id))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
@client.command(aliases=['ui'])
async def userinfo(ctx, person: discord.Member):

    rollen = ''
    for role in person.roles:
        if not role.is_default():
            rollen += '{} \r\n'.format(role.mention)

    userinfo_embed = discord.Embed(title=str(person))
    userinfo_embed.add_field(name="Standart-Avatar", value=str(person.default_avatar))
    userinfo_embed.add_field(name="Aktivitaet", value=person.activities)
    userinfo_embed.add_field(name="Joined am", value=person.joined_at.strftime("%d.%m.%Y um %H:%M:%S"))
    userinfo_embed.add_field(name="Joined Discord at:", value=person.created_at.strftime("%d.%m.%Y um %H:%M:%S"))
    userinfo_embed.add_field(name="Status", value=str(person.status))
    userinfo_embed.add_field(name="Rollen", value=rollen)
    userinfo_embed.set_thumbnail(url=person.avatar_url)

    await ctx.send(content=None, embed=userinfo_embed)


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
async def banid(ctx, user_id, *, reason=None):
    await ctx.channel.purge(limit=1)
    user = await client.fetch_user(user_id)
    await ctx.guild.ban(user, reason=reason)



@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
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
async def nickedit(ctx, mensch: discord.Member, newname):

    await ctx.channel.purge(limit=1)
    if newname:

        try:

            await mensch.edit(nick=newname)

        except:

            pass#errormessage einfuegen

    else:

        pass



@client.command(aliases=['edit'])
@commands.has_permissions(manage_channels=True)
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

        pass#errormessage einfuegen


@client.command()
@commands.has_permissions(manage_channels=True)
async def slomo(ctx, delay):

    slomo_embed = discord.Embed(title="Slowmode auf " + str(delay) + " Sekunden gesetzt.", color=discord.Color.dark_red())
    slomo_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.send(content=None, embed=slomo_embed)



"""
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, *, args=None):

    await ctx.channel.purge(limit=1)

    guild = ctx.guild
    members = guild.members
    lock_embed = discord.Embed(title="Channel wurden gelockt", color=discord.Color.dark_red())

    for member in members:

        if member.top_role.id == 719486012182626315 or 713411213463388332:

            roles = discord.utils.get(guild.roles, name="Muted")
            await member.add_roles(roles)
            await ctx.send(content=None, embed=lock_embed)

        else:

            pass
"""


@client.command(aliases=['ar'])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, person: discord.Member, *, role):

    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    addrole_embed = discord.Embed(title="Rolle " + str(roles) + " zu " + str(person) + " hinzugefuegt")
    addrole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)

    try:

        await person.add_roles(roles)
        await ctx.send(content=None, embed=addrole_embed)

    except:

        return


@client.command(aliases=['rr'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, person: discord.Member, *, role):

    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    removerole_embed = discord.Embed(title="Rolle " + str(roles) + " von " + str(person) + " entfernt")
    removerole_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)

    try:

        await person.remove_roles(roles)
        await ctx.send(content=None, embed=removerole_embed)

    except:

        return

@client.command()
async def dummy(ctx):
    await ctx.channel.purge(limit=1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
client.run(TOKEN)
