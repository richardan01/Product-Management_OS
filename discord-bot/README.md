# Product OS — Discord Bot

A Discord bot that gives you access to your Product OS from any device.

## Commands

| Command | Description |
|---------|-------------|
| `/ping` | Check bot is online |
| `/briefing` | Full morning brief — tasks, CDP, priorities |
| `/today` | Today's focus, top 3 tasks, blockers |
| `/roadmap` | Milestone status, OKR alignment, risks |
| `/weekly-update` | Draft weekly update for Jervis |
| `/cdp-status` | CDP phase, risks, flight 1 recommendation |
| `/ask [question]` | Ask anything about your OS |
| `/add-task [desc]` | Add task to Tasks/active.md |
| `/note [title] [content]` | Save quick note to Meetings/ |

## Setup

### 1. Create a Discord bot

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. New Application → give it a name (e.g. "Product OS")
3. Bot tab → Reset Token → copy the token
4. Bot tab → enable **Message Content Intent**
5. OAuth2 → URL Generator → scopes: `bot` + `applications.commands` → permissions: `Send Messages`, `Read Messages/View Channels`
6. Copy the generated URL → open it → invite bot to your personal server

### 2. Get your channel ID

1. Discord → User Settings → Advanced → enable Developer Mode
2. Right-click your notification channel → Copy Channel ID

### 3. Configure

```bash
cd /Users/richardng/Documents/Product-OS/discord-bot
cp .env.example .env
```

Edit `.env`:
```
DISCORD_TOKEN=your_token_here
ANTHROPIC_API_KEY=your_key_here
NOTIFICATION_CHANNEL_ID=your_channel_id_here
```

### 4. Install and run

```bash
pip install -r requirements.txt
python bot.py
```

Bot should show as Online in Discord. Type `/ping` to verify.

## Daily notifications

The bot posts a standup message every day at **9:00 AM HKT** to your notification channel.
Set `NOTIFICATION_CHANNEL_ID` in `.env` to enable it. Leave it as `0` to disable.

## File paths

The bot reads from and writes to `../My-OS/` relative to its own folder. No separate database — same files Claude Code uses.
