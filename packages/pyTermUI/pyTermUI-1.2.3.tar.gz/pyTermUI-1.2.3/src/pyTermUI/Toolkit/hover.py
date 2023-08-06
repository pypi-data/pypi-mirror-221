from curses import getmouse
from threading import Thread
import time

from datetime import datetime

from ..position import Position
from ..element import Element

class Hover:
    """A handler for on_hover events for elements.
    """
    
    wait = .125
    "The wait to check for hover events"
    
    def __init__(self):
        self.elements = []
        self.threads = []
        self.last = {}
        self.terminate = False
        
    def add(self, element: Element, on_hover, off_hover):
        """Add an element with a callback to the hover event

        Args:
            element (Element): The element you want to watch for hovers
            callback (function): The callback to run when the element is hovered
        """
        self.elements.append({"obj": element, "on_hover": on_hover, "off_hover": off_hover})
    
    def __check_hover(self):
        while not self.terminate:
            _, mx, my, _, _ = getmouse()
            position = Position(mx, my)
            # has the mouse moved out of the last hover?
            if self.last:
                if not self.last.get("obj").in_bounds(position):
                    self.last.get("off_hover")(self.last.get("obj"))
                    
            
            # check for a new hover if the mouse has left the last hover.
            for element in self.elements:
                if element.get("obj").region.visible and element.get("obj").region.ui.active and element.get("obj").in_bounds(position):
                    element.get("on_hover")(element.get("obj"))
                    self.last = element
                    continue
            
            time.sleep(Hover.wait)
                    
    def end(self):
        "Kill all hover threads"
        if not self.terminate:
            self.terminate = True
            for thread in self.threads:
                thread.join()
            now = datetime.now()
        
    
    def build(self):
        "Build the main thread handler"
        
        if self.terminate:
            self.end()
            self.terminate = False
        self.threads = []
        
        thread = Thread(target=self.__check_hover, args=())
        
        self.threads.append(thread)
    
    def run(self):
        """Run the handler."""
        
        for thread in self.threads: 
            thread.start()