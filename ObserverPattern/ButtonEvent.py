from enum import Enum
from ObserverPattern.GameEvent import GameEvent

class BUTTONSTATE(Enum):
    UP = 1
    DOWN = 2

class ButtonEvent(GameEvent):
    def __init__(self):
        self._Key = None
        self._State = None

    def Notify(self, key, state):
        self._Key = key
        self._State = state
        super().Notify()