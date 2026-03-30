import discord
from discord.ext import commands
from utils.file_writer import append_task, create_meeting_note


def setup_capture_commands(bot: commands.Bot):

    @bot.tree.command(name="add-task", description="Add a task to active.md")
    @discord.app_commands.describe(
        description="Task description",
        priority="Priority: p0, p1, or p2 (default: p1)",
        tag="Tag e.g. cdp, martech, roadmap (optional)",
    )
    async def add_task(
        interaction: discord.Interaction,
        description: str,
        priority: str = "p1",
        tag: str = "",
    ):
        if priority not in ("p0", "p1", "p2"):
            await interaction.response.send_message(
                "Priority must be p0, p1, or p2.", ephemeral=True
            )
            return
        result = append_task(description, priority, tag)
        await interaction.response.send_message(f"✓ {result}")

    @bot.tree.command(name="note", description="Save a quick note to Meetings/_temp")
    @discord.app_commands.describe(
        title="Note title (e.g. '[your-manager]-sync', 'cdp-idea')",
        content="Note content",
    )
    async def note(interaction: discord.Interaction, title: str, content: str):
        result = create_meeting_note(title, content)
        await interaction.response.send_message(f"✓ {result}")
