import discord
from discord.ext import commands
import logging

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['h'])
    @commands.guild_only()
    async def help(self, ctx, arg = None):

        if arg == None:

            help_embed = discord.Embed(title="Commands accessible for everyone:", colour=0x75e8ee)
            help_embed.add_field(name="$shorturl <`link that you want to shorten`>", value="turns your long link into a short one.")
            help_embed.add_field(name="$qrcode <`link`>", value="Creates a QR-code.")
            help_embed.add_field(name="$info", value="Some navnløs-statistics")
            help_embed.add_field(name="$hasrole <`role-name OR @role-mention OR role-ID`>", value="All members that have this role")
            help_embed.add_field(name="$voicechat", value="All members currently in a voicechat")
            help_embed.add_field(name="$support", value="Invitation to the official support server")
            help_embed.add_field(name="$invite", value="A link to invite navnløs")
            help_embed.add_field(name="$question", value="Let the bot answer your Yes/No - questions")
            help_embed.add_field(name="$ping", value="The latency of navnløs")
            help_embed.add_field(name="$changelog", value="Shows the latest changelog")
            help_embed.add_field(name="$day", value="Shows the current day (Point of reference: UTC+0 [London time])")
            help_embed.add_field(name="$help <`command`>", value="Shows usage of any command. (Example: `$help embed`)")
            help_embed.add_field(name="$embed <`text`>", value="Puts you message into a beautiful embed.")
            help_embed.add_field(name="$poll <`question`> <`answers`>", value="Creates a basic poll with up to 9 possible answers. See `$help poll` for usage.")
            help_embed.add_field(name="$wiki <`query`>", value="Searches Wikipedia for a matching article")
            help_embed.add_field(name="$price <`query`>", value="Brings you to [Geizhals](https://geizhals.eu/) where you can check the price for you item")
            help_embed.add_field(name="$define <`query`>", value="Looks up any word on [urnbandictionary](https://urbandictionary.com)")
            help_embed.add_field(name="$dummy", value="Does absolutely nothing.")
            help_embed.add_field(name="$whois <`@mention`>", value="Shows information about a specific user.")
            help_embed.add_field(name="$developer", value="Hey, that's me!")
            help_embed.add_field(name="$bugreport <`\"title\"`> <`\"description\"`>", value="Creates a bug-report on [GitHub](https://github.com/joseywoermann/navnlos/issues/).")
            help_embed.set_footer(text = "$help | @navnløs")

            await ctx.reply(content=None, embed=help_embed)

            mod_help_embed = discord.Embed(title="Commands that require advanced permissions:", colour=0x75e8ee)
            mod_help_embed.add_field(name="$clear <`number`>", value="deletes the specified amount of messages. (max. 2000 messages at once)")
            mod_help_embed.add_field(name="$kick <`@mention`> (<`reason`>)", value="Kicks a user.")
            mod_help_embed.add_field(name="$ban <`@mention`> (<`reason`>)", value="Bans a user.")
            mod_help_embed.add_field(name="$banid <`user-id`> (<`reason`>)", value="Bans a user by ID. With this, you can ban users that aren't even on the server.")
            mod_help_embed.add_field(name="$unban <`username#id`>", value="Removes the ban from a user.")
            mod_help_embed.add_field(name="$addrole <`@mention`> <`role-name`>", value="Adds a role to a user.")
            mod_help_embed.add_field(name="$removerole <`@mention`> <`role-name`>", value="Removes a role from a user.")
            mod_help_embed.add_field(name="$slomo <`seconds`>", value="Enables slow mode in the current channel. You need to specify the lenght in seconds.")
            mod_help_embed.add_field(name="$channeledit <`new name`>", value="Changes the name / description of the current channel.")
            mod_help_embed.add_field(name="$nickedit <`@mention`> <`new nickname`>", value="Changes the nickname of a specified user.")
            mod_help_embed.set_footer(text = "$help | @navnløs")

            await ctx.reply(content=None, embed=mod_help_embed)


def setup(client):
    client.add_cog(Help(client))
