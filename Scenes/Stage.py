from Scenes.Scene import Scene
from Components.Player import Player
from GameWorld import GameWorld
from Levels.Level1 import Level1
import pygame
from Components.SpriteRenderer import SpriteRenderer
from GameObject import GameObject
from Components.Collider import Collider

class Stage(Scene):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(Stage, cls).__new__(cls)
        return cls.instance
    
    stage_left = GameWorld.instance.screen.get_width() / 2 - 380
    stage_right = GameWorld.instance.screen.get_width() / 2 + 380
    

    def __init__(self):
        super().__init__()
        self.myLevels = []
        self.currentLevel = 0
        self.health = 2
        self.heartObject = None
        self.missingHeartObject = None
    
    def LoadContent(self):
        background = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() / 2))
        background.AddComponent(SpriteRenderer("Sprites/BeachLevel.png", .92))
        self.myGameObjects.append(background)
        #self.myGameObjects.append(ImageAsset("Sprites/BeachLevel.png", (GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() / 2), .92))
        
        player = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() - 100))
        player.tag = "Player"
        spriteRenderer = SpriteRenderer("Sprites/player.png", 0.8)
        player.AddComponent(spriteRenderer)
        player.AddComponent(Collider(player, spriteRenderer, 2, (0, 0)))
        player.AddComponent(Player())
        self.myGameObjects.append(player)
        #self.myGameObjects.append(Player("Sprites/player.png", (GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() - 100)))

        self.bgMusic = "Sounds/CrabRave.mp3"

        self.heartObject = GameObject((122,70))
        self.heartObject.AddComponent(SpriteRenderer("Sprites/Heart.png", .25))
        self.missingHeartObject = GameObject((122,70))
        self.missingHeartObject.AddComponent(SpriteRenderer("Sprites/LostHeart.png", .25))
        #ImageAsset("Sprites/Heart.png", (122, 70), .25)
        #self.missingHeartObject = ImageAsset("Sprites/LostHeart.png", (122, 70), .25)
        self.musicVolume = 0.05
        super().LoadContent()
        self.myLevels.append(Level1())
        self.myLevels[0].LoadContent()
        #testing = 0
        for unitInGrid in self.myLevels[0].unitsInGrid:
            #testing += 1
            self.myGameObjects.append(unitInGrid)
            #unitInGrid.transform.posX = GameWorld.instance.screen.get_width() / 2 - 440 + 80 * testing
            #unitInGrid.transform.posY = 70

    def Update(self):
        super().Update()


    def Draw(self):
        super().Draw()
        for i in range(3):
            if i < self.health:
                GameWorld.instance.screen.blit(self.heartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))
            else:
                GameWorld.instance.screen.blit(self.missingHeartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))