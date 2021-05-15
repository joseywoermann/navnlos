import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "message",
        description = "What do you want to send?",
        option_type = 3,
        required = True
    ),
    create_option(
        name = "serverid",
        description = "Which server do you want to send the message to?",
        option_type = 3,
        required = False
    ),
    create_option(
        name = "channelid",
        description = "Whhich channel do you want to send the message to?",
        option_type = 3,
        required = False
    )
]



class BotChat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, message, serverid = None, channelid = None):
        if serverid is None or channelid is None:
            await BotChat.make(self, ctx, message, ctx.guild.id, ctx.channel.id)
        else:
            await BotChat.make(self, ctx, message, int(serverid), int(channelid))


    @cog_ext.cog_slash(name = "say", description = "Make the bot say stuff.", options = options, guild_ids = test_guilds)
    @commands.is_owner()
    @commands.guild_only()
    async def _say(self, ctx: SlashContext, message, serverid = None, channelid = None):
        if serverid and channelid:
            await BotChat.make(self, ctx, message, int(serverid), int(channelid))
        else:
            await BotChat.make(self, ctx, message, None, None)


    async def make(self, ctx, message, serverid, channelid):
        try:
            if serverid and channelid:
                target = self.client.get_guild(int(serverid)).get_channel(int(channelid))
                await target.send(message)

                if channelid == ctx.channel.id:
                    pass
                else:
                    embed = discord.Embed(
                        title = f"Success!",
                        description = f"Sent **{message}** to **{target.mention}** on **{self.client.get_guild(int(serverid)).name}**."
                    )
                    await ctx.send(embed = embed)

            else:
                await ctx.send(message)

        except Exception as e:
            await ctx.send(embed = await make_error_embed(e))

def setup(client):
    client.add_cog(BotChat(client))
