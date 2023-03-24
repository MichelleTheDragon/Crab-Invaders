from Scenes.Scene import Scene
from Components.Player import Player
from Components.Enemy import Enemy
from GameWorld import GameWorld
from Levels.Level1 import Level1
from Levels.Level2 import Level2
from Levels.Level3 import Level3
from Levels.Level4 import Level4
from Levels.Level5 import Level5
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
    
    #Set the sideways borders for where the player and enemies can move to
    stage_left = GameWorld.instance.screen.get_width() / 2 - 380
    stage_right = GameWorld.instance.screen.get_width() / 2 + 380
    

    def __init__(self):
        super().__init__()
        self.myLevels = []
        self.heartObject = None
        self.missingHeartObject = None
        self.myPlayer = None

        #Set up text
        scoreTextFont = pygame.font.SysFont('Arial',40)
        self.scoreText = scoreTextFont.render('SCORE:' , True , (255,255,255))
        self.scoreValueFont = pygame.font.SysFont('Arial',40)
        self.scoreValue = self.scoreValueFont.render(str(0) , True , (255,255,255))
        self.finalScore = self.scoreValueFont.render("N/A" , True , (0,0,0))
        buttonFont = pygame.font.SysFont('Arial',35)
        self.restartButtonText = buttonFont.render('RESTART' , True , (255,255,255))
        self.menuButtonText = buttonFont.render('MENU' , True , (255,255,255))

        #set up buttons
        self.buttonWidth = 250
        self.buttonHeight = 50
        self.buttonHeightPush = 35
        buttonBackgroundWidth = 650
        buttonBackgroundHeight = 200
        self.buttonBackground = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - buttonBackgroundWidth / 2, GameWorld.instance.actual_screen.get_height() / 2 - buttonBackgroundHeight / 2, buttonBackgroundWidth, buttonBackgroundHeight)
        self.restartCollider = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - self.buttonWidth / 2 - 150, GameWorld.instance.actual_screen.get_height() / 2 - self.buttonHeight / 2 + self.buttonHeightPush, self.buttonWidth, self.buttonHeight)
        self.menuCollider = pygame.Rect(GameWorld.instance.actual_screen.get_width() / 2 - self.buttonWidth / 2 + 150, GameWorld.instance.actual_screen.get_height() / 2 - self.buttonHeight / 2 + self.buttonHeightPush, self.buttonWidth, self.buttonHeight)
        self.buttonBaseColour = (104,166,195)
        self.buttonHoverColour = (53,134,172)
        self.restartButtonColour = self.buttonBaseColour
        self.menuButtonColour = self.buttonBaseColour
        
        #set up sound
        self.click_sound = pygame.mixer.Sound("Sounds/MenuClick.wav")
        self.click_sound.set_volume(0.2)
    
    def LoadContent(self):
        self.myGameObjects = []
        self.health = 3
        self.currentLevel = 0
        self.score = 0
        self.timeElapsed = 0.0
        self.moveDown = False
        self.loadingLevel = False

        #set up background
        background = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() / 2))
        backgroundSprite = pygame.image.load("Sprites/BeachLevel.png")
        background.AddComponent(SpriteRenderer(backgroundSprite, .92))
        self.myGameObjects.append(background)

        #set up hearts
        self.heartObject = GameObject((122,70))
        heartSprite = pygame.image.load("Sprites/Heart.png")
        self.heartObject.AddComponent(SpriteRenderer(heartSprite, .25))
        self.missingHeartObject = GameObject((122,70))
        missingHeartSprite = pygame.image.load("Sprites/LostHeart.png")
        self.missingHeartObject.AddComponent(SpriteRenderer(missingHeartSprite, .25))
        
        #Add a player
        self.myGameObjects.append(self.LoadPlayer())

        #set music
        self.bgMusic = "Sounds/CrabRave.mp3"
        self.musicVolume = 0.05
        self.crabDeathSound = pygame.mixer.Sound("Sounds/CrabDeath.mp3")
        self.crabDeathSound.set_volume(1)
        self.owwSound = pygame.mixer.Sound("Sounds/Oww.mp3")
        self.owwSound.set_volume(0.3)
        
        #crab movement
        self.movingDir = 1
        self.crabSpeed = 0.6

        super().LoadContent()

        #Add all Levels
        self.myLevels.append(Level1())
        self.myLevels.append(Level2())
        self.myLevels.append(Level3())
        self.myLevels.append(Level4())
        self.myLevels.append(Level5())
        self.LoadLevel(self.currentLevel) #Load the First Level

    #Load a level
    def LoadLevel(self, level):
        self.moveDown = False #Make sure the crabs don't instantly moves down
        self.myLevels[level].LoadContent(self) #Load the content of the level
        if len(self.myLevels[level].bgMusic) > 0: #If the level contains music, play it
            self.myLevels[level].StartLevel()
            pygame.mixer.music.fadeout(10000) #Fade out current music
        for unitInGrid in self.myLevels[level].unitsInGrid: #Add all basic units to the scene
            self.myGameObjects.append(unitInGrid)
            unitInGrid.GetComponent(Animator).PlayAnimation("Idle", False)
        for mySpecialUnit in self.myLevels[level].mySpecialUnits: #Add all special units to the scene
            self.myGameObjects.append(mySpecialUnit)
        self.loadingLevel = False 

    def Update(self):
        super().Update()
        if self.hasDied == False and self.loadingLevel == False:
            self.timeElapsed += GameWorld.instance.deltaTime
            if self.timeElapsed > self.crabSpeed: #Every X time move the crabs
                self.MoveCrabs()
                self.timeElapsed = 0.0

        #If the player has died, show the end screen
        if self.hasDied == True:
            point = pygame.mouse.get_pos()

            #calculate screen center position and width
            calc_height = self.buttonHeight * GameWorld.instance.screen_scale
            calc_width = self.buttonWidth * GameWorld.instance.screen_scale
            calc_left = GameWorld.instance.actual_screen.get_width() / 2 - calc_width / 2
            calc_top = GameWorld.instance.actual_screen.get_height() / 2 - calc_height / 2 + self.buttonHeightPush * GameWorld.instance.screen_scale
            calc_disToCenter = 150 * GameWorld.instance.screen_scale

            #Check Mouse point Collision with rectangles
            self.scaledRestartCollider = pygame.Rect(calc_left - calc_disToCenter, calc_top, calc_width, calc_height)
            self.scaledMenuCollider = pygame.Rect(calc_left + calc_disToCenter, calc_top, calc_width, calc_height)
            self.collideRestart = self.scaledRestartCollider.collidepoint(point)
            self.collideMenu = self.scaledMenuCollider.collidepoint(point)
            self.restartButtonColour = self.CheckMouseCollision(self.collideRestart)
            self.menuButtonColour = self.CheckMouseCollision(self.collideMenu)


    def Draw(self):
        super().Draw()
        
        #Draw Hearts
        for i in range(3):
            if i < self.health:
                GameWorld.instance.screen.blit(self.heartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.heartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))
            else:
                GameWorld.instance.screen.blit(self.missingHeartObject.GetComponent(SpriteRenderer).sprite_image, (110 + 215/2 * i - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.x/2, 90 - self.missingHeartObject.GetComponent(SpriteRenderer).sprite.rect.y/2))
        
        #Draw Score
        GameWorld.instance.screen.blit(self.scoreText , (GameWorld.instance.screen.get_width() - 380, 40))
        GameWorld.instance.screen.blit(self.scoreValue , (GameWorld.instance.screen.get_width() - 50 - self.scoreValue.get_rect().w, 40))
        
        #Draw end screen
        if self.hasDied == True:
            pygame.draw.rect(GameWorld.instance.screen, (222,246,255), self.buttonBackground)
            GameWorld.instance.screen.blit(self.finalScore , (GameWorld.instance.screen.get_width() / 2 - self.finalScore.get_rect().w / 2, GameWorld.instance.screen.get_height() / 2 - self.finalScore.get_rect().h / 2 - 50))
            pygame.draw.rect(GameWorld.instance.screen, self.restartButtonColour, self.restartCollider)
            GameWorld.instance.screen.blit(self.restartButtonText , (self.restartCollider.width/2 + self.restartCollider.x - self.restartButtonText.get_rect().w / 2, self.restartCollider.height/2 + self.restartCollider.y - self.restartButtonText.get_rect().h / 2))
            pygame.draw.rect(GameWorld.instance.screen, self.menuButtonColour, self.menuCollider)
            GameWorld.instance.screen.blit(self.menuButtonText , (self.menuCollider.width/2 + self.menuCollider.x - self.menuButtonText.get_rect().w / 2, self.menuCollider.height/2 + self.menuCollider.y - self.menuButtonText.get_rect().h / 2))
    
    def CheckClick(self):
        if self.collideRestart == True: #Restart game
            pygame.mixer.Sound.play(self.click_sound)
            self.LoadContent()
        elif self.collideMenu == True: #Go to Main Menu
            pygame.mixer.Sound.play(self.click_sound)
            GameWorld.instance.currentScene = 0
            GameWorld.instance.LoadContent()

    def ChangeLevel(self, current):
        if current < len(self.myLevels):
            self.myLevels[current + 1].LoadContent()

    #Create the player
    def LoadPlayer(self):
        player = GameObject((GameWorld.instance.screen.get_width() / 2, GameWorld.instance.screen.get_height() - 100))
        player.tag = "Player"
        playerSprite = pygame.image.load("Sprites/CrabIcon.png") #Temporary sprite
        spriteRenderer = SpriteRenderer(playerSprite, 0.2)
        player.AddComponent(spriteRenderer)
        player.AddComponent(Collider(player, spriteRenderer, 3, (-20, 0)))
        self.myPlayer = Player(self)
        player.AddComponent(self.myPlayer)
        return player
    
    #If a crab has been hit, check if it has died, if it has remove it from the scene
    def CrabHit(self, gameObject):
        pygame.mixer.Sound.play(self.crabDeathSound)
        if gameObject.GetComponent(Enemy).CheckAlive() == 0:
            self.score += gameObject.GetComponent(Enemy).point_value * (self.currentLevel + 1)
            self.scoreValue = self.scoreValueFont.render(str(self.score), True, (255,255,255))
            self.myGameObjects.remove(gameObject)

    def MoveCrabs(self):
        leftmostCrabPosX = GameWorld.instance.screen.get_width() / 2
        rightmostCrabPosX = GameWorld.instance.screen.get_width() / 2
        crabs = []
        #Add all crabs to a list and find the side borders of the group 
        for gameObject in self.myGameObjects:
            if gameObject.tag == "Enemy":
                if gameObject.transform.posX < leftmostCrabPosX:
                    leftmostCrabPosX = gameObject.transform.posX
                elif gameObject.transform.posX > rightmostCrabPosX:
                    rightmostCrabPosX = gameObject.transform.posX
                crabs.append(gameObject)
        
        #Move the crabs
        if len(crabs) > 0:
            if self.moveDown == True:
                for crab in crabs:
                    crab.transform.posY += 40
                self.moveDown = False
            elif self.movingDir > 0:
                if rightmostCrabPosX >= self.stage_right:
                    self.movingDir = -1
                    self.moveDown = True
                else:
                    for crab in crabs:
                        crab.transform.Translate((30, 0), 7)
            elif self.movingDir < 0: 
                if leftmostCrabPosX <= self.stage_left:
                    self.movingDir = 1
                    self.moveDown = True
                else:
                    for crab in crabs:
                        crab.transform.Translate((-30, 0), 7)
        elif self.loadingLevel == False: #if there are no more crabs, load next level
            self.loadingLevel = True
            if self.currentLevel < len(self.myLevels) - 1:
                self.currentLevel += 1
                self.LoadLevel(self.currentLevel)
            
    #If the player gets hit, play a sound, and if they died, stop the game and show the end screen
    def PlayerHit(self):
        pygame.mixer.Sound.play(self.owwSound)
        self.health -= 1
        if self.health == 0:
            self.hasDied = True
            self.finalScore = self.scoreValueFont.render("Final Score: " + str(self.score), True, (0,0,0))

    #Check mouse point collsions with buttons
    def CheckMouseCollision(self, myBool):
        if myBool == True:
            return self.buttonHoverColour
        return self.buttonBaseColour
