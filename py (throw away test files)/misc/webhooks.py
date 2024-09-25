import discord
import aiohttp
from discord.ext import commands

bot = commands.Bot(command_prefix=';', self_bot=True, case_insensitive=False, chunk_guilds_at_startup=False)

@bot.command()
async def test(ctx):
    await web(ctx)

async def web(ctx):
    async with aiohttp.ClientSession() as session:
        url = ""
        webhook = discord.Webhook.from_url(url=url, session=session)
        embed = discord.Embed(
            title="Hello!",
            description="This is my description! Yippee!",
            color=discord.Color.green()
        )
        embed.set_author(name=f"{bot.user.name}", icon_url=bot.user.avatar.url, url=bot.user.avatar.url)
        await webhook.send(embed=embed)
        