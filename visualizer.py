import pygame

# proof of concept
def getInput():
    keypressed = pygame.event.get()

    return keypressed

if __name__ == "__main__":
    screen = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)

    while(True):
        a = getInput()
        if a:
            print(a)

