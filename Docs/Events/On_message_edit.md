# on_message_edit *event*

### Intro
on_message but actively listens for when messages in the bot's logged history is edited

## Functions

**Keep in mind, this still uses discord.Message *class*** <br>
Before = The message before the edit <br>
After = The message after the edit <br>
<br>

#### **Examples**
```py
@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    #Uses before and after, let's make an example for if you want to log an edit's before and after in a specific channel and send it to another channel:
    channel = 1234567890
    logs_channel = 1234567890
    
    if after.channel.id == channel:
        logs = bot.get_channel(logs_channel)
        await logs.send(f"User: **{after.author.name}** || **{after.author.display_name}**\n\n**Before Edit Content:**\n\n{before.content}\n\n**After Edit Content:**\n\n{after.content}\n\n[**Jump to message**]({after.jump_url})")
        
    
    #Bot who have embeds can edit the embed's content:
    bot_id = 1234567890
    channel = 1234567890
    
    if after.channel.id ==  channel and after.author.id == bot_id:
        if after.embeds:
            for embed in after.embeds:
                if embed.title == "Whatever":
                    await after.channel.send("Hi!")
                    
                    #As a user, you cannot send or copy embeds, you may only get the contents of the embed and send it in a normal message
                    
                    await after.channel.send(f"Embed Title: {embed.title}\nEmbed Description: {embed.description}\nEmbed Author: {embed.author}")
                    
    
    clicked = set()
    #This statement can also handle components
    if after.channel.id == channel and after.author.id == bot_id:
        if after.components:
            for action_row in after.components:
                for button in action_row.children:
                    if isinstance(button, discord.Button):
                        if button.label == "Hi!":
                            if after.id in clicked():
                                return
                            
                            await asyncio.sleep(1)
                            await button.click()
```