from GeneralSubs import TextObjects
from pygame.locals import *
import pygame

class Ghost:
        
    def __init__(self, GivenLocation, SetImage):
        self.Location = GivenLocation
        self.Image = SetImage

class PAC:
    
    def __init__(self, GivenLocation):
        self.Location = GivenLocation
        
    #def ChangeProperty(self,Modifier as property, Value):
        #self.Modifier = Value

class Pill:
    pass

class Button:
    def __init__(self, _msg, _msgcolour, _x, _y, _width, _height, _inactivecolour, _activecolour, _display, _action=None):
        self.Action = _action
        self.Display = _display
        self.LocationInfo = [_x, _y, _width, _height]
        self.Colour = [_inactivecolour, _activecolour]
        self.MsgInfo = [_msg, _msgcolour]
        smallText = pygame.font.SysFont("freesansbold.ttf",20)
        textSurf, textRect = TextObjects(self.MsgInfo[0], smallText, self.MsgInfo[1])
        textRect.center = ((_x+(_width/2)), (_y+(_height/2)))
        self.TextSurf = textSurf
        self.TextRect = textRect
        _display.blit(textSurf, textRect)

    def Check(self):

        ToGive = None
        mouse = pygame.mouse.get_pos()
        ev = pygame.event.get()

        if self.LocationInfo[0] + self.LocationInfo[2] > mouse[0] > self.LocationInfo[0] and self.LocationInfo[1] + self.LocationInfo[3] > mouse[1] > self.LocationInfo[1]:
            pygame.draw.rect(self.Display, self.Colour[1], self.LocationInfo)

            for event in ev:
                if  event.type == pygame.MOUSEBUTTONUP and self.Action != None:
                    ToGive = self.Action

        else:
            pygame.draw.rect(self.Display, self.Colour[0], self.LocationInfo)
                        
        self.Display.blit(self.TextSurf, self.TextRect)
        return ToGive
        

