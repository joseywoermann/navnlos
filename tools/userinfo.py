import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option
import datetime

options = [
    create_option(
        name = "user",
        description = "Select a user",
        option_type = 6,
        required = False
    )
]

class UserInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def resolve_status(member):
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

    
    async def calculate_member_age(member):
        now = datetime.datetime.now()
        join_date = member.created_at
        account_age = now - join_date
        account_age_final = str(account_age)[:-7]
        return account_age_final

    async def calculate_member_join_age(member):
        now = datetime.datetime.now()
        server_join_date = member.joined_at
        server_join_age = now - server_join_date
        server_join_age_final = str(server_join_age)[:-7]
        return server_join_age_final

    @cog_ext.cog_slash(name = "whois", description = "Get information about a user", options = options, guild_ids = test_guilds)
    async def _userinfo(self, ctx: SlashContext, user: discord.Member = None):
        if user is None:
            user = ctx.author
            print(user)
        else:
            print(user)

        embed = await UserInfo.make(self, ctx, user)
        await ctx.send(embed=embed)


    async def make(self, ctx, person):
        try:
            rollen = ""
            toprole = ""

            for role in reversed(person.roles):
                if not role.is_default():
                    rollen += f"{role.mention} \r\n"
                if role == person.top_role:
                    toprole += f"{role.mention} \r\n"

            person_status = await UserInfo.resolve_status(person)
            account_age =  await UserInfo.calculate_member_age(person)
            server_join_age = await UserInfo.calculate_member_join_age(person)

            embed = discord.Embed(title=str(person), color = 0x75e8ee)
            embed.add_field(name="Server join date: ", value=person.joined_at.strftime("%d.%m.%Y at %H:%M:%S"))
            embed.add_field(name="Account created on: ", value=person.created_at.strftime("%d.%m.%Y at %H:%M:%S"))
            embed.add_field(name="Status", value=person_status)
            embed.add_field(name="ID", value=str(person.id))
            embed.add_field(name="Account-age:", value=f"{account_age} hours")
            embed.add_field(name="Member of the server for:", value=f"{server_join_age} hours")

            if rollen:
                if len(rollen) > 50:
                    embed.add_field(name = "Roles:", value = "Too many to display")
                else:
                    embed.add_field(name="Roles:", value=rollen)

            if toprole:
                embed.add_field(name="Highest role:", value=toprole)

            embed.set_thumbnail(url=person.avatar_url)

        except Exception as e:
            embed = await make_error_embed(e)

        finally:
            return embed
def setup(client):
    client.add_cog(UserInfo(client))
