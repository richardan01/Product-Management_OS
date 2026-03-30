import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
NOTIFICATION_CHANNEL_ID = int(os.getenv("NOTIFICATION_CHANNEL_ID", "0"))

# Claude Code subprocess
CLAUDE_BIN = os.getenv("CLAUDE_BIN", "/Users/richardng/.local/bin/claude")
CLAUDE_MODEL = "sonnet"

# My-OS paths
MY_OS = Path(__file__).parent.parent / "My-OS"

TASKS_ACTIVE = MY_OS / "Tasks" / "active.md"
TASKS_BACKLOG = MY_OS / "Tasks" / "backlog.md"
GOALS = MY_OS / "GOALS.md"
CDP_BRIEF = MY_OS / "Projects" / "cdp-implementation" / "brief.md"
CDP_RESEARCH = MY_OS / "Projects" / "cdp-implementation" / "research" / "pain-point-synthesis.md"
CDP_REFERENCE = MY_OS / "Knowledge" / "Reference" / "cdp.md"
MARTECH_STACK = MY_OS / "Knowledge" / "Reference" / "martech-stack.md"
MEETINGS_DIR = MY_OS / "Meetings"
TEMP_DIR = MY_OS / "_temp"

# Notifications schedule (24h, HKT = UTC+8)
STANDUP_HOUR = 9    # 9:00 AM HKT
STANDUP_MINUTE = 0
TIMEZONE = "Asia/Hong_Kong"
