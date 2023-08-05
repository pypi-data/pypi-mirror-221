import curses
from .position import Position


class Element:
    """
    ? Description
    * * An element that exists within a region
    """

    def __init__(self, start: Position):
        self.region = None  # the region it resides in
        self.start = start
        self.hidden = False
        self.end = None
        self.size = None
        self.color = -1
        self.callback = None
        self.data = {}

    def in_bounds(self, position: Position) -> bool:
        """Checks if a position is in bounds

        Args:
            position (Position): the position to check
        """

        x, y = position.x, position.y

        def in_x_bound():
            return self.start.x <= x <= self.end.x

        def in_y_bound():
            return self.start.y <= y <= self.end.y

        return in_x_bound() and in_y_bound()

    def addstr(self, y: int, x: int, string: str, options=0):
        """Shorthand helper function to add a string to the screen

        Args:
            y (int): Row value
            x (int): Column value
            string (str): The string to add
            options (int, optional): Other options: color, formatting, etc. Defaults to 0.
        """
        if y >= curses.LINES-1 or x >= curses.COLS-1:
            return
        self.region.ui.window.addstr(y, x, string, options)

    def move(self, position: Position):
        """Move a element

        Args:
            position (Position): The new position
        """
        self.start = position
        self.end = position + self.size
        self.calc_pack()

    def resize(self, position: Position):
        """Resize a element

        Args:
            position (Position): The new size.
        """
        self.size = position
        self.end = position + self.start
        self.calc_pack()

    def calc_pack(self):
        """Recalculate an elements relative placement packing."""
        self.pack = {
            "right": Position(
                self.size.x+self.start.x+1, self.start.y),
            "down": Position(self.start.x, self.start.y+self.size.y+1),
            "up": Position(self.start.x, self.start.y-1)
        }

    def event_mask(self, *args):
        """An event mask for allowing other elements click events to emulate a click on this element. 

        This should only be used as a callback for another element.

        Useful for making labels.
        """
        self.click()
