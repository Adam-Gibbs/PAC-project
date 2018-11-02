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
    def __init__(msg, Msgcolour, x, y, width, height, Inactivecolour, Activecolour, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+width > mouse[0] > x and y+height > mouse[1] > y:
            pygame.draw.rect(StartDisplay, Activecolour, (x,y,width,height))

            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(StartDisplay, Inactivecolour,(x,y,width,height))

        smallText = pygame.font.SysFont("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText, Msgcolour)
        textRect.center = ( (x+(width/2)), (y+(height/2)) )
        StartDisplay.blit(textSurf, textRect)
    