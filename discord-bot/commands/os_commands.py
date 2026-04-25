import discord
from discord.ext import commands
from utils import file_reader
from utils.claude_client import ask_claude

OS_SYSTEM = (
    "You are a Product OS assistant. Be concise, direct, and use markdown. "
    "No preamble — lead with the answer."
)


def setup_os_commands(bot: commands.Bot):

    @bot.tree.command(name="today", description="Today's focus — tasks, blockers, priorities")
    async def today(interaction: discord.Interaction):
        await interaction.response.defer()
        context = f"## Active Tasks\n\n{file_reader.read_tasks()}\n\n## Goals\n\n{file_reader.read_goals()}"
        reply = ask_claude(
            OS_SYSTEM,
            f"Reply in under 800 characters. Give me today's focus: top 3 tasks to work on, any blockers to flag, and one thing I should NOT do today.\n\n{context}",
            max_chars=800,
        )
        await interaction.followup.send(reply)

    @bot.tree.command(name="roadmap", description="Milestone status, OKR alignment, risks")
    async def roadmap(interaction: discord.Interaction):
        await interaction.response.defer()
        context = "\n\n---\n\n".join([
            f"## Active Tasks\n\n{file_reader.read_tasks()}",
            f"## Backlog\n\n{file_reader.read_backlog()}",
            f"## Goals\n\n{file_reader.read_goals()}",
            f"## CDP Brief\n\n{file_reader.read_cdp_brief()}",
        ])
        reply = ask_claude(
            OS_SYSTEM,
            f"Reply in under 1200 characters. Run a roadmap review: (1) milestone status with 🟢/🟡/🔴, (2) which active tasks align to OKRs and which are orphaned, (3) top risks or blockers, (4) reprioritization suggestions.\n\n{context}",
            max_chars=1200,
        )
        await interaction.followup.send(reply)

    @bot.tree.command(name="weekly-update", description="Draft weekly status update for your manager (<300 words)")
    async def weekly_update(interaction: discord.Interaction):
        await interaction.response.defer()
        context = "\n\n---\n\n".join([
            f"## Active Tasks\n\n{file_reader.read_tasks()}",
            f"## Goals\n\n{file_reader.read_goals()}",
            f"## CDP Brief\n\n{file_reader.read_cdp_brief()}",
        ])
        reply = ask_claude(
            OS_SYSTEM,
            f"Reply in under 600 characters (300 words max). Draft my weekly status update for my manager. "
            f"Scannable bullet points. Include: completed, in progress, blockers needing manager input, decisions needed. "
            f"Use 🟢/🟡/🔴 for overall status.\n\n{context}",
            max_chars=600,
        )
        await interaction.followup.send(reply)

    @bot.tree.command(name="cdp-status", description="CDP milestone, risks, and research summary")
    async def cdp_status(interaction: discord.Interaction):
        await interaction.response.defer()
        context = "\n\n---\n\n".join([
            f"## CDP Brief\n\n{file_reader.read_cdp_brief()}",
            f"## CDP Research\n\n{file_reader.read_cdp_research()}",
            f"## CDP Reference\n\n{file_reader.read_cdp_reference()}",
        ])
        reply = ask_claude(
            OS_SYSTEM,
            f"Reply in under 900 characters. Give me a CDP status update: current phase, milestone status (🟢/🟡/🔴), top risks, and the recommended flight 1 use case with rationale.\n\n{context}",
            max_chars=900,
        )
        await interaction.followup.send(reply)

    @bot.tree.command(name="briefing", description="Full morning briefing — tasks, CDP, risks, focus")
    async def briefing(interaction: discord.Interaction):
        await interaction.response.defer()
        context = file_reader.briefing_context()
        reply = ask_claude(
            OS_SYSTEM,
            f"Reply in under 1200 characters. Give me my morning briefing: (1) Overall status 🟢/🟡/🔴, "
            f"(2) Top 3 priorities today, (3) Blockers requiring action, (4) CDP progress, (5) Suggested next command.\n\n{context}",
            max_chars=1200,
        )
        await interaction.followup.send(reply)
