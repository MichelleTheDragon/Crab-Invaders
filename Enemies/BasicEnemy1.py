from GameObject import GameObject
from Components.Enemy import Enemy
from Components.SpriteRenderer import SpriteRenderer
from Components.Projectile import Projectile

class BasicEnemy1:
    def __init__(self, posX, posY, myLevel):
        self.gameObject = GameObject()
        self.gameObject.transform = (posX, posY)
        self.gameObject.AddComponent(SpriteRenderer("Sprites/enemy_01.png", 1))
        self.gameObject.AddComponent(Enemy(Projectile(self.gameObject, 30), myLevel))
        #super().__init__(posX, posY, True, 1)

    def LoadContent(self):
        self.gameObject.LoadContent()
    
    def Update(self):
        self.gameObject.Update()
    
    def Draw(self):
        self.gameObject.Draw()
    
    def move(self, sideMove, downMove):
        self.posX += sideMove
        self.posY += downMove