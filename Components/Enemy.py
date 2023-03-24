from Components.Component import Component
from GameWorld import GameWorld
from random import randint, randrange
from Components.Animator import Animator
from Objectpools.ProjectilePool import ProjectilePool
from Factories.ProjectileFactory import PROJECTILETYPE

class Enemy(Component):
    def __init__(self, enemyType, stage):
        super().__init__()
        self.point_value = 1
        self.SetType(enemyType, stage)
        self.cooldown = False
        self.isAlive = False
        self.checkFreq = 0.25

    def SetType(self, enemyType, stage):
        self.timeElapsed = 0.0
        self.stage = stage
        self.isAlive = True
        
        from Factories.EnemyFactory import ENEMYTYPE
        match enemyType:
            case ENEMYTYPE.BASIC:
                self.health = 1
                self.attackfrequency = 1
                self.point_value = 1
                self.cooldown = 2.0
                self.projectileType = PROJECTILETYPE.SLOW
            case ENEMYTYPE.ADVANCED:
                self.health = 1
                self.attackfrequency = 3
                self.point_value = 2    
                self.cooldown = 2.0
                self.projectileType = PROJECTILETYPE.MEDIUM
            case ENEMYTYPE.TOUGH:
                self.health = 2
                self.attackfrequency = 2
                self.point_value = 3
                self.cooldown = 2.0
                self.projectileType = PROJECTILETYPE.FAST
            case ENEMYTYPE.BOSS1:
                self.health = 30
                self.attackfrequency = 100
                self.point_value = 200
                self.cooldown = 0.5
                self.projectileType = PROJECTILETYPE.FAST
            case ENEMYTYPE.BOSS2:
                self.health = 40
                self.attackfrequency = 150
                self.point_value = 300
                self.cooldown = 0.3
                self.projectileType = PROJECTILETYPE.FAST
            case _:
                self.health = 1
                self.attackfrequency = 1
                self.point_value = 1
                self.projectileType = PROJECTILETYPE.SLOW

    def Update(self):
        self.timeElapsed += GameWorld.instance.deltaTime
        if self.cooldown == True:
            if self.timeElapsed > self.cooldown:
                self.cooldown = False
                self.timeElapsed = 0.0
                self.checkFreq = 0.15 + float(randrange(5)/ 10)
        elif self.timeElapsed > self.checkFreq:
            if randint(0, 10000 + 30 * self.attackfrequency) >=  10000:
                if self.gameObject.HasComponent(Animator):
                    self.gameObject.GetComponent(Animator).PlayAnimation("Attack", True)
                self.Shoot(True)
                self.cooldown = True
            self.timeElapsed = 0.0

    def CheckAlive(self):
        self.health -= 1
        return self.health


    def Shoot(self, straightShot):
        if straightShot == True:
            self.stage.myGameObjects.append(ProjectilePool().GetObject(self.projectileType, (self.gameObject.transform.posX, self.gameObject.transform.posY + 20), "Enemy", (0, 3)))
        else:
            self.myLevel.myAttacks.append()#Ask projectile factory for unused projectile or create new
