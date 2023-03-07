import pygame
from abc import ABC, abstractmethod
import inspect

class GameObject(ABC):
    @abstractmethod
    def __init__(self, sprite, posX, posY, hasCollider):
        self.components = []
        self.sprite_image, self.sprite = GameObject.buildSprite(sprite)
        self.posX = posX
        self.posY = posY
        self.hasCollider = hasCollider
        self.color = (255, 255, 255)

    @abstractmethod
    def LoadContent(self):
        pass

    @abstractmethod
    def Update(self, deltaTime, debugMode):
        if debugMode == True and self.hasCollider == True:
            point = pygame.mouse.get_pos()
            self.collider = pygame.Rect(self.posX - self.sprite.rect.x/2, self.posY - self.sprite.rect.y/2, self.sprite_image.get_rect().width, self.sprite_image.get_rect().height)
            collide = self.collider.collidepoint(point)
            self.color = (255, 0, 0) if collide else (255, 255, 255)

    @abstractmethod
    def Draw(self, screen, debugMode):
        screen.blit(self.sprite_image, (self.posX - self.sprite.rect.x/2, self.posY - self.sprite.rect.y/2))
        if debugMode == True and self.hasCollider == True:
            pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.sprite.rect.x/2 - 5, 2)

    def buildSprite(path):
        sprite_image = pygame.image.load(path)
        sprite = pygame.sprite.Sprite()
        sprite.rect = sprite_image.get_rect()
        sprite.rect.x = sprite_image.get_width()
        sprite.rect.y = sprite_image.get_height()
        return sprite_image, sprite