import pygame
from Components.Component import Component
from GameWorld import GameWorld

class Player(Component):
    def __init__(self):
        super().__init__()

    def LoadContent(self):
        super().LoadContent()
    
    def Update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move(-1)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move(1)
        super().Update()
    
    def Draw(self):
        super().Draw()
    
    def move(self, direction):
        print(GameWorld.instance.deltaTime)
        self.gameObject.transform.Translate([float(direction) * GameWorld.instance.deltaTime, 0])