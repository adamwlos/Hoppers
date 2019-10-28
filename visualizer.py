import pygame

WINDOW = (500,500)
BLACK = (0,0,0)
GREY = (100,100,100)
WHITE = (255,255,255)
DIMENSION = 8# Dimension of game board
SIZE = 50 # dimension of a grid tile

class Visualizer:

    screen: pygame.Surface
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW, pygame.HWSURFACE | pygame.DOUBLEBUF)
        
    def getInput(self):
        keypressed = pygame.event.get()
        return keypressed

    """
    Create a DIMENSION*DIMENSION grid onto the screen with alternating
    white and grey tiles, with tiles of dimension SIZE*SIZE
    By Ronald, on 10/27/2019
    """
    def create_initial_grid(self) -> None:
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
        self.screen.blit(background, (0,0))
        pygame.display.update()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    
    visualizer = Visualizer()
    visualizer.create_initial_grid()
    
    is_running = True
    while(is_running):
        events = visualizer.getInput()
        if events:
            print(events)
        for event in events:
            if event.type == pygame.QUIT:
                visualizer.quit()
                is_running = False
