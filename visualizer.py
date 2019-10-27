import pygame

# proof of concept
def getInput():
    keypressed = pygame.event.get()

    return keypressed

if __name__ == "__main__":
    pygame.init()
    running = True
    screen = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)

    while(running):
        a = getInput()
        if a:
            print(a)
        for event in a:
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

