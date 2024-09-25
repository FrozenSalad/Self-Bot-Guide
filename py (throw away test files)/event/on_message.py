import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)


@bot.event
async def on_message(message: discord.Message):
    #This is just as straight forward as in the normal message class, but this finds every single message being sent no matter the limit
    
    #Refer to message class for a few on_message examples
    print()