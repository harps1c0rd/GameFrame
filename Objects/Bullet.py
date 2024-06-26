from GameFrame import RoomObject, Globals

class Bullet(RoomObject):
    """
    Class for the bullet shot by the dude
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the bullet
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("bullet.png")
        self.set_image(image, 33, 9)
        
        # set movement
        self.set_direction(0, 20)
        
        # handle events
        self.register_collision_object("Net")
        self.register_collision_object("Hostage")

    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

    # --- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Net":
            self.room.net_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Hostage":
            self.room.hostage_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(-10)