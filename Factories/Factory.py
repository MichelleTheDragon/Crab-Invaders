from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def Create(self, enemyType):
        pass