import discord
from discord.ext import commands
import asyncio
from discord import Message

bot = commands.Bot(command_prefix=">", case_insensitive=True, self_bot=True, chunk_at_guilds_startup=False, request_guilds=False)
bot.remove_command('help')


# For this example were going to use on_message
@bot.event
async def on_message(message: Message):
    
    # This is going to use bot.get 
    # Let's say you want to log a message from a different channel with a specific keyword and send it to another channel
    # Here were going to log the whole server for messages but only send to one channel
    
    guild_id = 2379847823789
    
    if message.guild.id == guild_id and message.content == "Hi":
        channel_to_send = 1234567899
        channel = bot.get_channel(channel_to_send)
        await channel.send(f"**Username:** {message.author.name} || {message.author.display_name}\n**User ID:** {message.author.id}\n\n**Message Sent:** \n{message.content}\n\n[Jump to Message]({message.jump_url})")
        
    
    # You can also get guilds/servers that way, 