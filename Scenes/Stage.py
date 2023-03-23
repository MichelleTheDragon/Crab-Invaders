from Scenes.Scene import Scene
from Components.Player import Player
from GameWorld import GameWorld
from Levels.Level1 import Level1
from Levels.Level2 import Level2
from Levels.Level3 import Level3
import pygame
from Components.SpriteRenderer import SpriteRenderer
from GameObject import GameObject
from Components.Collider import Collider
from Components.Animator import Animator

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
        self.health = 3
        self.heartObject = None
        self.missingHeartObject = None
    
    def LoadContent(self):
        background = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() / 2))
        backgroundSprite = pygame.image.load("Sprites/BeachLevel.png")
        background.AddComponent(SpriteRenderer(backgroundSprite, .92))
        self.myGameObjects.append(background)
        self.heartObject = GameObject((122,70))
        heartSprite = pygame.image.load("Sprites/Heart.png")
        self.heartObject.AddComponent(SpriteRenderer(heartSprite, .25))
        self.missingHeartObject = GameObject((122,70))
        missingHeartSprite = pygame.image.load("Sprites/LostHeart.png")
        self.missingHeartObject.AddComponent(SpriteRenderer(missingHeartSprite, .25))
        
        self.myGameObjects.append(self.LoadPlayer())

        self.bgMusic = "Sounds/CrabRave.mp3"
        self.musicVolume = 0.05

        super().LoadContent()
        self.myLevels.append(Level1())
        self.myLevels.append(Level2())
        self.myLevels.append(Level3())
        self.myLevels[0].LoadContent()
        for unitInGrid in self.myLevels[0].unitsInGrid:
            self.myGameObjects.append(unitInGrid)
            unitInGrid.GetComponent(Animator).PlayAnimation("Idle")

    def Update(self):
        super().Update()
        if self.health == 0:
            self.gameLost = True


    def Draw(self):
        super().Draw()
        for i in range(3):
            if i < self.health:
                GameWorld.instance.screen.blit(self.heartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))
            else:
                GameWorld.instance.screen.blit(self.missingHeartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))

    def ChangeLevel(self, current):
        if current < len(self.myLevels):
            self.myLevels[current + 1].LoadContent()

    def LoadPlayer(self):
        player = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() - 100))
        player.tag = "Player"
        playerSprite = pygame.image.load("Sprites/player.png")
        spriteRenderer = SpriteRenderer(playerSprite, 0.8)
        player.AddComponent(spriteRenderer)
        player.AddComponent(Collider(player, spriteRenderer, 3, (-20, 0)))
        player.AddComponent(Player(self))
        return player
    
