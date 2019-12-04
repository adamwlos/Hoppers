import pygame


class MainMenu:
    """ THe MainMenu class generates a menu before the user can play the game. 
        This menu contains buttons that allow the user to select the game mode
        they want to play on. They can either choose to play versus a human
        or computer player.
    """

    WINDOW = (500,500)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    GREY = (200,200,200)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW, pygame.HWSURFACE |
                                              pygame.DOUBLEBUF)
        self.screen.fill(self.WHITE)
        title_font = pygame.font.SysFont("arial.ttf", 115)
        text = title_font.render("Hoppers", 1, self.BLACK)
        text_position = text.get_rect(centerx=self.WINDOW[0]//2, 
                                                    centery=self.WINDOW[1]//5)
        self.screen.blit(text, text_position)
        self.create_buttons()
        pygame.display.update()
    
    def get_input(self):
        """ Returns the event object of an action. We are looking for mouse
            clicks in the menu.
        """
        keypressed = pygame.event.get()
        return keypressed

    def get_mouse_position(self, event):
        """ Takes in an event object and returns the coordinates of the event. 
            The menu requires the coordinates of the mouse click to check if
            the user clicked a button.
        """
        return (event.dict['pos'][0], event.dict['pos'][1])
#
    def quit(self):
        """ Closes the screen when it is no longer needed.
        """
        pygame.quit()

    def create_buttons(self):
        """ Gives the user the option to select either the mode to player 
            versus another human or versus the computer.
        """
        # Human VS Human
        # Human VS Computer
        rect = pygame.Rect(self.WINDOW[0]//4, 200, 250, 50)
        pygame.draw.rect(self.screen, self.GREY, rect)
        rect = pygame.Rect(self.WINDOW[0]//4, 300, 250, 50)
        pygame.draw.rect(self.screen, self.GREY, rect)
        self.screen.blit(self.screen, (0,0))

        title_font = pygame.font.SysFont("arial.ttf", 30)
        text = title_font.render("Human VS Human", 1, self.BLACK)
        text_position = text.get_rect(centerx=self.WINDOW[0]//2, 
                                                centery=225)
        self.screen.blit(text, text_position)

        text = title_font.render("Human VS Computer", 1, self.BLACK)
        text_position = text.get_rect(centerx=self.WINDOW[0]//2, 
                                                centery=325)
        self.screen.blit(text, text_position)

    def get_game_mode(self, event):
        """ Based on where the user clicked on the screen, this method will
            figure out which button the user selected. From then it will return
            the game mode listed on the button.
        """
        mode = ""
        # Check for human vs human
        location = self.get_mouse_position(event)
        if (location[0] > self.WINDOW[0]//4 and location [0] < self.WINDOW[0]-
                self.WINDOW[0]//4 and location[1] > 200 and location[1] < 250):
            mode = "HumanVSHuman"
        # Check for human vs computer
        elif (location[0] > self.WINDOW[0]//4 and location [0] < self.WINDOW[0]
            -self.WINDOW[0]//4 and location[1] > 300 and location[1] < 350):
            mode = "HumanVSComputer"
        return mode
