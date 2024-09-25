import discord
from discord.ext import commands

#Command Prefix is set to whatever you want, it's the first thing in a message that triggers it
#Example: if your prefix is ! or m and the command is help; !help, mhelp
bot = commands.Bot(command_prefix="prefix")

#Setting Self Bot to True:
bot = commands.Bot(self_bot=True)

#commands.Bot allows a case insensitive parameter which makes most things like commands case insensitive
bot = commands.Bot(case_insensitive=False)

#Disabling Chunking Guilds
#When you're chunking guilds and the bot user has a lot of guilds, your user bot can take up to 2 minutes to start
bot = commands.Bot(chunk_guilds_at_startup=False)
#This parameter is True by default, it's best to disable this if you want an efficient bot unless you're making a project that requires chunking guilds




#Ex. Starting your first bot (boring edition)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';', self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)
    
@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("Pong!")
    
token = ""
bot.run(token)


#Ex. #2 Starting your first bot (cool edition :3)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';', self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

@bot.event
async def on_ready():
    print(f'Username: {bot.user.name} || {bot.user.display_name}\nUser ID: {bot.user.id}')
    

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.reply("Pong!")
    
bot.run("token")