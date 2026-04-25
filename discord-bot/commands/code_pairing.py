import discord
from discord.ext import commands
from utils import file_reader
from utils.claude_client import ask_claude

CODE_PAIR_SYSTEM = (
    "You are a Code Pairing assistant from the Product OS. "
    "You help with code questions, debugging, architecture decisions, and "
    "pair-programming tasks. Use the Product OS context provided to give "
    "relevant answers tied to the user's current projects and tech stack. "
    "Be concise, practical, and write code when helpful."
)

# Track active code pairing sessions by user ID
_active_sessions: set[int] = set()


async def handle_dm(bot: commands.Bot, message: discord.Message):
    """Handle incoming DMs — prompt code pairing or continue a session."""
    user_id = message.author.id

    if user_id not in _active_sessions:
        # First DM — prompt to start code pairing
        embed = discord.Embed(
            title="Code Pairing Session",
            description=(
                "Hey! I can start a **code pairing** session with you.\n\n"
                "I'll help with:\n"
                "- Debugging and code review\n"
                "- Architecture decisions for your projects\n"
                "- Writing and refactoring code\n"
                "- Technical questions about your stack\n\n"
                "Type your question or describe what you're working on to begin!"
            ),
            color=0x5865F2,
        )
        embed.set_footer(text="Type 'end' to finish the session.")
        _active_sessions.add(user_id)
        await message.channel.send(embed=embed)
        return

    # End session command
    if message.content.strip().lower() == "end":
        _active_sessions.discard(user_id)
        await message.channel.send("Code pairing session ended. DM me anytime to start a new one!")
        return

    # Active session — process as code pairing question
    async with message.channel.typing():
        context = "\n\n---\n\n".join([
            f"## Active Tasks\n\n{file_reader.read_tasks()}",
            f"## Goals\n\n{file_reader.read_goals()}",
            f"## Martech Stack\n\n{file_reader.read_martech_stack()}",
        ])
        reply = ask_claude(
            CODE_PAIR_SYSTEM,
            f"Reply in under 1800 characters.\n\nQuestion: {message.content}\n\nProduct OS Context:\n\n{context}",
            max_chars=1800,
        )
    await message.channel.send(reply)


def setup_code_pairing(bot: commands.Bot):
    """Register the /code-pair slash command."""

    @bot.tree.command(name="code-pair", description="Start a code pairing session (works in DMs too)")
    @discord.app_commands.describe(question="Your code question or what you're working on")
    async def code_pair(interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        context = "\n\n---\n\n".join([
            f"## Active Tasks\n\n{file_reader.read_tasks()}",
            f"## Goals\n\n{file_reader.read_goals()}",
            f"## Martech Stack\n\n{file_reader.read_martech_stack()}",
        ])
        reply = ask_claude(
            CODE_PAIR_SYSTEM,
            f"Reply in under 1800 characters.\n\nQuestion: {question}\n\nProduct OS Context:\n\n{context}",
            max_chars=1800,
        )
        _active_sessions.add(interaction.user.id)
        await interaction.followup.send(reply)
