import pygame
from Components.Component import Component
from GameWorld import GameWorld

class Player(Component):
    def __init__(self, stage):
        super().__init__()
        self.speed = 200
        self.stage = stage

    def LoadContent(self):
        super().LoadContent()
    
    def Update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.gameObject.transform.posX > self.stage.instance.stage_left:
            self.gameObject.transform.Translate([-1, 0], self.speed)
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.gameObject.transform.posX < self.stage.instance.stage_right:
            self.gameObject.transform.Translate([1 , 0], self.speed)
        super().Update()
    
    def Draw(self):
        super().Draw()