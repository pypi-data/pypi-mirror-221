import curses
from enum import Enum
from .position import Position
from .element import Element


class Region:
    """A area in a UI used to display elements
    """
    count = 0

    def __init__(self, title: str, position: Position, size: Position):
        self.ui = None
        "The UI its contained in."
        self.start = position
        "The top left corner."
        self.size = size-Position(1, 1)
        "The length / width of the region as a Position object."
        self.end = position + (size-Position(1, 1))
        "The bottom right corner."
        self.color = -1
        "The color of the region. Defaults to the UI color."
        self.text = title
        "The title at the top of the region."
        self.framed = True
        "Whether the regions borders are drawn. Defaults to True"
        self.visible = True
        "Whether the region is draw at all. Defaults to true."
        self.elements = []
        "The elements in the region. Only manipulate this if you know what you are doing."
        self.sOrigin = Position(
            self.start.x+1, self.start.y+1)
        "The relative starting location (inside the top left corner.)"
        self.eOrigin = Position(
            self.end.x-1, self.end.y-1)
        "The relative ending location (inside the bottom right corner.)"
        self.calc_pack()

    def set_text(self, text: str):
        """Change the name of this region

        Args:
            text (str): the new name of the region
        """
        self.text = text

    def move(self, size: Position):
        """Move a element

        Args:
            position (Position): The new position
        """
        self.start = size
        self.end = size + self.size
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
        """Recalculate the regions relative placement packing."""
        self.pack = {
            "right": Position(
                self.size.x+self.start.x+1, self.start.y),
            "down": Position(self.start.x, self.start.y+self.size.y+1),
            "up": Position(self.start.x, self.start.y-1),
            "left": Position(self.start.x-1, self.start.y)
        }

    def draw(self):
        """Draw this region to the screen.

        This will do nothing if you do not add it to a UI using UI().add_region()
        """

        if self.ui is None:
            return

        # * Initialize the corners of the box

        if self.framed:
            self.addstr(self.start.y, self.start.x,
                        BoxCharacters.TOPLEFT.value, curses.color_pair(self.color))
            self.addstr(self.start.y, self.end.x,
                        BoxCharacters.TOPRIGHT.value, curses.color_pair(self.color))
            self.addstr(self.end.y, self.start.x,
                        BoxCharacters.BOTTOMLEFT.value, curses.color_pair(self.color))
            self.addstr(self.end.y, self.end.x,
                        BoxCharacters.BOTTOMRIGHT.value, curses.color_pair(self.color))

            # * Create vertical lines
            for iy in range(self.end.y-self.start.y):
                if 0 < iy < self.end.y:
                    self.addstr(iy+self.start.y, self.start.x,
                                BoxCharacters.VERTICAL.value, curses.color_pair(self.color))
                    self.addstr(
                        iy+self.start.y, self.end.x, BoxCharacters.VERTICAL.value, curses.color_pair(self.color))

            # * Create horizontal lines
            title_offset = 2
            for ix in range(self.end.x-self.start.x):
                if 0 < ix < self.end.x:
                    char = BoxCharacters.HORIZONTAL.value
                    # * Add our title to our top horizontal line
                    if title_offset < ix < len(self.text)+(title_offset+1):
                        char = self.text[ix-(title_offset+1)]
                    self.addstr(self.start.y, ix+self.start.x,
                                char, curses.color_pair(self.color))
                    self.addstr(
                        self.end.y, ix+self.start.x, BoxCharacters.HORIZONTAL.value, curses.color_pair(self.color))

        # * Draw our elements into the region
        for element in self.elements:
            element.draw()

    def hidden(self, visibility: bool) -> bool:
        """Allows you to set the visibility of a region

        NO ELEMENTS INSIDE WILL BE RENDERED IF THIS IS FALSE, If you would like to hide JUST the title and frame, you can change Region().framed to false

        Args:
            visibility (bool): True for visible, False for invisible

        Returns:
            bool: _description_
        """
        self.visible = visibility

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
        self.ui.window.addstr(y, x, string, options)

    def error(self, text: str):
        """Clear the screen and dump the curses cache to send an error, this will end the current ui instance.

        Args:
            text (str): the text to send in the error message
        """
        self.ui.window.clear()
        self.ui.deactivate()
        self.ui.window.nodelay(True)
        self.ui.window.keypad(1)
        curses.curs_set(1)
        print(text)

    def echo_color(self):
        """
        Set all element colors to the region color if the element color is unset
        """
        for element in self.elements:
            if element.color == -1:
                element.color = self.color

    def add_element(self, element: Element):

        self.elements.append(element)
        element.region = self
        if element.color == -1:
            element.color = self.color
        element.start += self.sOrigin
        element.end = element.start + element.size

    def inBounds(self, position: Position) -> bool:
        """Check if a position is within the bounds of this object

        Args:
            position (tuple): the position to check

        Returns:
            bool: True if inside region, otherwise False
        """
        x, y = position.x, position.y

        def in_x_bound():
            return self.start.x < x < self.end.x

        def in_y_bound():
            return self.start.y < y < self.end.y

        return in_x_bound() and in_y_bound()


class BoxCharacters(Enum):
    TOPLEFT = "╭"
    TOPRIGHT = "╮"
    BOTTOMLEFT = "╰"
    BOTTOMRIGHT = "╯"
    HORIZONTAL = "─"
    VERTICAL = "│"
