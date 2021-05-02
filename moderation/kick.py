import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, person: discord.Member, *, reason=None):

        kick_embed = discord.Embed(
            title = "Kicked the following user:",
            description = f"{person.mention}",
            colour=discord.Color.dark_red()
        )


        kick_embed.set_footer(text = "$kick | @navnløs")

        kick_error_embed = discord.Embed(title="User couldn't be kicked.", colour=discord.Color.dark_purple())

        try:
            await person.kick(reason=f"{reason} | kicked by {ctx.author}")
            await ctx.reply(content=None, embed=kick_embed)

        except:
            await ctx.reply(content=None, embed=kick_error_embed)

def setup(client):
    client.add_cog(Kick(client))
