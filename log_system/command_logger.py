import discord
from discord.ext import commands
from discord_slash import SlashContext
import logging


class CommandLogger(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        log_server = self.client.get_guild(737650747432501308)

        if message.content.startswith("$"):

            log_channel = discord.utils.get(
                log_server.text_channels,
                name=str(message.guild.id)
            )

            embed = discord.Embed(
                title=message.content,
                description=f"Channel: **{message.channel.mention}** Channel-ID: [{message.channel.id}]"
            )

            embed.set_author(
                name=f"{message.author} | {message.author.id}",
                icon_url=message.author.avatar_url
            )

            embed.set_footer(
                text=f"{message.created_at.strftime('%Y-%m-%d, %H:%M:%S')} UTC | Server: {str(message.channel.guild)}"
            )

            await log_channel.send(content=None, embed=embed)

    @commands.Cog.listener()
    async def on_slash_command(self, ctx: SlashContext):
        logging.info(f"COMMAND_EXECUTION: {ctx.author} used /{ctx.command}")

        log_server = self.client.get_guild(737650747432501308)


        log_channel = discord.utils.get(
            log_server.text_channels,
            name=str(ctx.guild.id)
        )

        embed = discord.Embed(
            title=f"/{ctx.command}",
            description=f"Channel: **{ctx.channel.mention}** Channel-ID: [{ctx.channel.id}]"
        )

        embed.set_author(
            name=f"{ctx.author} | {ctx.author.id}",
            icon_url=ctx.author.avatar_url
        )

        embed.set_footer(
            #text=f"{ctx.created_at.strftime('%Y-%m-%d, %H:%M:%S')} UTC | Server: {str(ctx.channel.guild)}"
            text=f"Server: {str(ctx.channel.guild)}"
        )

        await log_channel.send(content=None, embed=embed)

def setup(client):
    client.add_cog(CommandLogger(client))
