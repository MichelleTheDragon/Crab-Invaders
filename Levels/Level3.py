from Levels.Level import Level
from GameWorld import GameWorld
from Objectpools.EnemyPool import EnemyPool
from Factories.EnemyFactory import ENEMYTYPE

class Level3(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = ""
        self.groupWidth = 7
        self.groupHeight = 5
        self.rowType = [ENEMYTYPE.TOUGH, ENEMYTYPE.TOUGH, ENEMYTYPE.ADVANCED, ENEMYTYPE.ADVANCED, ENEMYTYPE.ADVANCED]
        
    def LoadContent(self):
        for column in range(self.groupHeight):
            for row in range(self.groupWidth):
                self.unitsInGrid.append(EnemyPool().GetObject(self.rowType[column], (GameWorld.instance.screen.get_width() / 2 - 380 + row * 80, 50 + 70 * column)))