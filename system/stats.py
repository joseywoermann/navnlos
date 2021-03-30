import discord
from discord.ext import commands
import logging

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["stats"])
    @commands.guild_only()
    async def info(self, ctx):

        async with ctx.channel.typing():

            appinfo = await self.client.application_info()

            info_embed = discord.Embed(title="Information", color=0x75e8ee)
            info_embed.add_field(name = "Current version:", value = "`V 2.2.0`")
            info_embed.add_field(name = "👑 Bot Owner:", value = f"{appinfo.owner.mention}")
            info_embed.add_field(name = "📦 Used packages:", value = "`29`")
            info_embed.add_field(name = "📃 Lines of code:", value = "`1954`")
            info_embed.add_field(name = "Commands:", value = f"`{len(self.client.commands)}`")
            info_embed.add_field(name = "🖥️ Servers:", value = f"`{len(self.client.guilds)}`")
            info_embed.add_field(name = "Users:", value = f"`{len(self.client.users)}`")
            info_embed.add_field(name = "🗨️ Cached messages:", value = f"`{len(self.client.cached_messages)}`")
            info_embed.set_thumbnail(url = "https://raw.githubusercontent.com/joseywoermann/navnlos/master/navnlos_icon_tr.PNG")
            info_embed.set_footer(text = "$stats | @navnløs")

        await ctx.reply(embed=info_embed)

def setup(client):
    client.add_cog(Info(client))
