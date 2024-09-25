import discord 
from discord.ext import commands
import asyncio
import re


bot = commands.Bot(command_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False, request_guilds=False)


@bot.command()
async def m(ctx: commands.Context):
    global channel
    
    channel = ctx.channel.id
    

channel = None
bot_id = 519850436899897346
clicked = set()
mon = None

#Modal can be used via on_modal after an interaction triggers one, for example a button click on a application``
@bot.event
async def on_message(message: discord.Message):
    if message.id in clicked:
        return
    
    else:
        if message.components:
            for action_row in message.components:
                for button in action_row.children:
                    if isinstance(button, discord.Button):
                        if button.label == 'Click Here for Modal!':
                            await asyncio.sleep(1)
                            await button.click()
                            clicked.add(message.id)
                            

@bot.event
async def on_modal(modal: discord.Modal):
    if modal.title == "A Wild Modal Appeared!":
        if modal.components:
            for action_row in modal.components:
                for component in action_row.children:
                    if isinstance(component, discord.TextInput):
                        #You can check for a textinput placeholder or label like || if component.placeholder == "": || if component.label == ""
                        #This is for when there is more than 1 textinput, if there's only one box in a modal, component label and elif is not necessary
                        #
                        if component.label == "":
                            component.answer("Whatever you want to sumbit")
                        
                        elif component.label == "":
                            component.answer("Whatever")
                            
                    await modal.submit()                            


