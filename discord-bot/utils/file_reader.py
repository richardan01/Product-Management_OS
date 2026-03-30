from pathlib import Path
import config


def read_file(path: Path) -> str:
    """Read a markdown file, return empty string if not found."""
    if not path.exists():
        return f"[File not found: {path.name}]"
    return path.read_text(encoding="utf-8")


def read_tasks() -> str:
    return read_file(config.TASKS_ACTIVE)


def read_backlog() -> str:
    return read_file(config.TASKS_BACKLOG)


def read_goals() -> str:
    return read_file(config.GOALS)


def read_cdp_brief() -> str:
    return read_file(config.CDP_BRIEF)


def read_cdp_research() -> str:
    return read_file(config.CDP_RESEARCH)


def read_cdp_reference() -> str:
    return read_file(config.CDP_REFERENCE)


def read_martech_stack() -> str:
    return read_file(config.MARTECH_STACK)


def briefing_context() -> str:
    """Combine all key files for a full morning briefing."""
    sections = [
        ("Active Tasks", read_tasks()),
        ("Goals & OKRs", read_goals()),
        ("CDP Brief", read_cdp_brief()),
        ("CDP Research", read_cdp_research()),
    ]
    return "\n\n---\n\n".join(f"## {title}\n\n{content}" for title, content in sections)
