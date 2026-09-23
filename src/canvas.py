"""A fixed-size character grid that frames are drawn into, then rendered to text."""

from colors import RESET

class Canvas:
    """A width x height grid of (char, ansi_color) cells."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        """reset every cell to a blank space with no color."""

        self.cells = [
            [(" ", "")] * self.width 
            for _ in range(self.height)
        ]

    def put(self, x, y, char, color=""):
        """set a single cell. out-of-bounds coordinates are silently ignored,
        since orbit math can place points outside the canvas."""
        
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x] = (char, color)

    def draw_sprite(self, sprite, center_x, center_y, color=""):
        """draw a multi-line sprite (a list of strings) centered on (center_x, center_y).

        spaces in the sprite are transparent: they leave whatever was already
        drawn underneath untouched, so sprites can be stamped down in any order.
        """

        sprite_width = max(len(row) for row in sprite)
        sprite_height = len(sprite)

        left = center_x - sprite_width // 2
        top = center_y - sprite_height // 2

        for row_offset, row in enumerate(sprite):
            for col_offset, char in enumerate(row):
                if char != " ":
                    self.put(left + col_offset, top + row_offset, char, color)


    def draw_frame(self):
        """draw a box-drawing border around the whole canvas, overwriting the edges."""

        width, height = self.width, self.height

        # top and bottom lines
        for x in range(width):
            self.cells[0][x]            = ("─", "")
            self.cells[height - 1][x]   = ("─", "")

        # left and right lines
        for y in range(height):
            self.cells[y][0]            = ("│", "")
            self.cells[y][width - 1]    = ("│", "")


        # top right and top left corner
        self.cells[0][0]            = ("┌", "")
        self.cells[0][width - 1]    = ("┐", "")

        # bottom right and bottom left corner
        self.cells[height - 1][0]           = ("└", "")
        self.cells[height - 1][width - 1]   = ("┘", "")
    
    def rows(self):
        """Render every row to a plain string, with each cell's ANSI color applied."""
        return [
            "".join(f"{color}{char}{RESET}" if color else char for char, color in row)
            for row in self.cells
        ]