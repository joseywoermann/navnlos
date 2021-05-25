import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "info",
        description = "Show statistics",
        guild_ids = test_guilds
    )
    async def _info(self, ctx: SlashContext):
        embed = await Info.make(self, ctx)
        await ctx.send(embed=embed)


    async def make(self, ctx):
        try:

            channels_amount = 0
            for server in self.client.guilds:
                for channel in server.channels:
                    channels_amount = channels_amount + 1

            appinfo = await self.client.application_info()
            embed = discord.Embed(title="Information", color=0x75e8ee)
            embed.add_field(name = "Current version:", value = "`V 3.0.0`")
            embed.add_field(name = "Bot Owner:", value = f"{appinfo.owner.mention}")
            embed.add_field(name = "Written in:", value = "`discord.py`")
            embed.add_field(name = "Commands:", value = f"`{len(self.client.commands)}`")
            embed.add_field(name = "Servers:", value = f"`{len(self.client.guilds)}`")
            embed.add_field(name = "Channels:", value = f"`{channels_amount}`")
            embed.add_field(name = "Users:", value = f"`{len(self.client.users)}`")
            embed.add_field(name = "Cached messages:", value = f"`{len(self.client.cached_messages)}`")
            embed.set_thumbnail(url = "https://raw.githubusercontent.com/joseywoermann/navnlos/master/assets/icon.PNG")

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Info(client))
