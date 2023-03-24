import pygame
from Components.Component import Component
from GameWorld import GameWorld
from Objectpools.ProjectilePool import ProjectilePool
from Factories.ProjectileFactory import PROJECTILETYPE

class Player(Component):
    def __init__(self, stage):
        super().__init__()
        self.speed = 200
        self.stage = stage
        self.isAlive = True
        self.cooldown = False
        self.timeElapsed = 0.0

    def LoadContent(self):
        super().LoadContent()
    
    def Update(self):
        if self.cooldown == True:
            self.timeElapsed += GameWorld.instance.deltaTime
            if self.timeElapsed > 0.7:
                self.cooldown = False
                self.timeElapsed = 0.0

        if pygame.key.get_pressed()[pygame.K_LEFT] and self.gameObject.transform.posX > self.stage.instance.stage_left:
            self.gameObject.transform.Translate([-1, 0], self.speed)
            if self.gameObject.transform.posX < self.stage.instance.stage_left:
                self.gameObject.transform.posX = self.stage.instance.stage_left
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.gameObject.transform.posX < self.stage.instance.stage_right:
            self.gameObject.transform.Translate([1 , 0], self.speed)
            if self.gameObject.transform.posX > self.stage.instance.stage_right:
                self.gameObject.transform.posX = self.stage.instance.stage_right
        super().Update()
        
    
    def Draw(self):
        super().Draw()

    def Shoot(self):
        self.stage.myGameObjects.append(ProjectilePool().GetObject(PROJECTILETYPE.STONE, (self.gameObject.transform.posX, self.gameObject.transform.posY - 20), "Player", (0, -4)))
        self.cooldown = True
        self.timeElapsed = 0.0