import curses
from curses import color_pair
from .position import Position
from .element import Element


class Text(Element):
    def __init__(self, content: str, position: Position):
        super().__init__(position)
        self.text = content
        "The text displayed and stored."
        self.size = Position(len(content), 0)
        "The calculated size of the text."
        self.end = self.start + self.size
        "The position of the last character in the text."
        self.underlined = False
        "Whether the text should be underlined."
        self.calc_pack()

    def set_text(self, text: str):
        """Set the text of the current text element and update its size, this will not redraw the text element.

        Args:
            text (str): the new text
        """
        if self.region is None:
            return
        self.text = text
        self.size = Position(len(self.text), 0)
        self.end = self.start + self.size

    def click(self):
        """What happens when the text is clicked (if there is a callback on the element)

        This will do nothing if you do not add it to a region using Region.add_region().
        """
        if self.region is None or self.hidden:
            return
        self.callback(self)

    def draw(self):
        """Draw this text to the screen.

        This will do nothing if you do not add it to a region using Region().add_element()..
        """
        if self.region is None or self.hidden:
            return
        options = color_pair(self.color)
        if self.underlined:
            options += curses.A_UNDERLINE
        self.addstr(self.start.y, self.start.x,
                    self.text, options)
