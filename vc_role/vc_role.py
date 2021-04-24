import discord
from discord.ext import commands


class VC_role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        vc_role = discord.utils.get(member.guild.roles, name="in voicechat")

        if before.channel is None:
            await member.add_roles(vc_role)

        if after.channel is None:
            await member.remove_roles(vc_role)

def setup(client):
    client.add_cog(VC_role(client))
