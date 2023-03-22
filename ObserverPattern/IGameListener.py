from abc import ABC, abstractmethod

class IGameListener(ABC):
    @abstractmethod
    def Notify(gameEvent):
        pass