from datetime import datetime
from pathlib import Path
import config


def append_task(description: str, priority: str = "p1", tag: str = "") -> str:
    """Append a new task to Tasks/active.md under the In Progress section."""
    tag_str = f" #{tag}" if tag else ""
    new_task = f"\n- [ ] **{description}** #{priority}{tag_str}\n"

    content = config.TASKS_ACTIVE.read_text(encoding="utf-8")

    # Insert after "## In Progress" heading
    marker = "## In Progress"
    if marker in content:
        insert_at = content.index(marker) + len(marker)
        updated = content[:insert_at] + new_task + content[insert_at:]
    else:
        updated = content + new_task

    config.TASKS_ACTIVE.write_text(updated, encoding="utf-8")
    return f"Task added: **{description}** #{priority}{tag_str}"


def create_meeting_note(name: str, content: str) -> str:
    """Create a timestamped meeting note in Meetings/_temp or Meetings/."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_name = name.lower().replace(" ", "-")
    filename = f"{date_str}-{safe_name}.md"

    target_dir = config.TEMP_DIR if config.TEMP_DIR.exists() else config.MEETINGS_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    note_path = target_dir / filename
    note_path.write_text(
        f"# Note: {name}\n**Date:** {date_str}\n\n{content}\n",
        encoding="utf-8",
    )
    return f"Note saved to `{note_path.relative_to(config.MY_OS)}`"
