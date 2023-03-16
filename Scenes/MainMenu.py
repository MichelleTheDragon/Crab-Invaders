from Scenes.Scene import Scene
from ImageAsset import ImageAsset
import pygame

class MainMenu(Scene):
    def __init__(self, myWorld):
        super().__init__(myWorld)
    
    def LoadContent(self):
        self.myGameObjects.append(ImageAsset("Sprites/Background.jpg", self.myWorld.infoObject.current_w / 2, self.myWorld.infoObject.current_h / 2, 1))
        self.bgMusic = "Sounds/Menu.mp3"
        super().LoadContent()

    def Update(self, deltaTime, debugMode):
        return super().Update(deltaTime, debugMode)

    def Draw(self, screen, debugMode):
        return super().Draw(screen, debugMode)