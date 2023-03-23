from Components.Component import Component
from GameWorld import GameWorld

class Animator(Component):
    def __init__(self, spriteRenderer):
        self.currentIndex = 0
        self.timeElapsed = 0.0
        self.spriteRenderer = spriteRenderer
        self.animations = dict()
        self.currentAnimation = None

    def Update(self):
        self.timeElapsed += GameWorld.instance.deltaTime
        if self.currentAnimation != None:
            self.currentIndex = int(self.timeElapsed * self.currentAnimation.fps)
            if self.currentIndex > len(self.currentAnimation.sprites) - 1:
                self.timeElapsed = 0
                self.currentIndex = 0
            self.spriteRenderer.ChangeSprite(self.currentAnimation.sprites[self.currentIndex])

    def AddAnimation(self, animation):
        self.animations[animation.name] = animation
        if self.currentAnimation == None:
            self.currentAnimation = animation

    def PlayAnimation(self, animationName):
        if self.currentAnimation != None:
            if animationName != self.currentAnimation.name:
                self.currentAnimation = self.animations[animationName]
                self.timeElapsed = 0
                self.currentIndex = 0

class Animation:
    def __init__(self, name, sprites, fps):
        self.name = name
        self.sprites = sprites
        self.fps = fps