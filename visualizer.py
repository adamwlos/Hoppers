import pygame

WINDOW = (500,500)
BLACK = (0,0,0)
GREY = (100,100,100)
WHITE = (255,255,255)
DIMENSION = 8# Dimension of game board
SIZE = 50 # Dimension of a grid tile

# proof of concept
def getInput():
    keypressed = pygame.event.get()
    return keypressed

"""
Create a DIMENSION*DIMENSION grid with alternating white and grey tiles, with
tiles of dimension SIZE*SIZE
By Ronald, on 10/27/2019
"""
def create_initial_grid(self):
    background = pygame.Surface(WINDOW)
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            rect = pygame.Rect(column*SIZE,row*SIZE,SIZE,SIZE)
            """alternate white and grey tiles every column,
            switch order every row"""
            if(((column%2)+(row%2))%2 == 0):
                pygame.draw.rect(background, WHITE, rect)
            else:
                pygame.draw.rect(background, GREY, rect)
    screen.blit(background, (0,0))
    pygame.display.update()
    return

if __name__ == "__main__":
    pygame.init()
    is_running = True
    
    screen = pygame.display.set_mode(WINDOW, pygame.HWSURFACE | pygame.DOUBLEBUF)
    create_initial_grid()
    while(is_running):
        
        a = getInput()
        if a:
            print(a)
        for event in a:
            if event.type == pygame.QUIT:
                pygame.quit()
                is_running = False
