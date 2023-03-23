import pygame
import threading

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
    music_volume = 1
    effect_volume = 1
    screen_scale = 1

    def __init__(self):
        self.infoObject = pygame.display.Info()
        self.start_height = self.infoObject.current_h - 100
        self.start_width = (self.start_height) / 9 * 16
        self.actual_screen = pygame.display.set_mode((self.start_width, self.start_height), pygame.RESIZABLE)
        self.screen = self.actual_screen.copy()
        self.getResizeWidth = (self.actual_screen.get_rect().height) / 9.0 * 16.0
        self.getCurrentHeight = self.actual_screen.get_rect().height
        self.centerScreenInActualScreen = (self.actual_screen.get_width() - self.getResizeWidth) / 2
        self.last_width = self.actual_screen.get_width()
        self.last_height = self.actual_screen.get_height()
        icon_img = pygame.image.load('Sprites/CrabIcon.png')
        pygame.display.set_icon(icon_img)
        pygame.display.set_caption("Crab Invaders")
        self.clock = pygame.time.Clock()

    def LoadContent(self):
        from Scenes.Stage import Stage
        from Scenes.MainMenu import MainMenu
        self.myScenes.append(MainMenu())
        self.myScenes.append(Stage())
        self.myScenes[0].LoadContent()
        self.myScenes[self.currentScene].Start()
        self.t = threading.Thread(target = self.Update)
        self.t.daemon = True

    def UpdateLoop(self):
        self.t.start()
        while self.running == True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running = False
               elif event.type == pygame.WINDOWMAXIMIZED:
                   self.ChangeScreenSize(self.infoObject.current_w , self.infoObject.current_h)
               elif event.type == pygame.VIDEORESIZE:
                   if self.last_width != event.w or self.last_height != event.h:
                       self.last_width = event.w
                       self.last_height = event.h
                       self.height = event.w / 16 * 9
                       self.ChangeScreenSize(event.w , self.height)
               elif event.type == pygame.MOUSEBUTTONDOWN and self.currentScene == 0:
                   self.myScenes[0].CheckClick()
               elif event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_TAB:
                       self.debugMode = not self.debugMode
                
            

    def Update(self):
        while self.running == True: 
            self.deltaTime = self.clock.tick(60) / 1000.0
            self.myScenes[self.currentScene].Update()
            pygame.display.update()
            self.Draw()

    def ChangeScreenSize(self, width, height):
        self.actual_screen = pygame.display.set_mode((width , height),pygame.RESIZABLE)
        self.screen_scale = float(self.actual_screen.get_height())/float(self.screen.get_height())
        self.getResizeWidth = (self.actual_screen.get_rect().height) / 9.0 * 16.0
        self.getCurrentHeight = self.actual_screen.get_rect().height
        self.centerScreenInActualScreen = (self.actual_screen.get_width() - self.getResizeWidth) / 2


    def Draw(self):
        self.myScenes[self.currentScene].Draw()
        self.actual_screen.blit(pygame.transform.scale(self.screen, ((self.getResizeWidth, self.getCurrentHeight))), (self.centerScreenInActualScreen, 0))
        pygame.display.flip()    

    def ChangeScene(self, lastScene, newScene):
        self.myScenes[lastScene].Stop()
        self.myScenes[newScene].LoadContent()
        self.myScenes[newScene].Start()
        self.currentScene = newScene

    def StartGame(self):
        self.ChangeScene(0, 1)

    def QuitGame(self):
        self.running = False
