from GameFrame import RoomObject
import random

class Net(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the net object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("net.png")
        self.set_image(image,50,49)

        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, 10)
