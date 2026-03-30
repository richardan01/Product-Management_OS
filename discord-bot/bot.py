import ssl
import certifi
import asyncio
import aiohttp
import discord
from discord.ext import commands
import config
from commands.os_commands import setup_os_commands
from commands.capture import setup_capture_commands
from commands.query import setup_query_commands
from notifications.scheduler import setup_scheduler

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    setup_scheduler(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.tree.command(name="ping", description="Check if the bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong — Product OS bot is online ✓")


setup_os_commands(bot)
setup_capture_commands(bot)
setup_query_commands(bot)


async def main():
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_ctx)
    async with aiohttp.ClientSession(connector=connector) as session:
        bot.http.connector = connector
        await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    if not config.DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN not set in .env")
    asyncio.run(main())
