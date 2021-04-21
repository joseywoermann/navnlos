import discord
from discord.ext import commands

class CommandLogger(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        log_server = self.client.get_guild(737650747432501308)

        if message.content.startswith("$"):

            log_channel = discord.utils.get(log_server.text_channels, name=str(message.guild.id))

            log_embed = discord.Embed(title=message.content, description=f"Channel: **{message.channel.mention}** Channel-ID: [{message.channel.id}]")
            log_embed.set_author(name=f"{message.author} | {message.author.id}", icon_url=message.author.avatar_url)
            log_embed.set_footer(text=f"{message.created_at.strftime('%Y-%m-%d, %H:%M:%S')} UTC | Server: {str(message.channel.guild)}")

            await log_channel.send(content=None, embed=log_embed)

def setup(client):
    client.add_cog(CommandLogger(client))
