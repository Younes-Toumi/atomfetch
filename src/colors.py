"""ANSI truecolor helpers for shading sprites by depth."""

RESET = "\033[0m"


def hex_to_rgb(hex_color):
    """convert a "#rrggbb" string to an (r, g, b) tuple of ints."""

    hex_color = hex_color.lstrip("#")

    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def make_shades(hex_color, levels=24):
    """build a gradient of `levels` ANSI truecolor escape codes for one color.

    index 0 is the dimmest (25% brightness) and the last index is full
    brightness. Used to fake depth: points further from the viewer get a
    darker shade of the orbit's color.
    """

    r, g, b = hex_to_rgb(hex_color)
    shades = []

    for i in range(levels):
        brightness = 0.25 + 0.75 * i / (levels - 1)
        shades.append(f"\033[38;2;{int(r * brightness)};{int(g * brightness)};{int(b * brightness)}m")

    return shades
