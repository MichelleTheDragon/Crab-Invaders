from Components.Component import Component


class Enemy(Component):
    def __init__(self):#, projectile, myLevel):
        super().__init__()
        self.point_value = 1
        #self.projectile = projectile
        #self.myLevel = myLevel
        
    def Shoot(self, straightShot):
        if straightShot == True:
            pass
        else:
            self.myLevel.myAttacks.append()#Ask projectile factory for unused projectile or create new
