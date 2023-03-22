from Levels.Level import Level
from Enemies.BasicEnemy1 import BasicEnemy1
from GameWorld import GameWorld
from Objectpools.EnemyPool import EnemyPool
from Factories.EnemyFactory import ENEMYTYPE

class Level1(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = ""
        self.groupWidth = 7
        self.groupHeight = 5
        
    def LoadContent(self):
        self.unitsInGrid.append(EnemyPool().GetObject(ENEMYTYPE.BASIC))
        #for row in self.unitsInGrid:
        #    self.SpawnRow(row)