from Components.Component import Component
import Scenes.Stage
from GameWorld import GameWorld

class Projectile(Component):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.isAlive = False

    def SetType(self, myType, direction):
        self.direction = direction
        self.isAlive = True
        
        from Factories.ProjectileFactory import PROJECTILETYPE
        match myType:
            case PROJECTILETYPE.SLOW:
                self.speed = 20
            case PROJECTILETYPE.MEDIUM:
                self.speed = 30
            case PROJECTILETYPE.FAST:
                self.speed = 40
            case PROJECTILETYPE.STONE:
                self.speed = 60
            case _:
                self.speed = 20
        
    def Update(self):
        self.move()

    def move(self):
        if self.speed > 0:
            self.gameObject.transform.Translate(self.direction, self.speed)
            if self.gameObject.transform.posY < -100 or self.gameObject.transform.posY > GameWorld.instance.screen.get_height() + 100:
                Scenes.Stage.Stage.instance.myGameObjects.remove(self.gameObject)