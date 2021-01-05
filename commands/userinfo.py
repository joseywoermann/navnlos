import discord
from discord.ext import commands
import logging

class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, person: discord.Member):

        rollen = ''
        for role in person.roles:
            if not role.is_default():
                rollen += '{} \r\n'.format(role.mention)


        userinfo_embed = discord.Embed(title=str(person))
        userinfo_embed.add_field(name="Joined am", value=person.joined_at.strftime("%d.%m.%Y um %H:%M:%S"))
        userinfo_embed.add_field(name="Joined Discord am:", value=person.created_at.strftime("%d.%m.%Y um %H:%M:%S"))
        userinfo_embed.add_field(name="Status", value=str(person.status))
        userinfo_embed.add_field(name="Rollen", value=rollen)
        userinfo_embed.add_field(name="ID", value=str(person.id))
        userinfo_embed.add_field(name="top role", value=person.top_role)
        #userinfo_embed.add_field(name="Nitro", value=str(person.nitro))
        userinfo_embed.set_thumbnail(url=person.avatar_url)

        await ctx.channel.purge(limit=1)
        await ctx.send(content=None, embed=userinfo_embed)

def setup(client):
    client.add_cog(UserInfo(client))
