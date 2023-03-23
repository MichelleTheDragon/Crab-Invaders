from Components.Component import Component
import pygame
from GameWorld import GameWorld

class SpriteRenderer(Component):
    def __init__(self, sprite, scale):
        super().__init__()
        self.scale = scale
        self.offset = (0,0)
        self.sprite_image = sprite
        self.sprite_image = pygame.transform.smoothscale(self.sprite_image, (self.sprite_image.get_width() * self.scale, self.sprite_image.get_height() * self.scale))
        self.sprite = pygame.sprite.Sprite()
        self.sprite.rect = self.sprite_image.get_rect()
        self.sprite.rect.x = self.sprite_image.get_width() 
        self.sprite.rect.y = self.sprite_image.get_height() 
        self.origin = (0,0)
        self.color = (255, 255, 255)

    def ChangeSprite(self, sprite):
        self.sprite_image = sprite
        self.sprite_image = pygame.transform.smoothscale(self.sprite_image, (self.sprite_image.get_width() * self.scale, self.sprite_image.get_height() * self.scale))

    def Start(self):
        self.origin = (self.sprite.rect.x / 2, self.sprite.rect.y / 2)

    def Draw(self):
        GameWorld.instance.screen.blit(self.sprite_image, (self.gameObject.transform.posX - self.sprite.rect.x/2 + self.offset[0], self.gameObject.transform.posY - self.sprite.rect.y/2 + self.offset[1]))