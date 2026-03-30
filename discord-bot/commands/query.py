import discord
from discord.ext import commands
from utils import file_reader
from utils.claude_client import ask_claude

RICHARD_SYSTEM = (
    "You are Richard Ng's Product OS assistant. Richard is a Martech PM at Kpay. "
    "Answer questions using only the context provided. Be concise and direct. "
    "If the answer is not in the context, say so clearly."
)


def setup_query_commands(bot: commands.Bot):

    @bot.tree.command(name="ask", description="Ask a question about your Product OS")
    @discord.app_commands.describe(question="Your question")
    async def ask(interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        context = "\n\n---\n\n".join([
            f"## Active Tasks\n\n{file_reader.read_tasks()}",
            f"## Goals\n\n{file_reader.read_goals()}",
            f"## CDP Brief\n\n{file_reader.read_cdp_brief()}",
            f"## CDP Research\n\n{file_reader.read_cdp_research()}",
            f"## Martech Stack\n\n{file_reader.read_martech_stack()}",
        ])
        reply = ask_claude(
            RICHARD_SYSTEM,
            f"Reply in under 1000 characters. Question: {question}\n\nContext from Product OS:\n\n{context}",
            max_chars=1000,
        )
        await interaction.followup.send(reply)
