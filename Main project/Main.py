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
Green=(0,255,0)
DarkGreen=(50,200,50)
Red=(255,0,0)
DarkRed=(200,50,50)
Yellow=(255,255,0)
Black=(0,0,0)

def LoadDisplay():
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
            for wall in range (0,4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue, (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 10)

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        StartDisplay.fill(Black)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((MapSize[0]/2),(MapSize[1]/2))
        StartDisplay.blit(TextSurf, TextRect)

        button("GO!",White,150,450,100,50,Black,Black,Smaller)
        button("Quit",White,550,450,100,50,Black,Black,Quit)

        pygame.display.update()
        clock.tick(15)
    
def text_objects(text, font):
    textSurface = font.render(text, True, Red)
    return textSurface, textSurface.get_rect()

def button(msg, Msgcolour, x, y, width, height, Inactivecolour, Activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(StartDisplay, Activecolour,(x,y,width,height))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(StartDisplay, Inactivecolour,(x,y,width,height))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    StartDisplay.blit(textSurf, textRect)

StartDisplay.fill(Black)
LoadDisplay()

def Smaller():
    StartDisplay = pygame.display.set_mode(MapSize)
    LoadDisplay()

def Quit():
    pygame.quit() 
    sys.exit

while not ExitBool:
    pygame.display.flip()

    if pygame.key.get_pressed()[K_ESCAPE]:
        game_intro()    

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            Quit()