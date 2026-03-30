import subprocess
import config


def ask_claude(system_prompt: str, user_message: str, max_chars: int = 1800) -> str:
    """Run Claude Code as a subprocess and return the response."""
    full_prompt = f"{system_prompt}\n\n{user_message}"
    result = subprocess.run(
        [config.CLAUDE_BIN, "-p", "--model", config.CLAUDE_MODEL, full_prompt],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        error = result.stderr.strip() or "Unknown error"
        return f"[Claude Code error: {error}]"
    output = result.stdout.strip()
    if len(output) > max_chars:
        output = output[:max_chars] + "\n…(truncated)"
    return output
