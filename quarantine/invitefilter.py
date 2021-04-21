from discord.ext import commands

class InviteFilter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.guild.id == 304191437652623360:

            banned_links = ["discord.gg/", "discord.com/invite/"]
            server_invites = ["discord.gg/jM3JAKN", "discord.com/invite/jM3JAKN"]

            if any(word in message.content.lower() for word in banned_links):
                msg = message.content.lower()
                msg_words = msg.split()
                print(msg_words)

                if any(word in msg_words for word in server_invites):
                    pass
                else:
                    if "-embed" in msg_words:
                        pass
                    else:
                        await message.delete()
                        await message.channel.send("nope")
        else:
            pass



def setup(client):
    client.add_cog(InviteFilter(client))
