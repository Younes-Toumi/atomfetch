"""Fetches the system-info panel shown next to the animation."""

import subprocess

def get_system_info():
    """Return Neofetch output as a list of lines."""
    result = subprocess.run(
        ["neofetch", "--off"],
        capture_output=True,
        text=True,
    )

    return result.stdout.splitlines()