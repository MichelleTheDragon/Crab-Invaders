import pygame
import copy
from Components.Transform import Transform


class GameObject:
    def __init__(self, position):
        self.transform = Transform(position)
        self.components = []
        self.tag = ""
        self.isAlive = True
        self.enemyTags = []

    #Load all components
    def LoadContent(self):
        for component in self.components:
            component.LoadContent()

    #Update all Components
    def Update(self):
        if self.isAlive == True:
            for component in self.components:
                component.Update()

    #Draw all Components
    def Draw(self):
        if self.isAlive == True:
            for component in self.components:
                component.Draw() 

    #Add a component to this gameObject
    def AddComponent(self, component):
        component.gameObject = self
        self.components.append(component)
        return component
    
    #Get a specific component from this gameObject 
    def GetComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return component
            
    #Check if this gameObject contains a component of a certain type
    def HasComponent(self, myType):
        for component in self.components:
            if type(component) is myType:
                return True
        return False
    
    #Make a Clone of this gameObject, including all components
    def Clone(self):
        gameObject = GameObject()
        for component in self.components:
            gameObject.AddComponent(component.Clone())
        return gameObject