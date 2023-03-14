from GameObject import GameObject

class ImageAsset(GameObject):
    def __init__(self, sprite, posX, posY, scale):
        super().__init__(sprite, posX, posY, False, scale)

    def LoadContent(self):
        return super().LoadContent()
    
    def Update(self, deltaTime, debugMode):
        return super().Update(deltaTime, False)
    
    def Draw(self, screen, debugMode):
        return super().Draw(screen, False)