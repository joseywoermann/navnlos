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
status = cycle(['$help'])


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_ready():
    change_status.start()
    print('Active')


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command(aliases=['h'])
async def help(ctx):
    author = ctx.message.author
    help_embed = discord.Embed(title="Commands", description="Eine Uebersicht ueber alle Commands.", colour=discord.Color.gold())
    help_embed.add_field(name="$invite/$inv", value="Sendet einen Invite-Link")
    help_embed.add_field(name="$question/$q", value="Stelle eine ja/nein-Frage, die dir der Bot beantwortet.")
    help_embed.add_field(name="$ping/$p", value="Gibt den Ping des Bots aus.")
    help_embed.add_field(name="$info/$i", value="Gibt Information ueber den Bot aus.")
    help_embed.add_field(name="$changelog/$cl", value="Zeigt Aenderungen, die mit dem letzten Update kamen.")
    help_embed.add_field(name="$time/$z", value="Gibt die aktuelle Zeit aus.")
    help_embed.add_field(name="$day/$t", value="Gibt das aktuelle Datum aus.")
    help_embed.add_field(name="$help/$h", value="Das muss ich nicht erklaeren, du hast es ja schon herausgefunden!")
    help_embed.add_field(name="$repeat/$rep", value="Wiederholt deine Nachricht in Form eines Embeds.")

    await ctx.channel.purge(limit=1)
    await author.send(content=None, embed=help_embed)


@client.command(aliases=['mh'])
@commands.has_permissions(manage_messages=True)
async def modhelp(ctx):
    author = ctx.message.author
    help_embed = discord.Embed(title="Commands exklusiv fuer Moderatoren", colour=discord.Color.gold())
    help_embed.add_field(name="$clear/$c", value="Loescht die angegebene Anzahl an Nachrichten, angepinnte Nachrichten ausgenommen. Wenn nach der Anzahl der Nachrichten \"pin\" angehaengt wird, werden angepinnte Nachrichten auch geloescht. Beispiel: `$clear 100 pin`")
    help_embed.add_field(name="$kick/$k", value="Kickt einen User vom Server. Moderatoren und Admins koennen nicht gekickt werden. Beispiel: `$kick @jcw05`")
    help_embed.add_field(name="$ban/$b", value="Bannt einen User vom Server. Moderatoren und Admins koennen nicht gebannt werden.")
    help_embed.add_field(name="$unban/$ub", value="Entbannt einen User. Beispiel: `$unban jcw05#1331`")
    help_embed.add_field(name="$addrole/$ar", value="Gibt einem User eine spezifische Rolle. Beispiel: `$addrole @jcw05 Pustekuchen`")
    help_embed.add_field(name="$removerole/$rr", value="Entfernt einem User eine spezifische Rolle. Beispiel: `$removerole @jcw05 Pustekuchen`")
    help_embed.add_field(name="$slomo", value="Setzt den entsprechenden Kanal in einen Slow-Modus. Anwendung: `$slomo 60` setzt den Slow-Modus auf 1 Minute. `$slomo 0`entfernt ihn.")
    help_embed.add_field(name="$channeledit/$edit", value="Aendert den Namen/dei Beschreibung des Channels. Anwendung: `$channeledit topic whatever /$channeledit name irgendwas`")
    help_embed.add_field(name="$nickedit/$nick", value="Aendert den Nickname eines Users, der eine niedrigere Rolle hat als der Bot. Anwendung: `$nickedit @hanspeter Dosenravioli`")

    await ctx.channel.purge(limit=1)
    await author.send(content=None, embed=help_embed)


