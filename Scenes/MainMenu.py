from Scenes.Scene import Scene
import pygame
from GameWorld import GameWorld
import sys
from GameObject import GameObject
from Components.SpriteRenderer import SpriteRenderer

class MainMenu(Scene):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(MainMenu, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()
        
        #Set up text
        BigTextFont = pygame.font.SysFont('Arial',55)
        self.optionsText = BigTextFont.render('OPTIONS' , True , (255,255,255))
        buttonFont = pygame.font.SysFont('Arial',35)
        self.startButtonText = buttonFont.render('START' , True , (255,255,255))
        self.optionsButtonText = buttonFont.render('OPTIONS' , True , (255,255,255))
        self.quitButtonText = buttonFont.render('QUIT' , True , (255,255,255))
        self.backButtonText = buttonFont.render('BACK' , True , (255,255,255))

        #Set up button colours
        self.buttonBaseColour = (164,226,255)
        self.buttonHoverColour = (83,164,202)
        self.startButtonColour = self.buttonBaseColour
        self.optionsButtonColour = self.buttonBaseColour
        self.quitButtonColour = self.buttonBaseColour
        self.backButtonColour = self.buttonBaseColour

        #Set collider state for buttons
        self.collideStart = False
        self.collideOptions = False
        self.collideQuit = False
        self.collideBack = False

        self.buttonWidth = 250
        self.page = 0 #decides which group of elements are currently on screen
    
    def LoadContent(self):
        #set background
        background = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() / 2))
        backgroundSprite = pygame.image.load("Sprites/BeachArt.png")
        background.AddComponent(SpriteRenderer(backgroundSprite, .7))
        self.myGameObjects.append(background)

        #set music and sounds
        self.bgMusic = "Sounds/Menu.mp3"
        self.musicVolume = 0.2
        self.click_sound = pygame.mixer.Sound("Sounds/MenuClick.wav")
        self.click_sound.set_volume(self.musicVolume )

        #set up button rectangles
        self.startCollider = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - self.buttonWidth / 2, GameWorld.instance.actual_screen.get_height() / 2 - 85, self.buttonWidth, 50)
        self.optionsCollider = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - self.buttonWidth / 2, GameWorld.instance.actual_screen.get_height() / 2 - 25, self.buttonWidth, 50)
        self.quitCollider = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - self.buttonWidth / 2, GameWorld.instance.actual_screen.get_height() / 2 + 35, self.buttonWidth, 50)
            
        self.backCollider = pygame.Rect(GameWorld.instance.screen.get_width() / 2 - self.buttonWidth / 2, GameWorld.instance.screen.get_height() / 2 + 95, self.buttonWidth, 50)
        super().LoadContent()

    def Update(self):
        super().Update()
        point = pygame.mouse.get_pos() #get mouse position

        #calculate screen center position and width
        calc_height = 50 * GameWorld.instance.screen_scale
        calc_width = self.buttonWidth * GameWorld.instance.screen_scale
        calc_left = GameWorld.instance.actual_screen.get_width() / 2 - calc_width / 2
        calc_top = GameWorld.instance.actual_screen.get_height() / 2 - calc_height / 2

        #Check Mouse point Collision with rectangles
        if self.page == 0:
            self.scaledStartCollider = pygame.Rect(calc_left, calc_top - 60  * GameWorld.instance.screen_scale, calc_width, calc_height)
            self.scaledOptionsCollider = pygame.Rect(calc_left, calc_top, calc_width, calc_height)
            self.scaledQuitCollider = pygame.Rect(calc_left, calc_top + 60 * GameWorld.instance.screen_scale, calc_width, calc_height)
            self.collideStart = self.scaledStartCollider.collidepoint(point)
            self.collideOptions = self.scaledOptionsCollider.collidepoint(point)
            self.collideQuit = self.scaledQuitCollider.collidepoint(point)

            self.startButtonColour = self.CheckCollision(self.collideStart)
            self.optionsButtonColour = self.CheckCollision(self.collideOptions)
            self.quitButtonColour = self.CheckCollision(self.collideQuit)

        elif self.page == 1:
            self.scaledBackCollider = pygame.Rect(calc_left, calc_top + 120 * GameWorld.instance.screen_scale, calc_width, calc_height)
            self.collideBack = self.scaledBackCollider.collidepoint(point)
            self.backButtonColour = self.CheckCollision(self.collideBack)

    def Draw(self):
        GameWorld.instance.screen.fill((0,0,0))
        super().Draw()

        #Draw buttons
        if self.page == 0:
            pygame.draw.rect(GameWorld.instance.screen, self.startButtonColour, self.startCollider)
            GameWorld.instance.screen.blit(self.startButtonText , (self.startCollider.width/2 + self.startCollider.x - self.startButtonText.get_rect().w / 2, self.startCollider.height/2 + self.startCollider.y - self.startButtonText.get_rect().h / 2))
            pygame.draw.rect(GameWorld.instance.screen, self.optionsButtonColour, self.optionsCollider)
            GameWorld.instance.screen.blit(self.optionsButtonText , (self.optionsCollider.width/2 + self.optionsCollider.x - self.optionsButtonText.get_rect().w / 2, self.optionsCollider.height/2 + self.optionsCollider.y - self.optionsButtonText.get_rect().h / 2))
            pygame.draw.rect(GameWorld.instance.screen, self.quitButtonColour, self.quitCollider)
            GameWorld.instance.screen.blit(self.quitButtonText , (self.quitCollider.width/2 + self.quitCollider.x - self.quitButtonText.get_rect().w / 2, self.quitCollider.height/2 + self.quitCollider.y - self.quitButtonText.get_rect().h / 2))
        elif self.page == 1:
            GameWorld.instance.screen.blit(self.optionsText , (self.optionsCollider.width/2 + self.optionsCollider.x - self.optionsText.get_rect().w / 2, 300))
            pygame.draw.rect(GameWorld.instance.screen, self.backButtonColour, self.backCollider)
            GameWorld.instance.screen.blit(self.backButtonText , (self.backCollider.width/2 + self.backCollider.x - self.backButtonText.get_rect().w / 2, self.backCollider.height/2 + self.backCollider.y - self.backButtonText.get_rect().h / 2))
            
    #Check if mouse was over a button when clicked
    def CheckClick(self):
        if self.collideStart == True:
            self.Click()
            GameWorld.instance.StartGame()
        elif self.collideOptions == True:
            self.Click()
            self.collideOptions = False
            self.page = 1
        elif self.collideQuit == True:
            GameWorld.instance.QuitGame()
        elif self.collideBack == True:
            self.Click()
            self.collideBack = False
            self.page = 0

    #Check mouse collsion, if true change button colour to match
    def CheckCollision(self, myBool):
        if myBool == True:
            return self.buttonHoverColour
        return self.buttonBaseColour
    
    #Button click sound
    def Click(self):
        pygame.mixer.Sound.play(self.click_sound)
    