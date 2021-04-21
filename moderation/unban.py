import discord
from discord.ext import commands

class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self, ctx, *, member):

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        unban_embed = discord.Embed(title=f"Removed ban from {member}.", color=discord.Color.dark_red())
        unban_embed.set_footer(text = "$unban | @navnløs")

        for ban_entry in banned_users:

            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):

                try:
                    await ctx.guild.unban(user)
                    await ctx.reply(content=None, embed=unban_embed)

                except:
                    return


def setup(client):
    client.add_cog(Unban(client))
