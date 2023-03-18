from abc import ABC, abstractmethod

class Level(ABC):
    @abstractmethod
    def __init__(self, myWorld):
        self.mySpecialUnits = []
        self.unitsInGrid = []
        self.myWorld = myWorld
        self.bgMusic = ""
        

    @abstractmethod
    def LoadContent(self):
        pass

    def SpawnRow(self, height, unit):
        pass
