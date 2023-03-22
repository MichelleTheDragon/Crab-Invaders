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
        self.spriteList.append("Sprites/enemy_02.png")
        self.spriteList.append("Sprites/enemy_03.png")

    def Create(self, enemyType, position):
        gameObject = GameObject(position)
        gameObject.tag = "Enemy"
        gameObject.enemyTags.append("Player")
        gameObject.enemyTags.append("Barricade")
        match enemyType:
            case ENEMYTYPE.BASIC:
                spriteRenderer = SpriteRenderer(self.spriteList[0], 0.5)
            case ENEMYTYPE.ADVANCED:
                spriteRenderer = SpriteRenderer(self.spriteList[1], 0.5)
            case ENEMYTYPE.TOUGH:
                spriteRenderer = SpriteRenderer(self.spriteList[2], 0.5)
        gameObject.AddComponent(spriteRenderer)
        gameObject.AddComponent(Collider(gameObject, spriteRenderer, 3, (0, 0)))
        gameObject.AddComponent(Enemy(enemyType))
        return gameObject