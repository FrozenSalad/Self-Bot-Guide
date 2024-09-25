import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(commands_prefix="!", self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

#To get on_modal to catch a modal, a modal interaction needs to be interacted with

#For example let's use a button click, if a bot or application has a button which has a modal popup

#let's use on_message
bot_id = 1234567890
channel_id = 1234567890
clicked = set()

@bot.event
async def on_message(message: discord.Message):
    global clicked
    if message.author.id == bot_id and message.channel.id == channel_id:
        #lets just use embeds to detect a specific message from a bot with a button
        if message.embeds:
            for embed in message.embeds:
                if embed.title == "Hi!":
                    if message.components:
                        for action_row in message.components:
                            for button in action_row.children:
                                if isinstance(button, discord.Button):
                                    if button.label == "Say Hello back!":
                                        if message.id in clicked:
                                            return
                                        
                                        await asyncio.sleep(1)
                                        await button.click()
                                        clicked.add(message.id)
                                        
                                        
#After the component is clicked, a modal interaction should have been triggered     
@bot.event
async def on_modal(modal: discord.Modal):
    #Get the modal.title
    if modal.title == "Say Hello Back!":
        #Use components
        if modal.components:
            for action_row in modal.components:
                for textinput in action_row.children:
                    #Use text input to submit a response in a text box, there's also something for different placeholders in the text box if there are more than one like if textinput.placeholder == ""
                    if isinstance(textinput, discord.TextInput):
                        answer = "Hello"
                        await textinput.answer(answer)
                        #Submit the modal
                        await modal.submit()
                                        
                                        