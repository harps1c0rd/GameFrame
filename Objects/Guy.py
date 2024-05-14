from GameFrame import RoomObject, Globals
import pygame

class Dude(RoomObject):
    """
    A class for the player's avatar (the dude)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the dude object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("theguy.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10

    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height

    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()