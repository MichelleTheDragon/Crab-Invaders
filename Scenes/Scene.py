from abc import ABC, abstractmethod
import pygame
from GameWorld import GameWorld

class Scene(ABC):
    @abstractmethod
    def __init__(self):
        self.myGameObjects = []
        self.bgMusic = ""
        self.isEnabled = False
        self.musicVolume = 1

    @abstractmethod
    def LoadContent(self):
        pass

    def Start(self):
        self.isEnabled = True
        if(len(self.bgMusic) > 0):
            pygame.mixer.music.load(self.bgMusic)
            pygame.mixer.music.set_volume(self.musicVolume * GameWorld.instance.music_volume)
            pygame.mixer.music.play(-1)

    def Stop(self):
        self.isEnabled = False
        pygame.mixer.music.stop()

    @abstractmethod
    def Update(self):
        if self.isEnabled == True:
            for myGameObject in self.myGameObjects:
                myGameObject.Update()

    @abstractmethod
    def Draw(self):
        if self.isEnabled == True:
            for myGameObject in self.myGameObjects:
                myGameObject.Draw()

    def ChangeMusic(self):
        if(len(self.bgMusic) > 0):
            pygame.mixer.music.load(self.bgMusic)
            pygame.mixer.music.play(-1)