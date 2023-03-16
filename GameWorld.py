import pygame
from Player import Player
from ImageAsset import ImageAsset
from Scenes.Level1 import Level1
from Scenes.MainMenu import MainMenu

class GameWorld:
    def __init__(self):
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h), pygame.FULLSCREEN)
        pygame.display.set_caption("Crab Invaders")
        self.myScenes = []
        self.currentScene = 0
        self.clock = pygame.time.Clock()
        self.debugMode = False

    def LoadContent(self):
        self.myScenes.append(MainMenu(self))
        self.myScenes.append(Level1(self))
        self.running = True
        for myScene in self.myScenes:
            myScene.LoadContent()

    def Update(self):
        deltaTime = self.clock.tick(60) / 1000.0
        
        self.myScenes[self.currentScene].Update(deltaTime, self.debugMode)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_TAB:
                    self.debugMode = not self.debugMode
                elif event.key == pygame.K_e:
                    self.currentScene = 1
        return self.running

    def Draw(self):
        self.myScenes[self.currentScene].Draw(self.screen, self.debugMode)
        pygame.display.update()    
