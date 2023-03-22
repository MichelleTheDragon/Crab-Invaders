from Factories.Factory import Factory
from enum import Enum
from GameObject import GameObject
from Components.Collider import Collider
from Components.SpriteRenderer import SpriteRenderer
from Components.Enemy import Enemy

class ENEMYTYPE(Enum):
    BASIC = 1
    ADVANCED = 2
    TOUGH = 3
    
class EnemyFactory(Factory):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(EnemyFactory, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.spriteList = []
        self.spriteList.append("Sprites/enemy_01.png")

    def Create(self, enemyType):
        gameObject = GameObject((-500, -500))
        gameObject.tag = "Enemy"
        gameObject.enemyTags.append("Player")
        gameObject.enemyTags.append("Barricade")
        match enemyType:
            case ENEMYTYPE.BASIC:
                spriteRenderer = SpriteRenderer(self.spriteList[0], 0.8)
        gameObject.AddComponent(spriteRenderer)
        gameObject.AddComponent(Collider(gameObject, spriteRenderer, 3, (0, 0)))
        gameObject.AddComponent(Enemy())
        return gameObject