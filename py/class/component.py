import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

bot_id = 1234567890
channel_id = 1234567890
clicked = set()


# In this instance were going to use on_message
@bot.event
async def on_message(message: discord.Message):
    if message.channel.id == channel_id and message.author.id == bot_id:
        # You can make a bunch of if statements before this but this is just how you use it
        
        # This is a button example
        if message.components:
            for action_row in message.components:
                for button in action_row.children:
                    if isinstance(button, discord.Button):
                        await asyncio.sleep(1)
                        await button.click()
                        

        # If the button has a specific label
        if message.components:
            for action_row in message.components:
                for button in action_row.children:
                    if isinstance(button, discord.Button):
                        if button.label == "Label":
                            await asyncio.sleep(1)
                            await button.click()
                            
        
        # If you only want to click a message with a button once and want to minimize it bugging out and clicking it more than once
        clicked = set()
        
        if message.components:
            for action_row in message.components:
                for button in action_row.children:
                    if isinstance(button, discord.Button):
                        if message.id in clicked:
                            return
                        
                        await asyncio.sleep(1)
                        await button.click()
                        clicked.add(message.id)
                        
        
        if message.components:
            for action_row in message.components:
                for menu in action_row.children:
                    if isinstance(option, discord.SelectMenu):
                        for option in menu.options:
                            if option.label == "Pick Me!":
                                await asyncio.sleep(1)
                                await menu.choose(option.value)
                                
                                
        if message.components:
            for action_row in message.components:
                for component in action_row.children:
                    if isinstance(component, discord.SelectMenu):
                        for option in component.options:
                            if option.label == "Pick Me!":
                                await component.choose()
                                        
                        
            
                    
@bot.event
async def on_modal(modal: discord.Modal):
    if modal.components:
        for action_row in modal.components:
            for input in action_row.children:
                if isinstance(input, discord.TextInput):
                    input.answer('hi')
                    await modal.submit()
                    
                    
    if modal.components:
        for action_row in modal.components:
            for input in action_row.children:
                if isinstance(input, discord.TextInput):
                    if input.label == "Box 1":
                        input.answer("Whatever1")
                    
                    elif input.label == "Box 2":
                        input.answer("Whatever2")
                
                await modal.submit()
                
    
    if modal.components:
        for action_row in modal.components:
            for menu in action_row.children:
                if isinstance(menu, discord.SelectMenu):
                    for option in menu.options:
                        if option.label == "Pick Me!":
                            await menu.choose()
                            await modal.submit()
