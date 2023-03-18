from GameObject import GameObject
import pygame
import GameWorld
from Components.SpriteRenderer import SpriteRenderer
from Components.Component import Component

class Player(Component):
    def __init__(self, sprite, position):
        self.gameObject = GameObject(position)
        self.gameObject.AddComponent(SpriteRenderer(self.gameObject, sprite, 0.8))
        self.gameObject.AddComponent(self)

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
        self.gameObject.transform.Translate([direction * 3, 0])