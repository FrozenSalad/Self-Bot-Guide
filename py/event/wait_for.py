import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)


@bot.command()
async def test(ctx: commands.Context):
    
    #bot.wait_for or client.wait_for are essentially just events without the on_ prefix
    
    #For example, let's say I want to get a response from someone or myself
    
    #Define a check to make sure the parameters are correct and the message is what you're looking for
    channel = ctx.channel
    
    def check(ctx: commands.Context):
        return ctx.author == bot.user and ctx.channel == channel
    
    await ctx.send("Are you winning son?")
    #Get the response via bot.wait_for
    try:
        response = await bot.wait_for('message', timeout=60, check=check) #timeout in seconds
    
    except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        return
    
    else:
        if response.content.lower() == "yes":
            await ctx.send("Yippeee!")
        
        elif response.content.lower() == "no":
            await ctx.send("Awww..")
            
    
    
    #The check can be things like int/float/str:
    
    def integer(ctx: commands.Context):
        return ctx.author == bot.user and ctx.channel == channel and int
    
    await ctx.send("How old are you?")
    age = await bot.wait_for('message', timeout=60, check=integer)
    await ctx.send(f"Woah! You are {age.content} years old!")
    
    
    
    #bot.wait_for isn't strictly limited to message
    def react(ctx: commands.Context, reaction: discord.Reaction):
        return ctx.author.id == bot.user.id and str(reaction.emoji) == ''
    
    await ctx.send('Thumbs up this message for 5 years of good luck!')
    try:
        reaction = await bot.wait_for('reaction_add', timeout=60, check=react)
    
    except asyncio.TimeoutError:
        await ctx.send("Too Slow")
        return
    
    await ctx.send("You recieved 5 years of good luck!")
    #If you want it to be for other people, you need to set self_bot=False and the user who reacted should be replied to
    
    

    #Same for a message edit
    def check(after: discord.Message, before: discord.Message):
        return after.author.id == bot.user.id and after.author.id == channel
        
    try:
        edit = await bot.wait_for('message_edit', timeout=100, check=check)
    
    except asyncio.TimeoutError:
        await ctx.send("Timeout")
        return
    
    print(f"Message Content Before: {edit.before.content}")
    
    
    