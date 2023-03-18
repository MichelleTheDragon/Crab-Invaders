from Scenes.Scene import Scene
from ImageAsset import ImageAsset
import pygame
import GameWorld

class MainMenu(Scene):
    def __init__(self):
        super().__init__()
    
    def LoadContent(self):
        self.myGameObjects.append(ImageAsset("Sprites/BeachArt.jpg", (GameWorld.GameWorld.instance.screen.get_width() / 2, GameWorld.GameWorld.instance.screen.get_height() / 2), .7))
        self.bgMusic = "Sounds/Menu.mp3"
        self.audioVolume = 0.2
        super().LoadContent()

    def Update(self):
        super().Update()

    def Draw(self):
        super().Draw()