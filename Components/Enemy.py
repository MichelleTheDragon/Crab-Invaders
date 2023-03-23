from Components.Component import Component
from GameWorld import GameWorld
from random import randrange
from Components.Animator import Animator
from Objectpools.ProjectilePool import ProjectilePool
from Factories.ProjectileFactory import PROJECTILETYPE

class Enemy(Component):
    def __init__(self, enemyType, stage):
        super().__init__()
        self.SetType(enemyType, stage)
        self.cooldown = False
        self.isAlive = False

    def SetType(self, enemyType, stage):
        self.point_value = 1
        self.timeElapsed = 0.0
        self.stage = stage
        self.isAlive = True
        
        from Factories.EnemyFactory import ENEMYTYPE
        match enemyType:
            case ENEMYTYPE.BASIC:
                self.health = 1
                self.attackfrequency = 1
                self.projectileType = PROJECTILETYPE.SLOW
            case ENEMYTYPE.ADVANCED:
                self.health = 1
                self.attackfrequency = 3
                self.projectileType = PROJECTILETYPE.MEDIUM
            case ENEMYTYPE.TOUGH:
                self.health = 2
                self.attackfrequency = 2
                self.projectileType = PROJECTILETYPE.FAST
            case _:
                self.health = 1
                self.attackfrequency = 1
                self.projectileType = PROJECTILETYPE.SLOW

    def Update(self):
        self.timeElapsed += GameWorld.instance.deltaTime
        if self.cooldown == True:
            if self.timeElapsed > 2:
                self.cooldown = False
                self.timeElapsed = 0.0
        elif self.timeElapsed > 0.25:
            if randrange(1001 + 1 * self.attackfrequency) >=  1000:
                self.gameObject.GetComponent(Animator).PlayAnimation("Attack", True)
                self.Shoot(True)
                self.cooldown = True
            self.timeElapsed = 0.0

    def Shoot(self, straightShot):
        if straightShot == True:
            self.stage.myGameObjects.append(ProjectilePool().GetObject(self.projectileType, (self.gameObject.transform.posX, self.gameObject.transform.posY + 20), "Enemy", (0, 3)))
        else:
            self.myLevel.myAttacks.append()#Ask projectile factory for unused projectile or create new
