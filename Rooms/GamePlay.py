from GameFrame import Level
from Objects.Guy import Dude
from Objects.Badman import Bad

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

        # add objects
        self.add_room_object(Dude(self, 25, 50))
        self.add_room_object(Bad(self,1120, 50))

