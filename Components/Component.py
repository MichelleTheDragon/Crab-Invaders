from abc import ABC, abstractmethod
import inspect
import copy

class Component(ABC):
    def __init__(self):
        self.gameObject = None
        self.isEnabled = True

    def Start(self):
        pass

    def Update(self):
        pass

    def Draw(self):
        pass

    def Clone(self):
        return copy.copy(self)