import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from main import test_guilds, make_error_embed
from discord_slash.utils.manage_commands import create_option

options = [
    create_option(
        name = "member",
        description = "Who do you want to move?",
        option_type = 6,
        required = True
    )
]

class MoveHere(commands.Cog):

    def __init__(self, client):
        self.client = client
    """
    TODO: FIX PERMISSION CHECK
    """
    @cog_ext.cog_slash(name = "move", description = "Move a member into your voicechannel", options = options, guild_ids = test_guilds)
    @commands.has_permissions(manage_messages = True)
    async def _move(self, ctx: SlashContext, member: discord.Member):
        embed = await MoveHere.make(self, ctx, member)
        await ctx.send(embed = embed)


    async def make(self, ctx, member):
        try:

            #if ctx.message.author.
            if ctx.author.voice is None:
                embed = discord.Embed(
                    title = "You have to be connected to a voice channel!"
                )

            else:
                target_channel = ctx.author.voice.channel
                if member.voice is None:
                    embed = discord.Embed(
                        title = "The targeted member is not connected to a voice channel!"
                    )

                else:
                    await member.move_to(
                        target_channel,
                        reason = f"{ctx.author} executed \"$move {member}\""
                    )
                    embed = discord.Embed(
                        title = discord.Embed.Empty,
                        description = f"Moved {member.mention} to **{target_channel}**."
                    )

        except Exception as e:
            embed = await make_error_embed(e)
        finally:
            return embed

def setup(client):
    client.add_cog(MoveHere(client))
