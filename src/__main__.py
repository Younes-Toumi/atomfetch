"""entry point: runs the render loop until Enter is pressed or the process is interrupted."""

import select
import shutil
import sys
import time
from canvas import Canvas

from config import (
    ELECTRON,
    FRAME_DELAY,
    GAP,
    HEIGHT,
    WIDTH,
    NUCLEUS_FRAMES,
    NUCLEUS_STEP,
    NUCLEUS_COLOR,
)

from system_info import get_system_info

from examples import DEFAULT

# ANSI/VT100 control sequences, see https://vt100.net/docs/vt100-ug/chapter3.html
HOME = "\033[H"          # move cursor to row 1, col 1
CLEAR = "\033[2J"        # clear the whole screen
CLEAR_LINE = "\033[K"    # clear from cursor to end of line
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
NOWRAP = "\033[?7l"      # disable line wrap, so an over-wide line is clipped, not wrapped
WRAP = "\033[?7h"

# the alternate screen buffer has no scrollback. Drawing frames there means a
# terminal resize can never push old frames into scrollback (see the canvas
# comment in main() for why that matters).
ALT_ON = "\033[?1049h"
ALT_OFF = "\033[?1049l"

def nucleus_sprite(t):
    step = int(t / NUCLEUS_STEP)
    return NUCLEUS_FRAMES[step % len(NUCLEUS_FRAMES)]

def render_scene(canvas, orbits, t):
    """draw one full frame (orbit paths, electrons, nucleus, border) into `canvas`."""

    center_x = canvas.width // 2
    center_y = canvas.height // 2

    scale_x = canvas.width / WIDTH
    scale_y = canvas.height / HEIGHT

    canvas.clear()

    for orbit in orbits:
        for x, y, shade in orbit.path:
            canvas.put(
                round(center_x + x * scale_x),
                round(center_y + y * scale_y),
                ".",
                shade,
            )

        for x, y, shade in orbit.electrons(t):
            canvas.draw_sprite(
                ELECTRON,
                round(center_x + x * scale_x),
                round(center_y + y * scale_y),
                shade,
            )

    canvas.draw_sprite(
        nucleus_sprite(t),
        center_x,
        center_y,
        NUCLEUS_COLOR
    )

    # canvas.draw_frame()


def compose(canvas_rows, info_lines, max_rows, canvas_width):
    """zip the rendered canvas and the system-info lines into one side-by-side
    block of text, clipped to `max_rows` so it never exceeds the terminal height."""

    blank = " " * canvas_width
    lines = []

    for i in range(max(len(canvas_rows), len(info_lines))):
        left = canvas_rows[i] if i < len(canvas_rows) else blank
        right = info_lines[i] if i < len(info_lines) else ""

        lines.append(f"{left}{' ' * GAP}{right}{CLEAR_LINE}")

    return lines[:max_rows]


def main():
    info = get_system_info()
    last_frame = []

    orbits = DEFAULT

    start = time.monotonic()

    sys.stdout.write(ALT_ON + HIDE_CURSOR + NOWRAP)
    sys.stdout.flush()
    
    try:
        while True:
            # re-measured every frame so the animation adapts live if the user
            # resizes or zooms the terminal while it's running. The canvas is
            # capped at the configured WIDTH/HEIGHT and shrunk to fit smaller
            # terminals; render_scene() then scales the orbit geometry to match.
            terminal_width, terminal_height = shutil.get_terminal_size()

            canvas_width = min(terminal_width // 2, WIDTH)
            canvas_height = min(terminal_height, HEIGHT)

            canvas = Canvas(canvas_width, canvas_height)

            render_scene(canvas, orbits, time.monotonic() - start)

            last_frame = compose(canvas.rows(), info, terminal_height, canvas.width)

            sys.stdout.write(HIDE_CURSOR + HOME + "\n".join(last_frame) + HIDE_CURSOR)
            sys.stdout.flush()

            # doubles as the frame delay. returns early when Enter is pressed.
            ready, _, _ = select.select([sys.stdin], [], [], FRAME_DELAY)

            if ready:
                sys.stdin.readline()
                break

    except KeyboardInterrupt:
        pass

    finally:
        # leaving the alt screen makes the animation disappear, so the last
        # frame is reprinted once on the normal screen to leave it visible.
        sys.stdout.write(
            ALT_OFF
            + CLEAR
            + HOME
            + "\n".join(last_frame)
            + WRAP
            + SHOW_CURSOR
            + "\n"
        )
                
        sys.stdout.flush()


if __name__ == "__main__":
    main()
