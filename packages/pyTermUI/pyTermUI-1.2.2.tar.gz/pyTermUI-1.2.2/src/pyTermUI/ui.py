import curses
import time
from .region import Region
from .position import Position
from .textbox import Textbox


class UI:
    """The main UI component
    """
    count = 0
    screen_initialized = False
    last_element_clicked = 0
    clickable_cooldown = 300
    last_cursor_pos = (0, 0)
    "The amount of the time in milliseconds between registered clicks. default is 300"

    @staticmethod
    def init_screen():
        """Initialize the curses screen. This will happen the first time any UI is created. This also adds color support.
        """
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        curses.mousemask(1)
        # Initialize color pairs
        for i in range(0, curses.COLORS):
            if i < 255:
                curses.init_pair(i + 1, i, -1)
        UI.screen_initialized = True

    def __init__(self, stdscr):
        self.window = stdscr
        self.id = UI.count

        self.screen = Position(120, 30)
        self.half = self.screen.half()
        self._active = False
        self.default_color = 232
        self.draw_callback = None
        self.event_callback = None

        self.regions = []
        
        self.cursor = Position(0,0)
        if not UI.screen_initialized:
            UI.init_screen()
        UI.count += 1

    """
    This setter functions as the second half of deactivate and activate, it will hold the UI instance open until the new UI takes over
    """
    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value
        if self._active:
            self.draw()
            self.loop()

    def activate(self):
        """Show the UI and begin its loop.
        """
        self.active = True

    def deactivate(self):
        """Hide the UI and end its loop.
        """
        self.active = False

    def add_region(self, region: Region):
        """Add a region to the UI

        Args:
            region (Region): The region to add
        """
        self.regions.append(region)
        region.ui = self
        if region.color == -1:
            region.color = self.default_color
            region.echo_color()
        self.draw()

    def swap(self, new_ui):
        """
        Swap control of the main UI loop to another UI object.

        This will also hide the current UI, and reveal the new UI as only one can be active at a time.

        Args:
            new_ui (UI): The UI object to give control too
        """
        self.deactivate()
        new_ui.activate()

    def resize(self):
        """Resize the UI
        """
        x, y = self.window.getmaxyx()[::-1]
        curses.curs_set(0)
        curses.resize_term(y, x)
        self.window.clear()
        self.screen = Position(x, y)
        self.half = self.screen.half()
        self.draw()

    def get_clickable(self, position: Position):
        # I am sorry.
        for region in self.regions:
            if region.inBounds(position):
                for element in region.elements:
                    if element.callback is not None:
                        if element.in_bounds(position):
                            UI.last_element_clicked = time.time()*1000
                            element.click()
                            return element
        return None

    def loop(self):
        """
        ? Description:
        * * The main UI loop
        """
        while self.active:
            event = self.window.getch()
            if event == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                if time.time()*1000 - UI.last_element_clicked >= UI.clickable_cooldown:
                    position = Position(mx, my)
                    element = self.get_clickable(position)
                    if type(element) not in [Textbox, type(None)]:
                        self.draw()
            if event == curses.KEY_RESIZE:
                y, x = self.window.getmaxyx()
                curses.resize_term(y, x)
                self.draw()
            if self.event_callback is not None:
                self.event_callback(event)

    def set_curs(self):
        x, y = self.cursor.x, self.cursor.y
        
        curses.setsyx(y,x)

    def draw(self):
        """
        ? Description:
        * * Draw the current UI to the terminal
        """
        if self.active:
            self.window.clear()
            for region in self.regions:
                region.draw()
            self.window.noutrefresh()
            self.set_curs()
            curses.doupdate()
            if self.draw_callback is not None:
                self.draw_callback()
