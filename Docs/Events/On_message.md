# on_message *event*

### Intro
An event that actively listens for messages under the message class

## Functions

#### **It just uses the message class, but looks for messages actively** *random example*
```py
@bot.event
async def on_message(message: discord.Message):
    print(message.content)
```