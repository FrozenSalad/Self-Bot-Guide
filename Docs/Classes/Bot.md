# Bot / *class* discord.ext.commands.Bot 

### Intro
This will cover starting your first bot, commands.Bot parameters, and a couple bot attributes <br>
Attributes Used: **ctx.reply || bot.get_channel || message.guild || message.content**

## Starting your first bot
#### **The Boring way**:

```python
#Ex. Starting your first bot (boring edition)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)
    
@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("Pong!")
    
token = ""
bot.run(token)
```
<br>

#### **The Cool way**:
```python
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
```

## Functions

#### **A few important commands.Bot parameters**:

```py
#Command Prefix is set to whatever you want, it's the first thing in a message that triggers it
#Example: if your prefix is ! or m and the command is help; !help, mhelp
bot = commands.Bot(command_prefix="prefix")

#Setting Self Bot to True: If self bot is set to False, it makes it so users that are not the token user, are allowed to use your user commands instead
bot = commands.Bot(self_bot=True)

#commands.Bot allows a case insensitive parameter which makes most things like commands case insensitive
bot = commands.Bot(case_insensitive=False)

#Disabling Chunking Guilds
#When you're chunking guilds and the bot user has a lot of guilds, your user bot can take up to 2 minutes to start
bot = commands.Bot(chunk_guilds_at_startup=False)
#This parameter is True by default, it's best to disable this if you want an efficient bot unless you're making a project that requires chunking guilds
```
<br>

#### **A couple bot.get/fetch attribute types**:

```py
# For this example were going to use on_message
@bot.event
async def on_message(message: Message):
    
    # This is going to use bot.get 
    # Let's say you want to log a message from a different channel with a specific keyword and send it to another channel
    # Here were going to log the whole server for messages but only send to one channel
    
    if message.guild.id == guild_id and message.content == "Hi":
        channel_to_send = 1234567899
        channel = bot.get_channel(channel_to_send)
        await channel.send(f"**Username:** {message.author.name} || {message.author.display_name}\n**User ID:** {message.author.id}\n\n**Message Sent:** \n{message.content}\n\n[Jump to Message]({message.jump_url})")
        
    
    # You can also get guilds/servers that way as well, basically just utiizies the discord.Guild class
    
    guild_id = 2379847823789
    guild = bot.get_channel(guild_id)
```