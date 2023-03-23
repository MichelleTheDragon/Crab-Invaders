import pygame
from GameWorld import GameWorld
    
def main():
    pygame.init()

    myWorld = GameWorld()
    myWorld.LoadContent()
    myWorld.UpdateLoop()
        
    pygame.quit()

if __name__ == "__main__":
    main()