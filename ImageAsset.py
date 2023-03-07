from GameObject import GameObject

class ImageAsset(GameObject):
    def __init__(self, sprite, posX, posY):
        super().__init__(sprite, posX, posY, False)

    def LoadContent(self):
        return super().LoadContent()
    
    def Update(self, deltaTime):
        return super().Update(deltaTime, False)
    
    def Draw(self, screen):
        return super().Draw(screen, False)