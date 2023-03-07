import pygame
from Player import Player
from ImageAsset import ImageAsset

class GameWorld:
    def __init__(self):
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h))#, pygame.FULLSCREEN)
        pygame.display.set_caption("Space Invaders")
        #self.screen.fill((100,130,210))
        self.myGameObjects = []
        self.myScenes = []
        self.clock = pygame.time.Clock()
        self.debugMode = False

    def LoadContent(self):
        self.background = ImageAsset("Sprites/Background.jpg", self.infoObject.current_w / 2, self.infoObject.current_h / 2)
        self.myGameObjects.append(Player("Sprites/player.png", self.infoObject.current_w / 2, self.infoObject.current_h - 150))
        pygame.mixer.music.load("Sounds/Menu.mp3")
        self.running = True
        pygame.mixer.music.play(-1)

    def Update(self):
        deltaTime = self.clock.tick(60) / 1000.0
        
        for myGameObject in self.myGameObjects:
            myGameObject.Update(deltaTime, self.debugMode)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_TAB:
                    self.debugMode = not self.debugMode
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.myGameObjects[0].move(-deltaTime)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.myGameObjects[0].move(deltaTime)
        return self.running

    def Draw(self):
        #self.screen.fill((155,155,255))
        self.background.Draw(self.screen)
        for myGameObject in self.myGameObjects:
            myGameObject.Draw(self.screen, self.debugMode)
        pygame.display.update()    
