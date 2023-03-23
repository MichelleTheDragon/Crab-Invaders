from Factories.Factory import Factory
from enum import Enum
from GameObject import GameObject
from Components.Collider import Collider
from Components.SpriteRenderer import SpriteRenderer
from Components.Enemy import Enemy
from Components.Animator import Animator, Animation
import pygame

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
        self.baseSprite = pygame.image.load("Sprites/Crab_Base.png")
        
        self.idleAnimationSprites = []
        self.idleAnimationSprites.append(self.baseSprite)
        self.idleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle3.png"))
        self.idleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle2.png"))
        self.idleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle2.png"))
        self.idleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle3.png"))
        self.idleAnimationSprites.append(self.baseSprite)

        self.attackAnimationSprites = []
        self.attackAnimationSprites.append(self.baseSprite)
        self.attackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack2.png"))
        self.attackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack3.png"))
        self.attackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack4.png"))
        self.idleAnimation = []

    def Create(self, enemyType, position):
        gameObject = GameObject(position)
        gameObject.tag = "Enemy"
        gameObject.enemyTags.append("Player")
        gameObject.enemyTags.append("Barricade")
        match enemyType:
            case ENEMYTYPE.BASIC:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
            case ENEMYTYPE.ADVANCED:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
            case ENEMYTYPE.TOUGH:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
            case _:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
            
        spriteRenderer.offset = (0, -45)
        gameObject.AddComponent(spriteRenderer)
        animator = Animator(spriteRenderer)
        animator.AddAnimation(Animation("Idle", self.idleAnimationSprites, 4))
        animator.AddAnimation(Animation("Attack", self.attackAnimationSprites, 5))
        gameObject.AddComponent(animator)
        gameObject.AddComponent(Collider(gameObject, spriteRenderer, 1, (-50, -80)))
        gameObject.AddComponent(Enemy(enemyType))
        return gameObject
