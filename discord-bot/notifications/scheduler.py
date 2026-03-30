from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import file_reader
from utils.claude_client import ask_claude
import config

_scheduler = AsyncIOScheduler(timezone=config.TIMEZONE)


def _truncate(text: str, limit: int = 1900) -> str:
    return text if len(text) <= limit else text[:limit] + "\n…(truncated)"


async def _post_standup(bot: commands.Bot):
    channel = bot.get_channel(config.NOTIFICATION_CHANNEL_ID)
    if not channel:
        print(f"Standup: channel {config.NOTIFICATION_CHANNEL_ID} not found")
        return

    tasks = file_reader.read_tasks()
    goals = file_reader.read_goals()

    # Check for blockers
    has_blockers = "## Blocked" in tasks and tasks.split("## Blocked")[1].strip().startswith("-")

    system = (
        "You are [Your Name]'s Product OS assistant. Be very concise — this is a morning standup message. "
        "Use bullet points. No preamble."
    )
    prompt = (
        "Reply in under 600 characters. Give me a morning standup summary:\n"
        "1. Top 3 tasks to focus on today (from In Progress)\n"
        "2. Any blockers that need attention (🔴 flag these)\n"
        "3. One quick reminder aligned to 30-60-90 goals\n\n"
        f"## Active Tasks\n\n{tasks}\n\n## Goals\n\n{goals}"
    )

    reply = ask_claude(system, prompt, max_chars=600)
    header = "🌅 **Good morning — here's your daily standup**\n\n"
    if has_blockers:
        header = "🌅 **Good morning — you have blockers to address today**\n\n"

    await channel.send(_truncate(header + reply))


def setup_scheduler(bot: commands.Bot):
    if not config.NOTIFICATION_CHANNEL_ID:
        print("NOTIFICATION_CHANNEL_ID not set — skipping scheduler")
        return

    _scheduler.add_job(
        _post_standup,
        trigger="cron",
        hour=config.STANDUP_HOUR,
        minute=config.STANDUP_MINUTE,
        args=[bot],
        id="daily_standup",
        replace_existing=True,
    )
    _scheduler.start()
    print(f"Scheduler started — standup at {config.STANDUP_HOUR:02d}:{config.STANDUP_MINUTE:02d} {config.TIMEZONE}")
