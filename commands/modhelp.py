import discord
from discord.ext import commands
import logging

class ModHelp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def modhelp(self, ctx):

        help_embed = discord.Embed(title="Commands exklusiv fuer Moderatoren", colour=discord.Color.gold())
        help_embed.add_field(name="$clear", value="Loescht die angegebene Anzahl an Nachrichten.")
        help_embed.add_field(name="$kick", value="Kickt einen User.")
        help_embed.add_field(name="$ban", value="Bannt einen User")
        help_embed.add_field(name="$banid", value="Bannt einen User mithilfe der ID. User, die nicht auf dem Server sind, koennen so gebannt werden.")
        help_embed.add_field(name="$unban", value="Entbannt einen User")
        help_embed.add_field(name="$addrole/$ar", value="Fuegt einem User eine Rolle hinzu")
        help_embed.add_field(name="$removerole/$rr", value="Entfernt einem User eine Rolle")
        help_embed.add_field(name="$slomo", value="Setzt den Slowmode fuer den Kannal auf die angegebene Sekundenzahl")
        help_embed.add_field(name="$channeledit", value="Aendert den Namen / Beschreibung eines Channels")
        help_embed.add_field(name="$nickedit", value="Aendert den Nickname eines Users")
        help_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(content=None, embed=help_embed)

def setup(client):
    client.add_cog(ModHelp(client))
