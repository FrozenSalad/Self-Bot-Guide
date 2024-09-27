# Asyncio *Library*

### Intro
This is utilizations on the asyncio library in your self-bot

## Functions

#### We can start off with very basic examples:
```py
# This is for when you want the script to wait however many seconds before going onto the next statement or doing the next functions
# The number being how many seconds, it can be a float as well
await asyncio.sleep(1)


# This is for an asyncio loop if you don't want to utilize variables and for in range
task = None

@bot.command
async def start(ctx):
  # Define it as a global variable
  global task

  # Create a task
  task = asyncio.create_task(loop(ctx))

async def loop(ctx: commands.Context):
  # It'll keep looping until you cancel, asyncio.sleep() being a delay or cooldown before sending or doing something
  while True:
    await ctx.send("Hi!"))
    await asyncio.sleep(3)

@bot.command
async def stop():
  global task

  # Stops the task
  task.cancel()
```
