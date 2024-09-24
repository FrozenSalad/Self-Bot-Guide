import discord 
from discord.ext import commands

bot = commands.Bot(self_bot=True)


@bot.event
async def on_ready():
    #There's many different things you can do this case, 2 examples being:
    
    #If you want it to print the Bot User's Name & ID
    print(f'Username: {bot.user.name} || {bot.user.display_name}\nUser ID: {bot.user.id}')
    
    #Setting presence
    
    #discord.Status.idle/online/dnd/offline 
    bot.change_presence(status=discord.Status.idle)
    
    #Setting afk to true let's notifications go through, when you don't have this set to true it stops notifications from appearing on most devices
    bot.change_presence(afk=True)
    
    #You can also set an activity upon startup which you'd need to set via discord.Activity, for example:
    activity = discord.Activity(type=discord.ActivityType.watching, name="Youtube")
    bot.change_presence(activity=activity)
    
    