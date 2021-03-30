import discord
from discord.ext import commands
import logging
from asyncio import sleep

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['c'])
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, amount_typed=1):

        clear_overflow_embed = discord.Embed(title="The bot can only delete up to 2000 messages at once!")

        amount = amount_typed + 1

        if amount <= 2000:
            deleted = await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)

            clear_embed = discord.Embed(title=f'Deleted {len(deleted)-1} messages.', color=discord.Color.dark_red())
            clear_embed.set_footer(text = "$clear | @navnløs")

            msg = await ctx.send(embed=clear_embed)
            await sleep(2)
            await msg.delete()

        else:
            await ctx.reply(content=None, embed=clear_overflow_embed)

def setup(client):
    client.add_cog(Clear(client))
