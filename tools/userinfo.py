import discord
from discord.ext import commands

import datetime

class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client



    def resolve_status(member):
        if str(member.status) == "online":
            person_status = "🟢 - ONLINE"
        elif str(member.status) == "idle":
            person_status = "🟡 - IDLE"
        elif str(member.status) == "dnd":
            person_status = "🔴 - DO NOT DISTURB"
        elif str(member.status) == "offline":
            person_status = "🌑 - OFFLINE"
        else:
            person_status = "Could not get the user's status information.\nPlease inform `jcw05#1331` or make a bugreport using `$bugreport`."
        return person_status

    def calculate_member_age(member):
        now = datetime.datetime.now()
        join_date = member.created_at
        account_age = now - join_date
        account_age_final = str(account_age)[:-7]
        return account_age_final

    def claculate_member_join_age(member):
        now = datetime.datetime.now()
        server_join_date = member.joined_at
        server_join_age = now - server_join_date
        server_join_age_final = str(server_join_age)[:-7]
        return server_join_age_final

    @commands.command(aliases=['whois'])
    async def userinfo(self, ctx, person: discord.Member):

        async with ctx.channel.typing():
            rollen = ""
            toprole = ""

            for role in reversed(person.roles):
                if not role.is_default():
                    rollen += '{} \r\n'.format(role.mention)
                if role == person.top_role:
                    toprole += '{} \r\n'.format(role.mention)

            person_status = UserInfo.resolve_status(person)
            account_age = UserInfo.calculate_member_age(person)
            server_join_age = UserInfo.claculate_member_join_age(person)


            userinfo_embed = discord.Embed(
                title=str(person), color = 0x75e8ee
            )

            userinfo_embed.add_field(
                name="Server join date: ",
                value=person.joined_at.strftime("%d.%m.%Y at %H:%M:%S")
            )

            userinfo_embed.add_field(
                name="Account created on: ",
                value=person.created_at.strftime("%d.%m.%Y at %H:%M:%S")
            )

            userinfo_embed.add_field(
                name="Status",
                value=person_status
            )

            userinfo_embed.add_field(
                name="ID",
                value=str(person.id)
            )

            userinfo_embed.add_field(
                name="Account-age:",
                value=f"{account_age} hours"
            )

            userinfo_embed.add_field(
                name="Member of the server for:",
                value=f"{server_join_age} hours"
            )


            if rollen:
                userinfo_embed.add_field(name="Roles:", value=rollen)

            if toprole:
                userinfo_embed.add_field(name="Highest role:", value=toprole)

            userinfo_embed.set_thumbnail(url=person.avatar_url)
            userinfo_embed.set_footer(text = "$whois | @navnløs")

        await ctx.reply(content=None, embed=userinfo_embed)

def setup(client):
    client.add_cog(UserInfo(client))
