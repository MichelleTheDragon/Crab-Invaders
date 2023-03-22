from Components.Component import Component
from GameWorld import GameWorld
#from Scenes.Stage import Stage
import pygame

class Collider(Component):
    def __init__(self, gameObject, spriteRenderer, mode, offset):
        super().__init__()
        self.gameObject = gameObject
        self.spriteRenderer = spriteRenderer
        self.offset = offset
        self.loaded = False
        self.color = (255, 255, 255)
        self.mode = mode

    def GetRectangle(self, spriteRenderer, offset):
        return [self.gameObject.transform.posX, self.gameObject.transform.posY, spriteRenderer.sprite.rect.x + offset[0], spriteRenderer.sprite.rect.y + offset[1]]

    def ChangeSprite(self, offset):
        self.offset = offset

    def Update(self):
        pass
        #point = pygame.mouse.get_pos()
        #self.collider = pygame.Rect(self.gameObject.transform.posX - self.spriteRenderer.sprite.rect.x/2, self.gameObject.transform.posY - self.spriteRenderer.sprite.rect.y/2, self.spriteRenderer.sprite_image.get_rect().width, self.spriteRenderer.sprite_image.get_rect().height)
        #collide = self.collider.colliderect(point)
        #self.color = (255, 0, 0) if collide == True else (255, 255, 255)
        
        #for other in Stage.instance.myGameObjects:
        #    for enemyTag in self.gameObject.enemyTags:
        #        if other.tag == enemyTag and other.

    def Draw(self):
        if GameWorld.instance.debugMode == True:
            self.rect = self.GetRectangle(self.spriteRenderer, self.offset)
            match self.mode:
                case 1:
                    pygame.draw.rect(GameWorld.instance.screen, self.color, (self.rect[0] - self.rect[2]/2, self.rect[1] - self.rect[3]/2, self.rect[2], self.rect[3]), 2)
                case 2:
                    pygame.draw.ellipse(GameWorld.instance.screen, self.color, (self.rect[0] - self.rect[2]/2, self.rect[1] - self.rect[3]/2, self.rect[2], self.rect[3]), 2)
                case 3:
                    pygame.draw.circle(GameWorld.instance.screen, self.color, (self.rect[0], self.rect[1]), self.rect[2] / 2, 2)