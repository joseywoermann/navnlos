import discord
from discord.ext import commands
import logging
from time import sleep

class On_raw_reaction_add(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #print(payload.emoji.name)
        error_channel = self.client.get_channel(719996916674592768)
        message_id = payload.message_id

        if message_id == 721461113866289252:

            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'ls19':

                role = discord.utils.get(guild.roles, name='farmingsimulator')

            elif payload.emoji.name == 'minecraft':

                role = discord.utils.get(guild.roles, name='minecraft')

            elif payload.emoji.name == 'simunews':

                role = discord.utils.get(guild.roles, name='simulator')

            elif payload.emoji.name == 'funfacts':

                role = discord.utils.get(guild.roles, name='funfacts')

            elif payload.emoji.name == 'kaenguru':

                role = discord.utils.get(guild.roles, name='kaenguru')

            elif payload.emoji.name == 'epicdealz':

                role = discord.utils.get(guild.roles, name='epicgames')

            elif payload.emoji.name == 'redstonia':

                role = discord.utils.get(guild.roles, name='mistericraft')

            elif payload.emoji.name == 'notifier':

                role = discord.utils.get(guild.roles, name='kgh-updates')

            else:

                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:

                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

                if member is not None:

                    await  member.add_roles(role)

                else:

                    await error_channel.send("Rolemenu-Error: Member not found.")

            else:

                await error_channel.send("Rolemenu-Error: Role not found.")


        error_channel = self.client.get_channel(719996916674592768)
        message_id = payload.message_id

        if message_id == 722547238840172675:

            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'check':

                role = discord.utils.get(guild.roles, name='verifiziert')

            else:

                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:

                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

                if member is not None:

                    await  member.add_roles(role)

                else:

                    await error_channel.send("Rolemenu-Error: Member not found.")

            else:

                await error_channel.send("Rolemenu-Error: Role not found.")


def setup(client):
    client.add_cog(On_raw_reaction_add(client))
