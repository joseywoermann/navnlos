import discord
from discord.ext import commands
import logging

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['vc', 'voicechat', 'talk', 'vcusers', 'voicechatusers', 'invoicechat'])
    @commands.guild_only()
    async def invc(self, ctx):

        server = ctx.guild
        vc_role = discord.utils.find(lambda r: r.name == 'in voicechat', server.roles)

        vc_users = []

        for member in server.members:
            if vc_role in member.roles:
                vc_users.append('{}'.format(member.mention))

        vc_embed = discord.Embed(title = "Users in voice chats:", description = '\n'.join(vc_users))
        await ctx.reply(content = None, embed = vc_embed)

def setup(client):
    client.add_cog(Invite(client))
