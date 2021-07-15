import discord
from discord.ext import commands
from asyncio import sleep
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option


options = [
    create_option(
        name = "count",
        description = "How many messages do you want to delete?",
        option_type = 4,
        required = False
    )
]

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name = "clear",
        description = "Delete up to 1000 messages in this channel, while ignoring pinned messages.",
        options = options,
        #guild_ids = test_guilds
    )
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def _clear(self, ctx: SlashContext, count = 1):
        await ctx.defer()
        embed = await Clear.make(self, ctx, count)
        await ctx.send(embed=embed, hidden=True)


    async def make(self, ctx, amount_typed):
        try:
            if amount_typed <= 1000:
                amount = amount_typed + 1

                deleted = await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)
                embed = discord.Embed(
                    title=f'Deleted {len(deleted)-1} messages.',
                    color=discord.Color.dark_red()
                )
            else:
                embed = await make_error_embed("You can only delete up to 1000 messages at once!")

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed

def setup(client):
    client.add_cog(Clear(client))
