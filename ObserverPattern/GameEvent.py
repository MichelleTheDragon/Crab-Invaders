from ObserverPattern.IGameListener import IGameListener
from abc import ABC, abstractmethod

class GameEvent(IGameListener, ABC):
    def __init__(self):
        self.listeners = []

    def Attach(self, listener):
        self.listeners.append(listener)

    def Detach(self, listener):
        self.listeners.remove(listener)

    @abstractmethod
    def Notify(self):
        for listener in self.listeners:
            listener.Notify(self)