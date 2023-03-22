from abc import ABC, abstractmethod
from GameWorld import GameWorld

class Objectpool(ABC):
    def __init__(self):
        self.activeGameObjects = []
        self.inactiveGameObjects = []

    @abstractmethod
    def GetObject(self):
        if len(self.inactiveGameObjects) == 0:
            return self.CreateObject()
        self.newGameObject = self.inactiveGameObjects.pop()
        self.activeGameObjects.append(self.newGameObject)
        return self.newGameObject
    
    def ReleaseObject(self, gameObject):
        self.activeGameObjects.remove(gameObject)
        self.inactiveGameObjects.append(gameObject)
        GameWorld.instance.Destroy(gameObject)
        self.CleanUp(gameObject)

    @abstractmethod
    def CreateObject():
        pass

    @abstractmethod
    def CleanUp(gameObject):
        pass