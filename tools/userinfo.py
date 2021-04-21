import discord
from discord.ext import commands

import datetime

class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ui', 'whois'])
    async def userinfo(self, ctx, person: discord.Member):

        async with ctx.channel.typing():
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
                person_status = "🟡 - IDLE"
            elif str(person.status) == "dnd":
                person_status = "🔴 - DO NOT DISTURB"
            elif str(person.status) == "offline":
                person_status = "🌑 - OFFLINE"
            else:
                person_status = "Could not get the user's status information.\nPlease inform `jcw05#1331` or make a bugreport using `$report`."


            # account-age
            now = datetime.datetime.now()
            join_date = person.created_at
            account_age = now - join_date
            account_age_final = str(account_age)[:-7]


            # server-age
            now = datetime.datetime.now()
            server_join_date = person.joined_at
            server_join_age = now - server_join_date
            server_join_age_final = str(server_join_age)[:-7]

            userinfo_embed = discord.Embed(title=str(person), color = 0x75e8ee)
            userinfo_embed.add_field(name="Server join date: ", value=person.joined_at.strftime("%d.%m.%Y at %H:%M:%S"))
            userinfo_embed.add_field(name="Account created on: ", value=person.created_at.strftime("%d.%m.%Y at %H:%M:%S"))
            userinfo_embed.add_field(name="Status", value=person_status)
            userinfo_embed.add_field(name="ID", value=str(person.id))
            userinfo_embed.add_field(name="Account-age:", value=account_age_final + " hours")
            userinfo_embed.add_field(name="Member of the server for:", value=server_join_age_final + " hours")

            if rollen:
                userinfo_embed.add_field(name="Roles:", value=rollen)

            if toprole:
                userinfo_embed.add_field(name="Highest role:", value=toprole)

            userinfo_embed.set_thumbnail(url=person.avatar_url)
            userinfo_embed.set_footer(text = "$whois | @navnløs")

        await ctx.reply(content=None, embed=userinfo_embed)

def setup(client):
    client.add_cog(UserInfo(client))
