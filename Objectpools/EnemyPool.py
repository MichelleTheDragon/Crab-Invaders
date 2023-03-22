from Objectpools.Objectpool import Objectpool
from Factories.EnemyFactory import EnemyFactory

class EnemyPool(Objectpool):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(EnemyPool, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()

    def GetObject(self, enemyType):
        if len(self.inactiveGameObjects) == 0:
            return self.CreateObject(enemyType)
        self.newGameObject = self.inactiveGameObjects.pop()
        self.activeGameObjects.append(self.newGameObject)
        return self.newGameObject
    
    def CleanUp(gameObject):
        pass
    
    def CreateObject(self, enemyType):
        return EnemyFactory().Create(enemyType)