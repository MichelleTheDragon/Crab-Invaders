import pygame
import copy
from Components.Transform import Transform
import GameWorld


class GameObject:
    def __init__(self, position):#, sprite, posX, posY, hasCollider, scale):
        self.transform = Transform(position)
        self.components = []
        self.tag = ""
        #self.scale = scale
        #self.sprite_image, self.sprite = self.buildSprite(sprite)
        #self.posX = posX
        #self.posY = posY
        #self.hasCollider = hasCollider
        #self.color = (255, 255, 255)

    def LoadContent(self):
        for component in self.components:
            component.LoadContent()

    def Update(self):
        for component in self.components:
            component.Update()
        #if GameWorld().debugMode == True and self.hasCollider == True:
        #    point = pygame.mouse.get_pos()
        #    self.collider = pygame.Rect(self.posX - self.sprite.rect.x/2, self.posY - self.sprite.rect.y/2, self.sprite_image.get_rect().width, self.sprite_image.get_rect().height)
        #    collide = self.collider.collidepoint(point)
        #    self.color = (255, 0, 0) if collide else (255, 255, 255)

    def Draw(self):
        for component in self.components:
            component.Draw()
        #screen.blit(self.sprite_image, (self.posX - self.sprite.rect.x/2, self.posY - self.sprite.rect.y/2))
        #if debugMode == True and self.hasCollider == True:
        #    pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.sprite.rect.x/2 - 5, 2)

    def AddComponent(self, component):
        component.GameObject = self
        self.components.append(component)
        return component
    
    def GetComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return component
            
    def HasComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return True
        return False
    
    def Clone(self):
        gameObject = GameObject()
        for component in self.components:
            gameObject.AddComponent(component.Clone())
        return gameObject


    #def buildSprite(self, path):
    #    sprite_image = pygame.image.load(path)
    #    sprite = pygame.sprite.Sprite()
    #    sprite.rect = sprite_image.get_rect()
    #    sprite.rect.x = sprite_image.get_width() * self.scale
    #    sprite.rect.y = sprite_image.get_height() * self.scale
    #    return sprite_image, sprite