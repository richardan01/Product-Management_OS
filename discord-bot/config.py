import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
NOTIFICATION_CHANNEL_ID = int(os.getenv("NOTIFICATION_CHANNEL_ID", "0"))

# Claude Code subprocess — defaults to 'claude' on your PATH
CLAUDE_BIN = os.getenv("CLAUDE_BIN", "claude")
CLAUDE_MODEL = "sonnet"

# My-OS paths
MY_OS = Path(__file__).parent.parent / "My-OS"

TASKS_ACTIVE = MY_OS / "Tasks" / "active.md"
TASKS_BACKLOG = MY_OS / "Tasks" / "backlog.md"
GOALS = MY_OS / "GOALS.md"

# Update these paths to point to your main project
CDP_BRIEF = MY_OS / "Projects" / "cdp-implementation" / "brief.md"
CDP_RESEARCH = MY_OS / "Projects" / "cdp-implementation" / "research" / "pain-point-synthesis.md"
CDP_REFERENCE = MY_OS / "Knowledge" / "Reference" / "cdp.md"
MARTECH_STACK = MY_OS / "Knowledge" / "Reference" / "martech-stack.md"

MEETINGS_DIR = MY_OS / "Meetings"
TEMP_DIR = MY_OS / "_temp"

# Notifications schedule — configure via .env
STANDUP_HOUR = int(os.getenv("STANDUP_HOUR", "9"))
STANDUP_MINUTE = int(os.getenv("STANDUP_MINUTE", "0"))
TIMEZONE = os.getenv("TIMEZONE", "UTC")
