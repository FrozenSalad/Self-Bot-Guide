# This is for when you want to capture messages from a specific channel(s)/server and send them to a webhook.
# Input your guild_id/channel_id/channel_ids, webhook_url, & token then run the script.
# Change the on_message event to fit your needs.
import discord
from discord.ext import commands
import asyncio
import aiohttp
from colorama import Fore, Style

bot = commands.Bot(command_prefix=">", self_bot=True, case_insensitive=True, chunk_guilds_at_startup=False, request_guilds=False)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(Fore.GREEN + f"Welcome! {bot.user.name} || {bot.user.display_name}\n\nUser ID: {bot.user.id}" + Style.RESET_ALL)
    await bot.change_presence(status=discord.Status.idle, afk=True)
    

guild_id = 1234567890
channel_id = 1234567890
channel_ids = [1234567890, 1234567890]
webhook_url = "https://discord.com/api/webhooks/1234567890/ABCDEFGHIJKLMN1234567890"

@bot.event
async def on_message(message: discord.Message):
    # if message.channel.id == channel_id:
    # if message.channel.id in channel_ids:
    if message.guild.id == guild_id:
        author = message.author
        if author.id == bot.user.id:
            return
        
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(webhook_url, session=session)
            
            embed = discord.Embed(
                title="Logged Message",
                description=message.content,
                color=discord.Color.green()
            )
            embed.set_author(name=author.name, icon_url=author.avatar_url)
            webhook.send(embed=embed, content=f"<@{bot.user.id}>")
            

bot.run("token")