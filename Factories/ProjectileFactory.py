from Factories.Factory import Factory
from enum import Enum
from GameObject import GameObject
from Components.Collider import Collider
from Components.SpriteRenderer import SpriteRenderer
from Components.Projectile import Projectile
from Components.Animator import Animator, Animation
import pygame

class PROJECTILETYPE(Enum):
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    STONE = 4
    
class ProjectileFactory(Factory):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(ProjectileFactory, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.LightShellSprite = pygame.image.load("Sprites/ShellLight.png")
        self.BlueShellSprite = pygame.image.load("Sprites/ShellBlue.png")
        self.CircleShellSprite = pygame.image.load("Sprites/ShellCircle.png")
        self.SpiralShellSprite = pygame.image.load("Sprites/ShellSpiral.png")
        self.Stone = pygame.image.load("Sprites/Stone.png")
        self.scale = 0.0

    def Create(self, projectileType, position, faction, direction):
        gameObject = GameObject(position)
        gameObject.tag = "Projectile"
        if faction == "Player":
            gameObject.enemyTags.append("Enemy")
        else:
            gameObject.enemyTags.append("Player")
            gameObject.enemyTags.append("Barricade")
        match projectileType:
            case PROJECTILETYPE.SLOW:
                self.scale = .1
                spriteRenderer = SpriteRenderer(self.LightShellSprite, self.scale)
                colliderResize = (5 * (1 - self.scale),0)
            case PROJECTILETYPE.MEDIUM:
                self.scale = .1
                spriteRenderer = SpriteRenderer(self.SpiralShellSprite, self.scale)
                colliderResize = (-20 * (1 - self.scale),0)
            case PROJECTILETYPE.FAST:
                self.scale = .15
                spriteRenderer = SpriteRenderer(self.BlueShellSprite, self.scale)
                colliderResize = (0,0)
            case PROJECTILETYPE.STONE:
                self.scale = .15
                spriteRenderer = SpriteRenderer(self.Stone, self.scale)
                colliderResize = (0,0)
            case _:
                self.scale = .1
                spriteRenderer = SpriteRenderer(self.LightShellSprite, self.scale)
                colliderResize = (5 * (1 - self.scale),0)
            
        gameObject.AddComponent(spriteRenderer)
        gameObject.AddComponent(Collider(gameObject, spriteRenderer, 3, colliderResize))
        newProjectile = Projectile()
        newProjectile.SetType(projectileType, direction)
        gameObject.AddComponent(newProjectile)
        return gameObject
