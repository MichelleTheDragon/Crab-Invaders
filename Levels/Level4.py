from Levels.Level import Level
from GameWorld import GameWorld
from Objectpools.EnemyPool import EnemyPool
from Factories.EnemyFactory import ENEMYTYPE
import pygame

class Level4(Level):
    def __init__(self):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.bgMusic = "Sounds/CrabRaveMetal.mp3"
        self.bossMusic = pygame.mixer.Sound(self.bgMusic)
        self.bossMusic.set_volume(0.4)
        
    def LoadContent(self, stage):
        print("Level4: Boss")
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.BOSS1, (GameWorld.instance.screen.get_width() / 2, 50), stage))
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.TOUGH, (GameWorld.instance.screen.get_width() / 2 - 100, 50), stage))
        self.mySpecialUnits.append(EnemyPool().GetObject(ENEMYTYPE.TOUGH, (GameWorld.instance.screen.get_width() / 2 + 100, 50), stage))

    def StartLevel(self):
        pygame.mixer.Sound.play(self.bossMusic)