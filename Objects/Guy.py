from GameFrame import RoomObject, Globals
from Objects.Bullet import Bullet
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
        
        self.can_shoot = True

    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10
        if key[pygame.K_SPACE]:
            self.shoot_bullet()

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

    def shoot_bullet(self):
        """
        Shoots a laser from the ship
        """
        new_bullet = Bullet(self.room, 
                          self.x + self.width, 
                          self.y + self.height/2 - 4)
        self.room.add_room_object(new_bullet)

        if self.can_shoot:
            new_bullet = Bullet(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_bullet)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            self.room.shoot_bullet.play()
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True