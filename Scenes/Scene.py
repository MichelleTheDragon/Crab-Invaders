from abc import ABC, abstractmethod

class Scene(ABC):
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def LoadContent(self):
        pass

    @abstractmethod
    def Update(self):
        pass

    @abstractmethod
    def Draw(self):
        pass