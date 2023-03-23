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
        
        self.baseIdleAnimationSprites = []
        self.baseIdleAnimationSprites.append(self.baseSprite)
        self.baseIdleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle3.png"))
        self.baseIdleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle2.png"))
        self.baseIdleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle2.png"))
        self.baseIdleAnimationSprites.append(pygame.image.load("Sprites/Crab_Idle3.png"))
        self.baseIdleAnimationSprites.append(self.baseSprite)

        self.baseAttackAnimationSprites = []
        self.baseAttackAnimationSprites.append(self.baseSprite)
        self.baseAttackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack2.png"))
        self.baseAttackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack3.png"))
        self.baseAttackAnimationSprites.append(pygame.image.load("Sprites/Crab_Attack4.png"))

        self.toughSprite = pygame.image.load("Sprites/CrabTough_Base.png")
        
        self.toughIdleAnimationSprites = []
        self.toughIdleAnimationSprites.append(self.toughSprite)
        self.toughIdleAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Idle3.png"))
        self.toughIdleAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Idle2.png"))
        self.toughIdleAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Idle2.png"))
        self.toughIdleAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Idle3.png"))
        self.toughIdleAnimationSprites.append(self.toughSprite)

        self.toughAttackAnimationSprites = []
        self.toughAttackAnimationSprites.append(self.toughSprite)
        self.toughAttackAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Attack2.png"))
        self.toughAttackAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Attack3.png"))
        self.toughAttackAnimationSprites.append(pygame.image.load("Sprites/CrabTough_Attack4.png"))

    def Create(self, enemyType, position, stage):
        gameObject = GameObject(position)
        gameObject.tag = "Enemy"
        gameObject.enemyTags.append("Player")
        gameObject.enemyTags.append("Barricade")
        spriteRenderer = self.SetSpecial(gameObject, enemyType)
        gameObject.AddComponent(Collider(gameObject, spriteRenderer, 3, (-60, -80)))
        gameObject.AddComponent(Enemy(enemyType, stage))
        return gameObject

    def SetSpecial(self, gameObject, enemyType):
        match enemyType:
            case ENEMYTYPE.BASIC:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
                spriteRenderer.offset = (0, -45)
                gameObject.AddComponent(spriteRenderer)
                animator = Animator(spriteRenderer)
                animator.AddAnimation(Animation("Idle", self.baseIdleAnimationSprites, 4))
                animator.AddAnimation(Animation("Attack", self.baseAttackAnimationSprites, 5))
                gameObject.AddComponent(animator)
            case ENEMYTYPE.ADVANCED:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
                spriteRenderer.offset = (0, -45)
                gameObject.AddComponent(spriteRenderer)
                animator = Animator(spriteRenderer)
                animator.AddAnimation(Animation("Idle", self.baseIdleAnimationSprites, 4))
                animator.AddAnimation(Animation("Attack", self.baseAttackAnimationSprites, 5))
                gameObject.AddComponent(animator)
            case ENEMYTYPE.TOUGH:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
                spriteRenderer.offset = (0, -45)
                gameObject.AddComponent(spriteRenderer)
                animator = Animator(spriteRenderer)
                animator.AddAnimation(Animation("Idle", self.toughIdleAnimationSprites, 4))
                animator.AddAnimation(Animation("Attack", self.toughAttackAnimationSprites, 5))
                gameObject.AddComponent(animator)
            case _:
                spriteRenderer = SpriteRenderer(self.baseSprite, 1)
                spriteRenderer.offset = (0, -45)
                gameObject.AddComponent(spriteRenderer)
                animator = Animator(spriteRenderer)
                animator.AddAnimation(Animation("Idle", self.baseIdleAnimationSprites, 4))
                animator.AddAnimation(Animation("Attack", self.baseAttackAnimationSprites, 5))
                gameObject.AddComponent(animator)
        return spriteRenderer