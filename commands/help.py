import discord
from discord.ext import commands
import logging

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx, arg = None):

        await ctx.channel.purge(limit=1)

        if arg == None:

            help_embed = discord.Embed(title="Commands", colour=discord.Color.gold())
            help_embed.add_field(name="$invite", value="Invitelink zum MisteriCraft-Communityserver")
            help_embed.add_field(name="$question", value="Beantwortet Ja/Nein-Fragen")
            help_embed.add_field(name="$ping", value="Latenz des Bots")
            help_embed.add_field(name="$info", value="Bot-Information")
            help_embed.add_field(name="$changelog", value="Zeigt den Changelog")
        #    help_embed.add_field(name="$time/$z", value="Gibt die aktuelle Zeit aus.")
            help_embed.add_field(name="$day", value="Gibt das aktuelle Datum an")
            help_embed.add_field(name="$help", value="Selbsterklaerend")
            help_embed.add_field(name="$repeat", value="Sendet deine Nachricht als Embed")
            help_embed.add_field(name="$poll", value="Umfrage mit bis zu 9 Antworten. Woerter mit `_` trennen: `$poll Ja? Ja Definitiv_nicht`")
            help_embed.add_field(name="$wiki", value="Wikipedia-Suche")
            help_embed.add_field(name="$price", value="Preisvergleich für angegebenes Produkt")
            help_embed.add_field(name="$define", value="Definiert ein Wort")
            help_embed.add_field(name="$bpm", value="Tempo fuer einen angegebenen Song")
            help_embed.add_field(name="$dummy", value="Tut absolut garnichts")
            help_embed.add_field(name="$userinfo", value="Zeigt informationen ueber einen User")
            help_embed.add_field(name="$developer", value="Informationen ueber den Entwickler dieses Bots.")
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

def setup(client):
    client.add_cog(Help(client))
