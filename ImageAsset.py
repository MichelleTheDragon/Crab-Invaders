from GameObject import GameObject
from Components.SpriteRenderer import SpriteRenderer

class ImageAsset:
    def __init__(self, sprite, position, scale):
        self.gameObject = GameObject(position)
        self.gameObject.AddComponent(SpriteRenderer(self.gameObject, sprite, scale))
        #super().__init__(sprite, posX, posY, False, scale)

    def LoadContent(self):
        self.gameObject.LoadContent()
    
    def Update(self):
        self.gameObject.Update()
    
    def Draw(self):
        self.gameObject.Draw()