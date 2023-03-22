from ObserverPattern.GameEvent import GameEvent

class CollisionEvent(GameEvent):
    def __init__(self):
        self.other = None

    def Notify(self, other):
        self.other = other
        super().Notify()