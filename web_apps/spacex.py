import discord
from discord.ext import commands
import requests


class SpaceX(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.base_url = "https://api.spacexdata.com/v4/"

  

  @commands.command()
  @commands.guild_only()
  async def nextlaunch(self, ctx):

    r = requests.get(f"{self.base_url}launches/next")
    data = r.json()
    #print(data)

    embed = discord.Embed(title = "Next SpaceX launch")
    
    embed.add_field(
      name="aee",
      value=data["payloads"]["name"]
    )
    embed.set_thumbnail(url = data["links"]["patch"]["large"])

    await ctx.reply(embed = embed)


def setup(client):
  client.add_cog(SpaceX(client))
