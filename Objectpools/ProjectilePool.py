from Objectpools.Objectpool import Objectpool
from Factories.ProjectileFactory import ProjectileFactory
from Components.Projectile import Projectile
import pygame
from random import randint

class ProjectilePool(Objectpool):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(ProjectilePool, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()
        self.whooshSounds = []
        self.whooshSounds.append(pygame.mixer.Sound("Sounds/Whoosh1.mp3"))
        self.whooshSounds.append(pygame.mixer.Sound("Sounds/Whoosh2.mp3"))
        for whoosh in self.whooshSounds:
            whoosh.set_volume(0.1)

    def GetObject(self, projectileType, position, faction, direction):
        test = randint(0, 1)
        try:
            pygame.mixer.Sound.play(self.whooshSounds[test])
        finally:
            pass
        if len(self.inactiveGameObjects) == 0:
            return self.CreateObject(projectileType, position, faction, direction)
        newGameObject = self.inactiveGameObjects.pop()
        newGameObject.transform.posX = position[0]
        newGameObject.transform.posY = position[1]
        newGameObject.GetComponent(Projectile).SetType(projectileType, direction)
        newGameObject.enemyTags = []
        if faction == "Player":
            newGameObject.enemyTags.append("Enemy")
        else:
            newGameObject.enemyTags.append("Player")
            newGameObject.enemyTags.append("Barricade")
        self.activeGameObjects.append(newGameObject)
        return newGameObject
    
    def CleanUp(gameObject):
        pass
    
    def CreateObject(self, projectileType, position, faction, direction):
        return ProjectileFactory().Create(projectileType, position, faction, direction)