import discord 
from discord import TextInput
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

channel_id = 1234567890

@bot.event
async def on_message(message: discord.Message):
    #Normal Messages/Content:
    
    #Let's say in a specific channel, you want to look for a phrase in a message like Hello! and you the user to say hi back
    if message.content == "Hello!" and message.channel.id == channel_id:
        await message.channel.send("Hi!")
        
    #If you want to look for a specific phrase in a message:
    if "Hello!" in message.content and message.channel.id == channel_id:
        await message.channel.send("Hi!")
        
    #You can also make everything lowercase to make everything case_insensitive
    if "Hello!".lower() in message.content.lower() and message.channel.id == channel_id:
        await message.channel.send("Hi!")
        
    if message.content.lower() == "Hello!".lower() and message.channel.id == channel_id:
        await message.channel.send("Hi!")
        
        

    #Embeds:
    
    #There's embed title, description, author, footer, image, thumbnail, etc.
    
    #Let's say you want to find a phrase in an embed, this applies to all of those
    if message.channel.id == channel_id:
        if message.embeds:
            for embed in message.embeds:
                if embed.title and 'Hello!' in embed.title.lower():
                    await message.channel.send("Hi!")
                    
    
    #Let's say you want to get the image or thumbnail url
    if message.channel.id == channel_id:
        if message.embeds:
            for embed in message.embeds:
                if embed.image:
                    print(embed.image.url)
                    
                if embed.thumbnail:
                    print(embed.thumbnail.url)
                    
    
    
    #Components:
    
    #Components include Action Row, Buttons, TextInput, and SelectMenu
    
    #Let's say you want to click a button from a specific bot or something
    bot_id = 1234567890
    if message.channel.id == channel_id and message.author.id == bot_id:
        #Let's say the bot has a message with a phrase and a button:
        if "Hello!".lower() in message.content.lower():
            if message.components:
                for action_row in message.components:
                    for button in action_row.children:
                        if isinstance(button, discord.Button):
                            #Check for something specific in the button
                            #Label being what the stuff on the button says
                            if button.label == 'Click Here!':
                                #Sleep 1 Second to prevent rate limiting and inefficiency
                                await asyncio.sleep(1)
                                await button.click()
                                
    
    #Let's say you want to prevent doubling of component interactions:
    clicked = set()
    
    if message.id in clicked:
        return
    
    #You can put an else statement, but really you don't have to
    else:
        bot_id = 1234567890
        if message.channel.id == channel_id and message.author.id == bot_id:
            #Let's say the bot has a message with a phrase and a button:
            if "Hello!".lower() in message.content.lower():
                if message.components:
                    for action_row in message.components:
                        for button in action_row.children:
                            if isinstance(button, discord.Button):
                                #Check for something specific in the button
                                #Label being what the stuff on the button says
                                if button.label == 'Click Here!':
                                    #Sleep 1 Second to prevent rate limiting and inefficiency
                                    await asyncio.sleep(1)
                                    await button.click()
                                    #Adding the message id to prevent it detecting the same message
                                    clicked.add(message.id)
                                    
                                    
    #Or you can put it here:
    
    bot_id = 1234567890
    if message.channel.id == channel_id and message.author.id == bot_id:
        #Let's say the bot has a message with a phrase and a button:
        if "Hello!".lower() in message.content.lower():
            if message.components:
                for action_row in message.components:
                    for button in action_row.children:
                        if isinstance(button, discord.Button):
                            #Check for something specific in the button
                            #Label being what the stuff on the button says
                            if button.label == 'Click Here!':
                                #Checking if it's already clicked
                                if message.id in clicked:
                                    return
                                    #Sleep 1 Second to prevent rate limiting and inefficiency
                                await asyncio.sleep(1)
                                await button.click()
                                #Adding the message id to prevent it detecting the same message
                                clicked.add(message.id)    
                                                                
                                


#Now let's use this knowledge to string something together:

import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

channel_id = 1234567890
bot_id = 1234567890
clicked = set()

@bot.event
async def on_message(message: discord.Message):
    if message.channel.id == channel_id and message.author.id == bot_id:
        if message.embeds:
            for embed in message.embeds:
                if embed.title and 'Hello!'.lower() in embed.title.lower():
                    if message.components:
                        for action_row in message.components:
                            for button in action_row.children:
                                if isinstance(button, discord.Button):
                                    if button.label == 'Click Me!':
                                        if message.id in clicked:
                                            return
                                        
                                        await asyncio.sleep(1)
                                        await button.click()
                                        clicked.add(message.id)
                                        

@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if after.author.id == bot_id and after.channel.id == channel_id:
        if after.embeds:
            for embed in after.embeds:
                if embed.title and 'You clicked the Button!'.lower() in embed.title.lower():
                    await after.channel.send("Yippee!")
                    
                    
#Really beginner example



#Utilizing the discord.Message class in a different instance:

task = None

@bot.command()
async def test(ctx: commands.Context):
    global task
    
    if task is not None:
        return
    
    #Using a task loop to loop for a msg
    task = asyncio.create_task(loop(ctx))
    

async def loop(ctx: commands.Context):
    while True:
        msg = False
        
        #Uses ctx.channel.history and discord.Message to find msgs
        async for message in ctx.channel.history(limit=10):
            if 'Hello'.lower() or 'Hello!'.lower() in message.content.lower():
                await message.reply("Hi!")
                msg = True
                
        if not msg:
            continue
                
        await asyncio.sleep(1)
        

#Task Cancel
@bot.command()
async def stop(ctx: commands.Context):
    global task
    
    if task is None:
        return
    
    task.cancel()
    task = None    
    
    
