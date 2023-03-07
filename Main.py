import pygame
from GameWorld import GameWorld
    
def main():
    pygame.init()

    running = True
    myWorld = GameWorld()
    myWorld.LoadContent()

    while running:
        if(myWorld.Update() == False):
            break
        
        pygame.display.update()    
        myWorld.Draw()
    pygame.quit()

if __name__ == "__main__":
    main()