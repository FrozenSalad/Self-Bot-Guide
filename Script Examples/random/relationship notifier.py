# Simple relationship notifier for when a friend removes you.

import discord
from discord.ext import commands
import asyncio
import aiohttp
 
bot = commands.Bot(command_prefix=">", case_insensitive=True, self_bot=True, chunk_guilds_at_startup=False, request_guilds=False)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Username: {bot.user.name} || {bot.user.display_name}\nUser ID: {bot.user.id}")
    
    
@bot.event
async def on_relationship_remove(relationship: discord.Relationship):
    if relationship.type == discord.RelationshipType.friend:
        embed = discord.Embed(
            title="**Relationship Notifier**",
            description=f"**{relationship.user}** has removed you as a friend.\n\nUser ID: {relationship.user.id}\nTime Removed: {discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S %Z')}",
            color=discord.Color.red()
        )
        await web(embed)
        
        
        
async def web(embed):
    async with aiohttp.ClientSession() as session:
        # Add your webhook URL
        url = ""
        webhook = discord.Webhook.from_url(url=url, session=session)
        await webhook.send(content=f"<@{bot.user.id}>", embed=embed)
        
        
bot.run("token")