import pygame, sys
from pygame.locals import *
from MapStruct import *
from LoadMap import *

MapSize = [1680, 1050]
pygame.init()
CurrMap = LoadMap("Maps\Test.txt", MapSize)
clock = pygame.time.Clock()
ExitBool = False

StartDisplay = pygame.display.set_mode(MapSize, pygame.FULLSCREEN)
White=(255,255,255)
Blue=(0, 0, 255)
DarkBlue=(50,50,200)
Green=(0,255,0)
DarkGreen=(50,200,50)
Red=(255,0,0)
DarkRed=(200,50,50)
Yellow=(255,255,0)
Black=(0,0,0)
intro = True

def LoadDisplay():
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
            for wall in range (0,4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue, (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 10)

def EscapeMenu():

    intro = True
    while intro:
        print(intro)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        StartDisplay.fill(Black)
        largeText = pygame.font.SysFont("freesansbold.ttf",115)

        button("Small",White,450,450,100,50,Black,DarkBlue,Smaller)
        button("Big",White,650,450,100,50,Black,DarkBlue,Smaller)
        button("Quit",White,550,450,100,50,Black,DarkBlue,Quit)

        pygame.display.update()
        clock.tick(15)
    
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def button(msg, Msgcolour, x, y, width, height, Inactivecolour, Activecolour, action=None):
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

StartDisplay.fill(Black)
LoadDisplay()

def Smaller():
    StartDisplay = pygame.display.set_mode(MapSize)
    intro = False
    print(intro)
    LoadDisplay()

def Bigger():
    StartDisplay = pygame.display.set_mode(MapSize, pygame.FULLSCREEN)
    intro = False
    print(intro)
    LoadDisplay()

def Quit():
    pygame.quit() 
    sys.exit

while not ExitBool:
    pygame.display.flip()

    if pygame.key.get_pressed()[K_ESCAPE]:
        EscapeMenu()    

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            Quit()