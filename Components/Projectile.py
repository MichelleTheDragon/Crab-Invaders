from Components.Component import Component

class Projectile(Component):
    def __init__(self, gameObject, speed):
        self.gameObject = gameObject
        self.speed = speed

    def Update(self):
        self.move()

    def move(self):
        self.gameObject.transform.Translate(self.speed)