"""
A command that moves a member into your current vc
$movehere @mention
"""
import discord
from discord.ext import commands

class MoveHere(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["movehere"])
    @commands.has_permissions(move_members = True)
    @commands.guild_only()
    async def move(self, ctx, target_member: discord.Member):

        if ctx.author.voice is None:

            move_embed = discord.Embed(title = "You have to be connected to a voice channel!")
            await ctx.reply(embed = move_embed)

        else:
            target_channel = ctx.author.voice.channel
            
            if target_member.voice is None:
                move_embed = discord.Embed(title = "The targeted member is not connected to a voice channel!")
                await ctx.reply(embed = move_embed)

            else:
                await target_member.move_to(target_channel, reason = f"{ctx.author} executed \"$move {target_member}\"")
                move_embed = discord.Embed(title = " ", description = f"Moved {target_member.mention} to **{target_channel}**.")
                await ctx.reply(embed = move_embed)

def setup(client):
    client.add_cog(MoveHere(client))
