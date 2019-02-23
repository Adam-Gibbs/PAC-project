import pygame


# This creates and returns a text object
def TextObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


class Button:
    # Run when a new button is created, needs the size and message
    def __init__(self, _msg, _msgcolour, _x, _y, _width, _height,
                 _inactivecolour, _activecolour, _display, _action=None):
        self.Action = _action
        self.Display = _display

        self.LocationInfo = [_x, _y, _width, _height]
        self.Colour = [_inactivecolour, _activecolour]
        self.MsgInfo = [_msg, _msgcolour]

        # Loads in the text of the button
        smallText = pygame.font.SysFont("freesansbold.ttf", 20)
        textSurf, textRect = TextObjects(self.MsgInfo[0], smallText,
                                         self.MsgInfo[1])
        textRect.center = ((_x+(_width/2)), (_y+(_height/2)))

        self.TextSurf = textSurf
        self.TextRect = textRect
        _display.blit(textSurf, textRect)

        self.Clicked = False

    # This checks the button for user input
    def Check(self):

        ToGive = None
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # This highlights the button when hovered over
        if self.LocationInfo[0] + self.LocationInfo[2] > mouse[0] > self.LocationInfo[0] and self.LocationInfo[1] + self.LocationInfo[3] > mouse[1] > self.LocationInfo[1]:
            pygame.draw.rect(self.Display, self.Colour[1], self.LocationInfo)

            # This activates the button if it has not been clicked
            if click[0] == 1 and self.Action is not None and not self.Clicked:
                ToGive = self.Action
                self.Clicked = True

            # This checks for repeated clicks
            elif self.Clicked is True:
                if click[0] != 1:
                    self.Clicked = False

        # This redraws the standard button
        else:
            pygame.draw.rect(self.Display, self.Colour[0], self.LocationInfo)

        # This redraws the text and returns an action if any
        self.Display.blit(self.TextSurf, self.TextRect)
        return ToGive
