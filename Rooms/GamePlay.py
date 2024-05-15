from GameFrame import Level, Globals
from Objects.Guy import Dude
from Objects.Badman import Bad
from Objects.Hud import Score
from Objects.Hud import Score, Lives

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

        # add objects
        self.add_room_object(Dude(self, 25, 50))
        self.add_room_object(Bad(self,1120, 50))

        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)

        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)

        # load sound files
        self.shoot_bullet = self.load_sound("bullet.mp3")
        self.net_shot = self.load_sound("net_shot.mp3")
        self.hostage_saved = self.load_sound("hostage_saved.mp3")
        self.net_collision = self.load_sound("dude_damage.mp3")
        self.hostage_shot = self.load_sound("hostage_hit.mp3")