import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import time
from collections import deque

bot = commands.Bot(command_prefix=';', self_bot=True, case_insensitive=True, chunk_guilds_at_startup=False, request_guilds=False)
bot.remove_command('help')

@bot.event
async def on_ready():
    global start 
    start = time.time()
    print(f'Username: {bot.user.name} || {bot.user.display_name}\nUser ID: {bot.user.id}')
    

@bot.command(name='ping')
async def ping(ctx: commands.Context):
    await ctx.reply(f'Pong! {round(bot.latency * 1000)}ms')
    

@bot.command(name='userid')
async def userid(ctx: commands.Context):
    await ctx.reply(f'{bot.user.id}')
    

@bot.command(name='av')
async def avatar(ctx: commands.Context):
    await ctx.reply(f'Avatar URL: {bot.user.avatar.url}')
    

@bot.command(name='token')
async def token(ctx: commands.Context):
    await ctx.reply(f'Token:\n{bot.http.token}')
    
    
@bot.command(name='uptime')
async def uptime(ctx: commands.Context):
    current_time = time.time()
    uptime_seconds = int(current_time - start)
    uptime = str(timedelta(seconds=uptime_seconds))
    
    days, remainder = divmod(uptime_seconds, 86400)  
    hours, remainder = divmod(remainder, 3600)       
    minutes, seconds = divmod(remainder, 60)
    
    readable = (
        (f"{days}d " if days else "") +
        (f"{hours}h " if hours else "") +
        (f"{minutes}m " if minutes else "") +
        (f"{seconds}s" if seconds else "")
    ).strip() 
    
    await ctx.reply(f'Uptime: {uptime} // {readable}')
    

deleted_snipes = deque(maxlen=10) 
edited_snipes = deque(maxlen=10)   

@bot.event
async def on_message_delete(message: discord.Message):
    if not message.guild: 
        return
    
    deleted_snipes.append({
        "content": message.content,
        "author": str(message.author),
        "channel": str(message.channel),
        "time": message.created_at
    })


@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if not before.guild:
        return
    
    edited_snipes.append({
        "before": before.content,
        "after": after.content,
        "author": str(before.author),
        "channel": str(before.channel),
        "time": before.edited_at
    })


@bot.command(name='snipe')
async def snipe(ctx: commands.Context) -> None:
    if deleted_snipes:
        snipe = deleted_snipes[-1]  
        content = snipe["content"]
        author = snipe["author"]
        channel = snipe["channel"]
        time = snipe["time"]

        
        await ctx.reply(f"Sniped deleted message:\nAuthor: {author}\nChannel: {channel}\nTime: {time}\nContent: {content}")
    elif edited_snipes:
        snipe = edited_snipes[-1] 
        before = snipe["before"]
        after = snipe["after"]
        author = snipe["author"]
        channel = snipe["channel"]
        time = snipe["time"]

        
        await ctx.reply(f"Sniped edited message:\nAuthor: {author}\nChannel: {channel}\nTime: {time}\nBefore: {before}\nAfter: {after}")
    else:
        await ctx.reply("No messages to snipe!")


@bot.command(name='snipelist')
async def snipelist(ctx: commands.Context) -> None:
    if not deleted_snipes and not edited_snipes:
        await ctx.reply("No messages to snipe!")
        return

    messages = []


    if deleted_snipes:
        messages.append("**Last Deleted Messages:**")
        for idx, snipe in enumerate(list(deleted_snipes)[::-1], 1):  
            messages.append(
                f"{idx}. Author: {snipe['author']} | Channel: {snipe['channel']} | Time: {snipe['time']}\nContent: {snipe['content']}"
            )

    # Format the last edited messages
    if edited_snipes:
        messages.append("\n**Last Edited Messages:**")
        for idx, snipe in enumerate(list(edited_snipes)[::-1], 1):  
            messages.append(
                f"{idx}. Author: {snipe['author']} | Channel: {snipe['channel']} | Time: {snipe['time']}\nBefore: {snipe['before']}\nAfter: {snipe['after']}"
            )


    await ctx.reply("\n".join(messages))
    

@bot.command(name='logout')
async def logout(ctx: commands.Context):
    await ctx.send('Closing Script')
    await bot.close()


bot.run("token")