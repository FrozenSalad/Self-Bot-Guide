# discord.Message *class*

### Intro

This is the message class, very used class in terms of Self-Bots when your self bot heavily influences message functions

## Functions


**Let's start off with basic necessities** <dl>
In most examples, we're going to use on_message for a simpler understanding, when using an on_ event, the trigger is always the context, so the message on_message finds is the context <br>
Most attributes in this class are relatively simple so I'll keep it mostly short and sweet <dl>

#### A couple attributes, content, channel/guild:
```python
channel_id = 1234567890

@bot.event
async def on_message(message: discord.Message):

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
```
Then again these are examples, this is just a basis on how to use it, you can use it different ways (possibly) <dl>
<br>
<br>

#### A simple utlitization of the discord.Embed attribute:
```python
channel_id = 1234567890

#There's embed title, description, author, footer, image, thumbnail, etc.

#Let's say you want to find a phrase in an embed, this applies to all of those

if message.channel.id == channel_id:
    if message.embeds:
        for embed in message.embeds:
            if embed.title and 'Hello!' in embed.title.lower():
                await message.channel.send("Hi!")


# Wanna just log the embed's attributes?
if message.channel.id == channel_id:
    if message.embeds:
        for embed in message.embeds:
            if embed:
                print
                (f'{embed.author}\n{embed.title}\n{embed.description}\n{embed.footer.text}')
                

#Let's say you want to get the image or thumbnail url
if message.channel.id == channel_id:
    if message.embeds:
        for embed in message.embeds:
            if embed.image:
                print(embed.image.url)
                
            if embed.thumbnail:
                print(embed.thumbnail.url)
```
<br>
<br>
<br>

#### A Simple Utiliization of discord.Message.components
```python
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
```
<br>
<br>
<br>

#### If you want to look for the message history of a context's channel:
```python
async for message in ctx.channel.history(limit=100):
    # Utilize the message class however you want based on the already sent messages, the limit is however many messages in the past history you want to look at
    
```