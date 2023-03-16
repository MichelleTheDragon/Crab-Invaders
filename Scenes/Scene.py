from abc import ABC, abstractmethod
import pygame

class Scene(ABC):
    @abstractmethod
    def __init__(self, myWorld):
        self.myGameObjects = []
        self.myWorld = myWorld
        self.bgMusic = ""
        

    @abstractmethod
    def LoadContent(self):
        if(len(self.bgMusic) > 0):
            pygame.mixer.music.load(self.bgMusic)
            pygame.mixer.music.play(-1)

    @abstractmethod
    def Update(self, deltaTime, debugMode):
        for myGameObject in self.myGameObjects:
            myGameObject.Update(deltaTime, debugMode)

    @abstractmethod
    def Draw(self, screen, debugMode):
        for myGameObject in self.myGameObjects:
            myGameObject.Draw(screen, debugMode)