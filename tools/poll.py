import discord
from discord.ext import commands

class Poll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, question=None, response0=None, response1=None, response2=None, response3=None, response4=None, response5=None, response6=None, response7=None, response8=None):

        async with ctx.channel.typing():
            emote_one = '1️⃣'
            emote_two = '2️⃣'
            emote_three = '3️⃣'
            emote_four = '4️⃣'
            emote_five = '5️⃣'
            emote_six = '6️⃣'
            emote_seven = '7️⃣'
            emote_eight = '8️⃣'
            emote_nine = '9️⃣'

            await ctx.channel.purge(limit = 1)

            if question:

                while '_' in question:
                    question = question.replace('_',' ')

                if response0:

                    while '_' in response0:
                        response0 = response0.replace('_',' ')

                    if response1:

                        while '_' in response1:
                            response1 = response1.replace('_',' ')

                        if response2:

                            while '_' in response2:
                                response2 = response2.replace('_',' ')

                            if response3:

                                while '_' in response3:
                                    response3 = response3.replace('_',' ')

                                if response4:

                                    while '_' in response4:
                                        response4 = response4.replace('_',' ')

                                    if response5:

                                        while '_' in response5:
                                            response5 = response5.replace('_',' ')

                                        if response6:

                                            while '_' in response6:
                                                response6 = response6.replace('_',' ')

                                            if response7:

                                                while '_' in response7:
                                                    response7 = response7.replace('_',' ')

                                                if response8:

                                                    while '_' in response8:
                                                        response8 = response8.replace('_',' ')

                                                    poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6) + "\n:eight: " + str(response7) + "\n:nine: " + str(response8), color=0x75e8ee)
                                                    poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                                    msg = await ctx.send(content=None, embed=poll_embed)

                                                    await msg.add_reaction(emote_one)
                                                    await msg.add_reaction(emote_two)
                                                    await msg.add_reaction(emote_three)
                                                    await msg.add_reaction(emote_four)
                                                    await msg.add_reaction(emote_five)
                                                    await msg.add_reaction(emote_six)
                                                    await msg.add_reaction(emote_seven)
                                                    await msg.add_reaction(emote_eight)
                                                    await msg.add_reaction(emote_nine)

                                                else:

                                                    poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6) + "\n:eight: " + str(response7), color=0x75e8ee)
                                                    poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                                    msg = await ctx.send(content=None, embed=poll_embed)

                                                    await msg.add_reaction(emote_one)
                                                    await msg.add_reaction(emote_two)
                                                    await msg.add_reaction(emote_three)
                                                    await msg.add_reaction(emote_four)
                                                    await msg.add_reaction(emote_five)
                                                    await msg.add_reaction(emote_six)
                                                    await msg.add_reaction(emote_seven)
                                                    await msg.add_reaction(emote_eight)

                                            else:

                                                poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5) + "\n:seven: " + str(response6), color=0x75e8ee)
                                                poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                                msg = await ctx.send(content=None, embed=poll_embed)

                                                await msg.add_reaction(emote_one)
                                                await msg.add_reaction(emote_two)
                                                await msg.add_reaction(emote_three)
                                                await msg.add_reaction(emote_four)
                                                await msg.add_reaction(emote_five)
                                                await msg.add_reaction(emote_six)
                                                await msg.add_reaction(emote_seven)

                                        else:

                                            poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4) + "\n:six: " + str(response5), color=0x75e8ee)
                                            poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                            msg = await ctx.send(content=None, embed=poll_embed)

                                            await msg.add_reaction(emote_one)
                                            await msg.add_reaction(emote_two)
                                            await msg.add_reaction(emote_three)
                                            await msg.add_reaction(emote_four)
                                            await msg.add_reaction(emote_five)
                                            await msg.add_reaction(emote_six)

                                    else:

                                        poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3) + "\n:five: " + str(response4), color=0x75e8ee)
                                        poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                        msg = await ctx.send(content=None, embed=poll_embed)

                                        await msg.add_reaction(emote_one)
                                        await msg.add_reaction(emote_two)
                                        await msg.add_reaction(emote_three)
                                        await msg.add_reaction(emote_four)
                                        await msg.add_reaction(emote_five)

                                else:

                                    poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2) + "\n:four: " + str(response3), color=0x75e8ee)
                                    poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                    msg = await ctx.send(content=None, embed=poll_embed)

                                    await msg.add_reaction(emote_one)
                                    await msg.add_reaction(emote_two)
                                    await msg.add_reaction(emote_three)
                                    await msg.add_reaction(emote_four)


                            else:

                                poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1) + "\n:three: " + str(response2), color=0x75e8ee)
                                poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                                msg = await ctx.send(content=None, embed=poll_embed)

                                await msg.add_reaction(emote_one)
                                await msg.add_reaction(emote_two)
                                await msg.add_reaction(emote_three)

                        else:

                            poll_embed = discord.Embed(title=str(question), description="\n\n  :one: " + str(response0) + "\n:two: " + str(response1), color=0x75e8ee)
                            poll_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)

                            msg = await ctx.send(content=None, embed=poll_embed)

                            await msg.add_reaction(emote_one)
                            await msg.add_reaction(emote_two)

                    else:
                        poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmöglichkeiten haben.", color=discord.Color.dark_purple())
                        poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
                        await ctx.send(content=None, embed=poll_error_embed)

                else:
                    poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmöglichkeiten haben.", color=discord.Color.dark_purple())
                    poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
                    await ctx.send(content=None, embed=poll_error_embed)
            else:
                poll_error_embed = discord.Embed(title="Error", description="Umfrage muss mindestens 2 Antwortmöglichkeiten und eine Frage haben.", color=discord.Color.dark_purple())
                poll_error_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
                await ctx.send(content=None, embed=poll_error_embed)

def setup(client):
    client.add_cog(Poll(client))
