from discord.ext import commands


class CommandFeedback(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        thumpsUpEmoji = "👍"

        if message.content.startswith("$"):
            await message.add_reaction(thumpsUpEmoji)

def setup(client):
    client.add_cog(CommandFeedback(client))
