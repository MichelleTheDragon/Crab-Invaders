from Components.Component import Component
import pygame
import GameWorld

class SpriteRenderer(Component):
    def __init__(self, gameObject, path, scale):
        super().__init__()
        self.gameObject = gameObject
        self.scale = scale
        self.sprite_image = pygame.image.load(path)
        self.sprite_image = pygame.transform.smoothscale(self.sprite_image, (self.sprite_image.get_width() * self.scale, self.sprite_image.get_height() * self.scale))
        self.sprite = pygame.sprite.Sprite()
        self.sprite.rect = self.sprite_image.get_rect()
        self.sprite.rect.x = self.sprite_image.get_width() 
        self.sprite.rect.y = self.sprite_image.get_height() 
        self.origin = (0,0)
        self.color = (255, 255, 255)

    def Start(self):
        self.origin = (self.sprite.rect.x / 2, self.sprite.rect.y / 2)

    def Draw(self):
        GameWorld.GameWorld.instance.screen.blit(self.sprite_image, (self.gameObject.transform.posX - self.sprite.rect.x/2, self.gameObject.transform.posY - self.sprite.rect.y/2))
        #if GameWorld.GameWorld.instance.debugMode == True and hasCollider == True:
        #    pygame.draw.circle(GameWorld.GameWorld.instance.screen, self.color, (self.posX, self.posY), self.sprite.rect.x/2 - 5, 2)
