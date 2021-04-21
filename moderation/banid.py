import discord
from discord.ext import commands
from time import sleep

class BanID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def banid(self, ctx, user_id, *, reason=None):
        user = await self.client.fetch_user(user_id)
        ban_embed = discord.Embed(title="Banned the following user:", description = f"{user.mention}", color=discord.Color.dark_red())
        ban_embed.set_footer(text = "$banid | @navnløs")

        ban_error_embed = discord.Embed(title="User couldn't be banned.", color=discord.Color.dark_purple())

        user = await self.client.fetch_user(user_id)

        try:
            await ctx.guild.ban(user, reason=reason)
            await ctx.reply(content=None, embed=ban_embed)

        except:
            await ctx.reply(content=None, embed=ban_error_embed)
            sleep(5)


def setup(client):
    client.add_cog(BanID(client))
