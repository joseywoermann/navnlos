from discord.ext import commands

class MoveAll(commands.Cog):

    def __init__(self, client):
        self.client = client
    """
    def in_vc():
        def precidate(ctx):
            return ctx.author.voice and ctx.author.voice.channel
        return check(precidate)

    @in_vc()
    @commands.command()
    @commands.guild_only()
    async def moveall(self, ctx, *, target_channel: discord.VoiceChannel):
        vc_members = ctx.author.voice.channel.members
        for member in vc_members:
            await member.move_to(target_channel)

    """



def setup(client):
    client.add_cog(MoveAll(client))
