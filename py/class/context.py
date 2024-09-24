import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

channel = None
# commands.Context / ctx || A couple usages:

@bot.command()
async def test(ctx: commands.Context):
    #You can set a global channel based off the context channel for other functions like on_message
    global channel
    channel = ctx.channel
    #Or
    channel = ctx.channel.id
    
    #ctx.message is the message that ran the context command in this case
    print(f'Original Message: {ctx.message.content}')
    
    
    #Maybe you want to send a message or reply to the context message
    await ctx.send("Hi!")
    #or
    await ctx.reply("Hi!", mention_author=True) #mention_author parameter is set to default True
    
    
    #If you want to async for messages, you can check in the ctx.channel.history:
    async for message in ctx.channel.history(limit=100):
        #You can use the message class based off the history of the channel, you can loop this in a loop if you want to make like a watchdog
        #This is essentially for if you don't want to use a wait_for or on_message event
        #Works the exact same but instead you're checking for history and you set how many msgs it can see at once while also changing it's speed of checking
        print()
    
    
    
    