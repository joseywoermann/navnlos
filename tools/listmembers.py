import discord
from discord.ext import commands
import logging

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def hasrole(self, ctx, *, role_name_or_id):

        async with ctx.channel.typing():
            server = ctx.guild

            # If role_name_or_id is a mention, make it to a role-name
            if role_name_or_id.startswith("<@&") and role_name_or_id.endswith(">"):
                role_name_or_id = role_name_or_id.replace('<@&', '')
                role_name_or_id = role_name_or_id.replace('>', '')

            target_role = discord.utils.find(lambda r: r.name == str(role_name_or_id), server.roles)

            # if an ID is specified, check for IDs
            if target_role is None:
                try:
                    target_role = discord.utils.find(lambda r: r.id == int(role_name_or_id), server.roles)
                except:
                    pass

            # role not found
            if target_role is None:
                embed = discord.Embed(title = f"Specified role \"{role_name_or_id}\" not found:")
                await ctx.reply(content = None, embed = embed)

            else:
                members = []
                for member in server.members:
                    if target_role in member.roles:
                        members.append('{}'.format(member.mention))

                embed = discord.Embed(title = "Users with this role:", description = ',\n'.join(members))
                await ctx.reply(content = None, embed = embed)

def setup(client):
    client.add_cog(Invite(client))
