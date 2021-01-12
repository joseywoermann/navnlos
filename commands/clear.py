import discord
from discord.ext import commands
import logging
from time import sleep

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, amount_typed=1, arg=' '):

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

            else:
                deleted = await ctx.channel.purge(limit=amount, check=lambda msg: not msg.pinned)

                clear_embed = discord.Embed(title='{} Nachrichten geloescht.'.format(len(deleted)-1), color=discord.Color.dark_red())
                clear_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                await ctx.send(embed=clear_embed)
                sleep(1)

        else:
            await ctx.reply(content=None, embed=clear_overflow_embed)
            sleep(1)

def setup(client):
    client.add_cog(Clear(client))
