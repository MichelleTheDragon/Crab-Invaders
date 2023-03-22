import math
from GameWorld import GameWorld

class Transform:
    def __init__(self, position):
        self.tag = ""
        self.posX = position[0]
        self.posY = position[1]

    def Translate(self, translation):
        self.posX += translation[0] * GameWorld.instance.deltaTime * 100
        self.posY += translation[1] * GameWorld.instance.deltaTime * 100