from Components.Component import Component
from GameWorld import GameWorld
import Scenes.Stage 
import pygame
import math

class Collider(Component):
    def __init__(self, gameObject, spriteRenderer, mode, offset):
        super().__init__()
        self.gameObject = gameObject
        self.spriteRenderer = spriteRenderer
        self.offset = offset
        self.loaded = False
        self.color = (255, 255, 255)
        self.mode = mode
        self.rect = self.GetRectangle(spriteRenderer, offset)

    def GetRectangle(self, spriteRenderer, offset):
        return [self.gameObject.transform.posX, self.gameObject.transform.posY, spriteRenderer.sprite.rect.x + offset[0], spriteRenderer.sprite.rect.y + offset[1]]

    def ChangeSprite(self, offset):
        self.offset = offset

    def Update(self):        
        for other in Scenes.Stage.Stage.instance.myGameObjects:
            for enemyTag in self.gameObject.enemyTags:
                if other.tag == enemyTag:
                    calcDist = math.dist((self.gameObject.transform.posX, self.gameObject.transform.posY), (other.transform.posX, other.transform.posY))
                    collisonDist = (other.GetComponent(Collider).rect[2] / 2 + self.rect[2] / 2)
                    if calcDist < collisonDist:
                        if other.tag == "Enemy":
                            #other.GetComponent(Enemy).isAlive = False
                            Scenes.Stage.Stage.instance.CrabHit(other)
                        elif other.tag == "Player":
                            Scenes.Stage.Stage.instance.PlayerHit()
                            #Scenes.Stage.Stage.instance.myGameObjects.remove(other)
                        if self.gameObject.tag == "Projectile":
                            if self.gameObject.isAlive == True and other.isAlive == True:
                                Scenes.Stage.Stage.instance.myGameObjects.remove(self.gameObject)
                            self.gameObject.isAlive = False

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