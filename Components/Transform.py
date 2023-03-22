import math
from GameWorld import GameWorld

class Transform:
    def __init__(self, position):
        self.tag = ""
        self.posX = position[0]
        self.posY = position[1]

    def Translate(self, translation):
        self.posX += float(translation[0] / 10)
        self.posY += float(translation[1] / 10)