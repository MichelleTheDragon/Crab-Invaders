import math
from GameWorld import GameWorld

class Transform:
    def __init__(self, position):
        self.tag = ""
        self.posX = position[0]
        self.posY = position[1]

    def Translate(self, translation, speed):
        self.posX += float(translation[0] * GameWorld.instance.deltaTime * speed)
        self.posY += float(translation[1] * GameWorld.instance.deltaTime * speed)