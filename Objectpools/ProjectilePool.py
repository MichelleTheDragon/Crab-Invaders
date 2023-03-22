from Objectpools.Objectpool import Objectpool

class ProjectilePool(Objectpool):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(ProjectilePool, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()

    def CleanUp(gameObject):
        pass
    
    def CreateObject():
        pass #ProjectileFactory.instance.Create()