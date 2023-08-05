import curses
from curses import color_pair

from .position import Position
from .text import Text
from .element import Element


class Checkbox(Element):

    def __init__(self, checked: bool, position: Position, callback=lambda _: ()):
        super().__init__(position)
        self.checked = checked
        "Whether its checked or not"
        self.colors = [204, 156]
        "[Off, On] colors respectively. Feel free to change them."
        self.callback = callback
        "The method to call when the checkbox is clicked."
        self.spacing = False
        "Is it spaced?"
        self.calc_size()

    @property
    def color(self):
        "Returns a color_pair color code, depending on what state the checkbox is in [Off, On]. The setter for this does nothing."
        return self.colors[self.checked]

    @color.setter
    def color(self, value):
        return

    def calc_size(self):
        """Recalculate an elements relative placement packing."""
        self.size = Position(3, 1)
        if self.spacing:
            self.size += Position(2, 0)
        self.end = self.start + self.size
        self.calc_pack()

    def spaced(self, spacing: bool):
        """Controls whether there is space around the x in the checkbox.

        [ x ] True
        [x] False - Default
        Args:
            spacing (bool): Whether to space the checkbox.
        """
        self.spacing = spacing
        self.calc_size()

    def draw(self):
        """Draw this text to the screen.

        This will do nothing if you do not add it to a region using Region().add_element()..
        """
        if self.region is None or self.hidden:
            return
        color = self.colors[self.checked]
        options = color_pair(color)

        checkbox = [
            "[",
            "x" if self.checked else " ",
            "]"
        ]
        if self.spacing:
            checkbox.insert(1, " ")
            checkbox.insert(3, " ")

        self.addstr(self.start.y, self.start.x,
                    "".join(checkbox), options)

    def click(self):
        """What happens when the checkbox is clicked

        This will do nothing if you do not add it to a region using Region.add_region().
        """
        if self.region is None or self.hidden:
            return
        self.checked = not self.checked
        if self.callback is not None:
            self.callback(self)
