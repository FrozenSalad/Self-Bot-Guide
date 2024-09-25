# on_message *event*

### Intro
An event that actively listens for messages under the message class <br>
**Extremely Important: If you have a command and on_message in the same script you need to include *await bot.process_commands(message)**
```py
@bot.command()
async def ping(ctx):
    await ctx.reply("pong")

@bot.event
async def on_message(message: discord.Message):
    print(message.content)

    # this should always be in the first indent at the very bottom of on_message
    await bot.process_commands(message)
```

## Functions

#### **It just uses the message class, but looks for messages actively** *random example*
```py
@bot.event
async def on_message(message: discord.Message):
    print(message.content)
```
