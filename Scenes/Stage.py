from Scenes.Scene import Scene
from Player import Player
from ImageAsset import ImageAsset
import GameWorld
from Levels.Level1 import Level1

class Stage(Scene):
    def __init__(self):
        super().__init__()
        self.myLevels = []
    
    def LoadContent(self):
        self.myGameObjects.append(ImageAsset("Sprites/Background.jpg", (GameWorld.GameWorld.instance.screen.get_width() / 2, GameWorld.GameWorld.instance.screen.get_height() / 2), .92))
        self.myGameObjects.append(Player("Sprites/player.png", (GameWorld.GameWorld.instance.screen.get_width() / 2, GameWorld.GameWorld.instance.screen.get_height() - 150)))
        self.bgMusic = "Sounds/CrabRave.mp3"
        self.audioVolume = 0.05
        super().LoadContent()
        #self.myGameObjects.append(ImageAsset("Sprites/enemy_01.png", self.myWorld.infoObject.current_w / 2, 150, 0.5))
        #self.myLevels.append(Level1())

    def Update(self):
        super().Update()

    def Draw(self):
        #GameWorld.GameWorld.instance.screen.fill((100,130,210))
        super().Draw()