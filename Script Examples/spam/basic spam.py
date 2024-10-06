# This script uses wait_for to get the channel IDs, delay, amount, and message to spam. Context & Commands, and Asyncio Loops
# The spamming can be stopped with the >stop command.
# If set to more than 1 channel, the rate limiting will be more likely to occur. Calculate the delays and set it accordingly.

import discord
from discord.ext import commands
import asyncio
 
bot = commands.Bot(command_prefix=">", case_insensitive=True, self_bot=True, chunk_guilds_at_startup=False, request_guilds=False)
bot.remove_command('help')
 
channel_ids = []
task = None
 
@bot.event
async def on_ready():
    print(f"Username: {bot.user.name} || {bot.user.display_name}\nUser ID: {bot.user.id}")
    

@bot.command()
async def spam(ctx: commands.Context):
    global channel_ids, task
    channel = ctx.channel
    
    def string(ctx: commands.Context):
        return ctx.author.id == bot.user.id and ctx.channel == channel
    
    def integer(ctx: commands.Context):
        return ctx.author.id == bot.user.id and ctx.channel == channel and int
    
    await ctx.send("**What Channel IDs?**")
    try:
        cid = await bot.wait_for('message', timeout=60, check=integer)
    except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        return
    
    channel_ids = [int(c) for c in cid.content.split()]
    
    await ctx.send("**What message sending delay do you want?**")
    try:
        de = await bot.wait_for('message', timeout=60, check=integer)
        delay = int(de.content)
    except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        return
    
    await ctx.send("**How many messages?**")
    try:
        amt = await bot.wait_for('message', timeout=60, check=integer)
        amount = int(amt.content)
    except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        return
    
    await ctx.send("**And what message would you like to send?**")
    try:
        msg = await bot.wait_for('message', timeout=60, check=string)
        message = str(msg.content)
    except asyncio.TimeoutError:
        await ctx.send("Timed Out")
        return
    
    
    await ctx.send(f"Starting in channels {channel_ids}")
    task = asyncio.create_task(spamming(channel_ids, delay, amount, message))
    
    
async def spamming(channel_ids, delay, amount, message):
    while True:
        for _ in range(amount):
            for id in channel_ids:
                channel = bot.get_channel(id)
                if channel:
                    await channel.send(message)
                    
            await asyncio.sleep(delay)
            
 
@bot.command()
async def stop(ctx: commands.Context):
    global task, channel_ids
    
    channel_ids = []
    task.cancel()
    await ctx.reply("Spamming Stopped")
    
    
bot.run("token")