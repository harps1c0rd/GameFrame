from GameFrame import RoomObject, Globals
from Objects.Net import Net
from Objects.Hostage import Hostage
import random

class Bad(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("badman.png")
        self.set_image(image,135,165)

        # set inital movement
        self.y_speed = random.choice([-10,10])

        # start asteroid timer
        net_spawn_time = random.randint(15,150)
        self.set_timer(net_spawn_time, self.spawn_net)

    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
        
    def spawn_net(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_net = Net(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_net)
        
        # reset time for next Asteroid spawn
        net_spawn_time = random.randint(15, 150)
        self.set_timer(net_spawn_time, self.spawn_net)

        # start hostage timer
        hostage_spawn_time = random.randint(30, 200)
        self.set_timer(hostage_spawn_time, self.spawn_hostage)

    def spawn_hostage(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn hostage and add to room
        new_hostage = Hostage(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_hostage)
        
        # reset timer for next hostage spawn
        hostage_spawn_time = random.randint(30, 200)
        self.set_timer(hostage_spawn_time, self.spawn_hostage)