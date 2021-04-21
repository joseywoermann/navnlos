import discord
from discord.ext import commands
from time import sleep

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, person: discord.Member, *, reason=None):

        ban_embed = discord.Embed(title="Banned the following user:", description = f"{person.mention}", color=discord.Color.dark_red())
        ban_embed.set_footer(text = "$ban | @navnløs")

        ban_error_embed = discord.Embed(title="User couldn't be banned.", color=discord.Color.dark_purple())

        try:
            await person.ban(reason=reason)
            await ctx.reply(content=None, embed=ban_embed)

        except:
            await ctx.reply(content=None, embed=ban_error_embed)
            sleep(5)

def setup(client):
    client.add_cog(Ban(client))
