import discord
from discord.ext import commands
import logging

import datetime

class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, person: discord.Member):

        rollen = ""
        toprole = ""

        for role in reversed(person.roles):
            if not role.is_default():
                rollen += '{} \r\n'.format(role.mention)
            if role == person.top_role:
                toprole += '{} \r\n'.format(role.mention)


        # status
        if str(person.status) == "online":
            person_status = "🟢 - ONLINE"
        elif str(person.status) == "idle":
            person_status = "🟡 - ABWESEND"
        elif str(person.status) == "dnd":
            person_status = "🔴 - DO NOT DISTURB"
        elif str(person.status) == "offline":
            person_status = "🌑 - OFFLINE"
        else:
            print(person.status)
            person_status = "test"


        # account-age
        now = datetime.datetime.now()
        join_date = person.created_at
        account_age = now - join_date


        # server-age
        now = datetime.datetime.now()
        server_join_date = person.joined_at
        server_join_age = now - server_join_date

        userinfo_embed = discord.Embed(title=str(person), color = 0x75e8ee)
        userinfo_embed.add_field(name="Dem Server beigetreten am: ", value=person.joined_at.strftime("%d.%m.%Y um %H:%M:%S"))
        userinfo_embed.add_field(name="Account erstellt am: ", value=person.created_at.strftime("%d.%m.%Y um %H:%M:%S"))
        userinfo_embed.add_field(name="Status", value=person_status)
        userinfo_embed.add_field(name="ID", value=str(person.id))
        userinfo_embed.add_field(name="Account-Alter:", value=account_age)
        userinfo_embed.add_field(name="Auf dem Server seit:", value=server_join_age)

        if rollen:
            userinfo_embed.add_field(name="Rollen", value=rollen)

        if toprole:
            userinfo_embed.add_field(name="Höchste Rolle", value=toprole)

        userinfo_embed.set_thumbnail(url=person.avatar_url)

        await ctx.reply(content=None, embed=userinfo_embed)

def setup(client):
    client.add_cog(UserInfo(client))
