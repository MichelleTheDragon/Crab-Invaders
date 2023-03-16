from GameObject import GameObject
import pygame

class Player(GameObject):
    def __init__(self, sprite, posX, posY):
        super().__init__(sprite, posX, posY, True, 1)

    def LoadContent(self):
        return super().LoadContent()
    
    def Update(self, deltaTime, debugMode):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move(-deltaTime)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move(deltaTime)
        return super().Update(deltaTime, debugMode)
    
    def Draw(self, screen, debugMode):
        return super().Draw(screen, debugMode)
    
    def move(self, deltaTime):
        self.posX += deltaTime * 300