@client.command()
async def dirhelp(ctx):
    help_embed = discord.Embed(title="Commands", description="Eine Uebersicht ueber alle Commands.", colour=discord.Color.gold())
    help_embed.add_field(name="$invite/$inv", value="Sendet einen Invite-Link")
    help_embed.add_field(name="$question/$q", value="Stelle eine ja/nein-Frage, die dir der Bot beantwortet.")
    help_embed.add_field(name="$ping/$p", value="Gibt den Ping des Bots aus.")
    help_embed.add_field(name="$info/$i", value="Gibt Information ueber den Bot aus.")
    help_embed.add_field(name="$changelog/$cl", value="Zeigt Aenderungen, die mit dem letzten Update kamen.")
    help_embed.add_field(name="$time/$z", value="Gibt die aktuelle Zeit aus.")
    help_embed.add_field(name="$day/$t", value="Gibt das aktuelle Datum aus.")
    help_embed.add_field(name="$help/$h", value="Das muss ich nicht erklaeren, du hast es ja schon herausgefunden!")
    help_embed.add_field(name="$repeat/$rep", value="Wiederholt deine Nachricht in Form eines Embeds.")

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=help_embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def moddirhelp(ctx):
    help_embed = discord.Embed(title="Commands exklusiv fuer Moderatoren", colour=discord.Color.gold())
    help_embed.add_field(name="$clear/$c", value="Loescht die angegebene Anzahl an Nachrichten, angepinnte Nachrichten ausgenommen. Wenn nach der Anzahl der Nachrichten \"pin\" angehaengt wird, werden angepinnte Nachrichten auch geloescht. Beispiel: `$clear 100 pin`")
    help_embed.add_field(name="$kick/$k", value="Kickt einen User vom Server. Moderatoren und Admins koennen nicht gekickt werden. Beispiel: `$kick @jcw05`")
    help_embed.add_field(name="$ban/$b", value="Bannt einen User vom Server. Moderatoren und Admins koennen nicht gebannt werden.")
    help_embed.add_field(name="$unban/$ub", value="Entbannt einen User. Beispiel: `$unban jcw05#1331`")
    help_embed.add_field(name="$addrole/$ar", value="Gibt einem User eine spezifische Rolle. Beispiel: `$addrole @jcw05 Pustekuchen`")
    help_embed.add_field(name="$removerole/$rr", value="Entfernt einem User eine spezifische Rolle. Beispiel: `$removerole @jcw05 Pustekuchen`")
    help_embed.add_field(name="$slomo", value="Setzt den entsprechenden Kanal in einen Slow-Modus. Anwendung: `$slomo 60` setzt den Slow-Modus auf 1 Minute. `$slomo 0`entfernt ihn.")
    help_embed.add_field(name="$channeledit/$edit", value="Aendert den Namen/dei Beschreibung des Channels. Anwendung: `$channeledit topic whatever /$channeledit name irgendwas`")
    help_embed.add_field(name="$nickedit/$nick", value="Aendert den Nickname eines Users, der eine niedrigere Rolle hat als der Bot. Anwendung: `$nickedit @hanspeter Dosenravioli`")

    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=help_embed)


@client.command(aliases=['i', 'about'])
async def info(ctx):
    info_embed = discord.Embed(title="Information", description="Version 1.3.1 by jcw05#1331", color=discord.Color.lighter_grey())
    info_embed.set_footer(text="Das hier ist das Kleingedruckte")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=info_embed)


@client.command(aliases=['cl'])
async def changelog(ctx):
    changelog_embed = discord.Embed(title="Changelog fuer Version 1.3.1", description="-Bugfixes", color=discord.Color.lighter_grey())
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=changelog_embed)



@client.command(aliases=['q'])
async def question(ctx, *, question):
    response = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Unwahrscheinlich']
    response_embed = discord.Embed(title="Auf die Frage \"" + str(question) + "\" ist die Antwort: " + str(random.choice(response)), color=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=response_embed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['inv'])
async def invite(ctx):
    invite_embed = discord.Embed(title="#Link hier einfuegen#", color=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=invite_embed)


@client.command(aliases=['rep'])
async def repeat(ctx, *, text):
    repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())
    repeat_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=repeat_embed)



@client.command(aliases=['z'])
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%H:%M")
    message = f"Es ist {current_time} Uhr."
    time_embed = discord.Embed(title=message, color=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=time_embed)



@client.command(aliases=['t'])
async def day(ctx):
    current_day = datetime.datetime.now().strftime("%d. %m. %Y, das ist der %j -ste Tag in diesem Jahr")
    message = f"Es ist der {current_day} ."
    day_embed = discord.Embed(title=str(message), color=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=day_embed)



