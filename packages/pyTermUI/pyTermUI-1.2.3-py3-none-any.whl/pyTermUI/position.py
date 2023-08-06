
import math


class Position:
    """Custom positioning object, very barebones and simple.

    Supports addition and subtraction between other positioning objects.

    And a custom .half() method which returns half of the position rounded down.
    """

    @classmethod
    def DEFAULT_TERM_SIZE(cls):
        "Return a position equal to the default terminal size on most operating systems. Equivalent to Position(108,28)"
        return cls(108, 28)

    @classmethod
    def ORIGIN(cls):
        "Return a position that will place an object in its parents origin, the top left corner. Equivalent to Position(0,0)"
        return cls(0, 0)

    def __init__(self, x: int = 0, y: int = 0, xypair: tuple = None):
        if xypair:
            self.x, self.y = xypair
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x+other.x, self.y+other.y)
        return self

    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.x-other.x, self.y-other.y)
        return self

    def half(self):
        """Returns a position equal to half of the current, on both y and x

        Returns:
            Position: The calculated position, rounded down
        """
        return Position(math.floor(self.x/2), math.floor(self.y/2))
