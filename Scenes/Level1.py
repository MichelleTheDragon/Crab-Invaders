from Scenes.Scene import Scene
from Player import Player
from ImageAsset import ImageAsset

class Level1(Scene):
    def __init__(self, myWorld):
        super().__init__(myWorld)
    
    def LoadContent(self):
        self.myGameObjects.append(Player("Sprites/player.png", self.myWorld.infoObject.current_w / 2, self.myWorld.infoObject.current_h - 150))
        self.myGameObjects.append(ImageAsset("Sprites/enemy_01.png", self.myWorld.infoObject.current_w / 2, 150, 0.5))

    def Update(self, deltaTime, debugMode):
        return super().Update(deltaTime, debugMode)

    def Draw(self, screen, debugMode):
        screen.fill((100,130,210))
        return super().Draw(screen, debugMode)