@client.command(aliases=['d'])
async def dice(ctx, arg=6):
    dice_result = random.randint(1, arg)
    dice_embed = discord.Embed(title=dice_result, color=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=dice_embed)



@client.command(aliases=['p'])
async def ping(ctx):
    ping_embed = discord.Embed(title=f"Pong! {round(client.latency * 1000)}ms", colour=discord.Color.gold())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=ping_embed)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount_typed=1, arg=' '):
    clear_embed = discord.Embed(title=str(amount_typed) + " Nachricht(en) wurden geloescht.", color=discord.Color.dark_red())
    clear_pin_embed = discord.Embed(title=str(amount_typed) + " Nachricht(en) wurden geloescht.", color=discord.Color.dark_red())
    clear_overflow_embed = discord.Embed(title="Du darfst maximal 1000 Nachrichten gleichzeitig loeschen.")
    amount = amount_typed + 1
    if amount <= 1001:
        if arg == 'pin':
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=clear_pin_embed)
            time.sleep(1)
            await ctx.channel.purge(limit=1)


        else:
            await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)
            await ctx.send(embed=clear_embed)
            time.sleep(1)
            await ctx.channel.purge(limit=1)



    else:
        await ctx.send(content=None, embed=clear_overflow_embed)
        time.sleep(1)
        await ctx.channel.purge(limit=2)



@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, person: discord.Member, *, reason=None):
    kick_embed = discord.Embed(title=str(person) + " wurde gekickt.", colour=discord.Color.dark_red())
    kick_error_embed = discord.Embed(title="User konnte nicht gekickt werden.", colour=discord.Color.dark_purple())
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
    ban_error_embed = discord.Embed(title="User konnte nicht gebannt werden", color=discord.Color.dark_purple())
    await ctx.channel.purge(limit=1)
    try:
        await person.ban(reason=reason)
        await ctx.send(content=None, embed=ban_embed)


    except:
        await ctx.send(content=None, embed=ban_error_embed)
        sleep(5)
        await ctx.channel.purge(limit=1)



@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    unban_embed = discord.Embed(title=str(member) + " wurde entbannt.", color=discord.Color.dark_red())
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
                pass#errormessage einfuegen
        else:
            pass
            
    elif thing == "topic":
        if newattribut:
            try:
                await ctx.channel.edit(topic=newattribut)
            except:
                pass#errormessage einfuegen
        else:
            pass       
   
    else:
        pass#errormessage einfuegen


@client.command()
@commands.has_permissions(manage_channels=True)
async def slomo(ctx, delay):
    slomo_embed = discord.Embed(title="Slowmode auf " + str(delay) + " Sekunden gesetzt.", color=discord.Color.dark_red())
    await ctx.channel.purge(limit=1)
    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.send(content=None, embed=slomo_embed)



@client.command(aliases=['ar'])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, person: discord.Member, role):
    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    addrole_embed = discord.Embed(title="Rolle " + str(roles) + " zu " + str(person) + " hinzugefuegt")
    await ctx.channel.purge(limit=1)
    try:
        await person.add_roles(roles)
        await ctx.send(content=None, embed=addrole_embed)

    except:
        return


@client.command(aliases=['rr'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, person: discord.Member, role):
    guild = ctx.message.guild
    roles = discord.utils.get(guild.roles, name=role)
    removerole_embed = discord.Embed(title="Rolle " + str(roles) + " von " + str(person) + " entfernt")
    await ctx.channel.purge(limit=1)
    try:
        await person.remove_roles(roles)
        await ctx.send(content=None, embed=removerole_embed)

    except:
        return
        
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command(aliases=['arep'])
@commands.has_permissions(manage_messages=True)
async def anonymrepeat(ctx, *, text):
    repeat_embed = discord.Embed(title=str(text), color=discord.Color.orange())
    await ctx.channel.purge(limit=1)
    await ctx.send(content=None, embed=repeat_embed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

client.run('#TOKEN HIER EINFÜGEN#')