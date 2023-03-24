from Levels.Level import Level
from GameWorld import GameWorld
from Objectpools.EnemyPool import EnemyPool
from Factories.EnemyFactory import ENEMYTYPE

class Level2(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = ""
        self.groupWidth = 7
        self.groupHeight = 5
        self.rowType = [ENEMYTYPE.TOUGH, ENEMYTYPE.ADVANCED, ENEMYTYPE.ADVANCED, ENEMYTYPE.BASIC, ENEMYTYPE.BASIC]
        
    def LoadContent(self, stage):
        print("Level2")
        for column in range(self.groupHeight):
            for row in range(self.groupWidth):
                self.unitsInGrid.append(EnemyPool().GetObject(self.rowType[column], (GameWorld.instance.screen.get_width() / 2 - 380 + row * 80, 50 + 70 * column), stage))