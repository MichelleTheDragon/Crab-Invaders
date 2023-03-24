import pygame
import threading

class GameWorld:
    #Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(GameWorld, cls).__new__(cls)
        return cls.instance
    
    #Static variables
    myScenes = []
    currentScene = 0
    debugMode = False #Shows colliders
    running = True #This variable decides if the game runs of stops
    deltaTime = None 
    screen = None #The screen everything is drawn on
    actual_screen = None #The screen the player sees
    music_volume = 1
    effect_volume = 1
    screen_scale = 1 #The scale diference between the drawn screen and the actual screen

    def __init__(self):
        #Set up screen
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

        #Add Icon
        icon_img = pygame.image.load('Sprites/CrabIcon.png')
        pygame.display.set_icon(icon_img)
        #Add Title
        pygame.display.set_caption("Crab Invaders")
        
        #Set Clock for deltaTime
        self.clock = pygame.time.Clock()

        #import and add scenes
        from Scenes.Stage import Stage
        from Scenes.MainMenu import MainMenu
        self.myScenes.append(MainMenu())
        self.myScenes.append(Stage())

        #Create Thread
        self.t = threading.Thread(target = self.Update)
        self.t.daemon = True

    def LoadContent(self):
        #Load Main Menu
        self.myScenes[0].LoadContent()
        self.myScenes[0].Start()

    def UpdateLoop(self):
        #Start running the thread that contains everythin but the game events, because events are very heavy on performance
        self.t.start()

        while self.running == True:
            #All Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Exit button in corner clicked
                    self.running = False
                elif event.type == pygame.WINDOWMAXIMIZED: #If the window gets maximized, change the screen content
                    self.ChangeScreenSize(self.infoObject.current_w , self.infoObject.current_h)
                elif event.type == pygame.VIDEORESIZE: #If the window size gets changed, change the screen, but uphold aspect ratio
                    if self.last_width != event.w or self.last_height != event.h:
                        self.last_width = event.w
                        self.last_height = event.h
                        self.height = event.w / 16 * 9
                        self.ChangeScreenSize(event.w , self.height)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.currentScene == 0: #If mouse is clicked in Main Menu
                    self.myScenes[0].CheckClick()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.currentScene == 1: #If mouse if clicked in the game scene, after the player has died
                    if self.myScenes[1].hasDied == True:
                        self.myScenes[1].CheckClick()
                elif event.type == pygame.KEYDOWN: #If a key is pressed down
                    if event.key == pygame.K_TAB: #If Tab is pressed toggle debugMode (Shows Colliders)
                        self.debugMode = not self.debugMode
                    if event.key == pygame.K_SPACE and self.currentScene == 1: #If Space is pressed in the game scene, shoot
                        if self.myScenes[1].hasDied == False:
                            player = self.myScenes[1].myPlayer
                            if player.cooldown == False :
                                player.Shoot()

                
    def Update(self):
        while self.running == True: 
            self.deltaTime = self.clock.tick(60) / 1000.0 #Set deltaTime (time since last Update)
            self.myScenes[self.currentScene].Update() #Update current Scene
            pygame.display.update()
            self.Draw()

    #Change the screen size and aspect ratio
    def ChangeScreenSize(self, width, height):
        self.actual_screen = pygame.display.set_mode((width , height),pygame.RESIZABLE)
        self.screen_scale = float(self.actual_screen.get_height())/float(self.screen.get_height())
        self.getResizeWidth = (self.actual_screen.get_rect().height) / 9.0 * 16.0
        self.getCurrentHeight = self.actual_screen.get_rect().height
        self.centerScreenInActualScreen = (self.actual_screen.get_width() - self.getResizeWidth) / 2

    def Draw(self):
        self.myScenes[self.currentScene].Draw() #Draw current Scene
        #Draw on the screen a scaled version of the scene
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
