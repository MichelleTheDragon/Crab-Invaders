from Levels.Level import Level
from GameWorld import GameWorld
from Objectpools.EnemyPool import EnemyPool
from Factories.EnemyFactory import ENEMYTYPE
import pygame

class Level5(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = ""
        
    def LoadContent(self, stage):
        print("Level5: Boss")
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.BOSS2, (GameWorld.instance.screen.get_width() / 2, 50), stage))
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.BOSS1, (GameWorld.instance.screen.get_width() / 2 - 200, 150), stage))
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.BOSS1, (GameWorld.instance.screen.get_width() / 2 + 200, 150), stage))
