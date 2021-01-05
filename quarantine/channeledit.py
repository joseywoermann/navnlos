import discord
from discord.ext import commands
import logging

class ChannelEdit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def channeledit(self, ctx, thing, *, newattribut):
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
            await ctx.send("Bitte \"name\" oder \"topic\" angeben."

def setup(client):
    client.add_cog(ChannelEdit(client))
