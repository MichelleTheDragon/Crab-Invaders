import pygame
import copy
from Components.Transform import Transform


class GameObject:
    def __init__(self, position):
        self.transform = Transform(position)
        self.components = []
        self.tag = ""
        self.enemyTags = []

    def LoadContent(self):
        for component in self.components:
            component.LoadContent()

    def Update(self):
        for component in self.components:
            component.Update()

    def Draw(self):
        for component in self.components:
            component.Draw() 

    def AddComponent(self, component):
        component.gameObject = self
        self.components.append(component)
        return component
    
    def GetComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return component
            
    def HasComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return True
        return False
    
    def Clone(self):
        gameObject = GameObject()
        for component in self.components:
            gameObject.AddComponent(component.Clone())
        return gameObject