import pygame
from Player import Player
from ImageAsset import ImageAsset
from Scenes.Stage import Stage
from Scenes.MainMenu import MainMenu

class GameWorld:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(GameWorld, cls).__new__(cls)
        return cls.instance
    
    myScenes = []
    currentScene = 0
    debugMode = False
    running = True
    deltaTime = None
    screen = None
    actual_screen = None

    def __init__(self):
        self.infoObject = pygame.display.Info()
        self.start_height = self.infoObject.current_h - 100
        self.start_width = (self.start_height) / 9 * 16
        self.actual_screen = pygame.display.set_mode((self.start_width, self.start_height), pygame.RESIZABLE)
        self.screen = self.actual_screen.copy()
        self.last_width = self.actual_screen.get_width()
        self.last_height = self.actual_screen.get_height()
        icon_img = pygame.image.load('Sprites/CrabIcon.png')
        pygame.display.set_icon(icon_img)
        pygame.display.set_caption("Crab Invaders")
        self.clock = pygame.time.Clock()

    def LoadContent(self):
        self.myScenes.append(MainMenu())
        self.myScenes.append(Stage())
        for myScene in self.myScenes:
            myScene.LoadContent()
        self.myScenes[self.currentScene].Start()

    def Update(self):
        self.deltaTime = self.clock.tick(100) / 1000.0
        
        self.myScenes[self.currentScene].Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.WINDOWMAXIMIZED:
                self.actual_screen = pygame.display.set_mode((self.infoObject.current_w , self.infoObject.current_h),pygame.RESIZABLE)
            elif event.type == pygame.VIDEORESIZE:
                if self.last_width != event.w or self.last_height != event.h:
                    self.last_width = event.w
                    self.last_height = event.h
                    self.height = event.w / 16 * 9
                    self.actual_screen = pygame.display.set_mode((event.w , self.height),pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_TAB:
                    self.debugMode = not self.debugMode
                elif event.key == pygame.K_e:
                    lastScene = self.currentScene
                    newScene = 1
                    self.ChangeScene(lastScene, newScene)
                elif event.key == pygame.K_a:
                    self.actual_screen.unlock
        return self.running

    def Draw(self):
        self.myScenes[self.currentScene].Draw()
        test = (self.actual_screen.get_rect().height + 5) / 9.0 * 16.0
        self.actual_screen.blit(pygame.transform.scale(self.screen, ((test, self.actual_screen.get_rect().height + 5))), ((self.actual_screen.get_width() - test) / 2, 0))
        pygame.display.flip()    

    def ChangeScene(self, lastScene, newScene):
        self.myScenes[lastScene].Stop()
        self.myScenes[newScene].Start()
        self.currentScene = newScene
