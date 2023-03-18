from Levels.Level import Level
from Enemies.BasicEnemy1 import BasicEnemy1
import GameWorld

class Level1(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = ""
        
    def LoadContent(self):
        self.unitsInGrid.append(BasicEnemy1(GameWorld().infoObject.current_w / 2, 150, 0.5, self))
        for row in self.unitsInGrid:
            self.SpawnRow(row)