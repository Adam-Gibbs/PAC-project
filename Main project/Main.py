import pygame, sys
from pygame.locals import *
from Structs import *
from LoadMap import *
from Entities import *
from GeneralSubs import *

clock = pygame.time.Clock()

DisplaySize = [1200, 800]
pygame.init()
CurrMap = LoadMap("Maps\Test.txt", DisplaySize)
clock = pygame.time.Clock()
ExitBool = False
Menu = None
Fullscreen = False
ActiveFPS= False

StartDisplay = pygame.display.set_mode(DisplaySize)
White=(255,255,255)
Blue=(0, 0, 255)
DarkBlue=(50,50,200)
Green=(0,255,0)
DarkGreen=(50,200,50)
Red=(255,0,0)
DarkRed=(200,50,50)
Yellow=(255,255,0)
Black=(0,0,0)

def LoadGame():
    StartDisplay.fill(Black)
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
            for wall in range (0,4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue, (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 10)        
    pygame.display.update()

def LoadMenu(Mode):
    ActionList = list()

    if Mode == "Escape":
        for item in EscapeButtons:
            ActionList.append(item.Check())

        for item in ActionList:
            if item != None:
                item()

    elif Mode == "Resolution":
        for item in EscapeButtons:
            ActionList.append(item.Check())
        
        for item in ResolutionButtons:
            ActionList.append(item.Check())
        
        for item in ActionList:
            if item != None:
                item()
                HideSubMenu()
        


def ToggleFullscreen():
    global Fullscreen
    if Fullscreen == True:
        StartDisplay = pygame.display.set_mode(DisplaySize)
    else:
        StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)

def HideSubMenu():
    StartDisplay.fill(Black, rect=(0, 100, 0.35*DisplaySize[0], DisplaySize[1]))
    global Menu
    Mode = "Escape"

def Return():
    global Menu
    Menu = None
    LoadGame()

def Quit():
    pygame.quit() 
    sys.exit

def ToggleFPS():
    global ActiveFPS
    ActiveFPS = not ActiveFPS

ButtonProperties = [(0.5*(DisplaySize[0]))-((0.3*DisplaySize[0])/2), (2/3)*((DisplaySize[1]-150)/7), 0.3*DisplaySize[0], (DisplaySize[1]-150)/7] # X, Length, Width, GapTillNext

EscapeButtons = [Button("Change Map", White, ButtonProperties[0], 100, ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay),
                Button("Resolution", White, ButtonProperties[0], 100+ButtonProperties[3], ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay),
                Button("Toggle Fullscreen", White, ButtonProperties[0], 100+(ButtonProperties[3]*2), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, ToggleFullscreen),
                Button("Toggle FPS", White, ButtonProperties[0], 100+(ButtonProperties[3]*3), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, ToggleFPS),
                Button("UI Scale", White, ButtonProperties[0], 100+(ButtonProperties[3]*4), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay),
                Button("Return", White, ButtonProperties[0], 100+(ButtonProperties[3]*5), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, Return),
                Button("Quit", White, ButtonProperties[0], 100+(ButtonProperties[3]*6), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, Quit)] 

#ResolutionButtons =                

StartDisplay.fill(Black)
LoadGame()

while not ExitBool:
    if pygame.key.get_pressed()[K_ESCAPE]:
        Menu = "Escape"   

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            ExitBool == True
            # if it is quit the game
            Quit()

    if Menu != None:
        StartDisplay.fill(Black)
        largeText = pygame.font.SysFont('freesansbold.ttf',35)
        TextSurf, TextRect = TextObjects("Debug Menu", largeText, Blue)
        TextRect.center = ((DisplaySize[0]/2),(35))
        StartDisplay.blit(TextSurf, TextRect)
        LoadMenu(Menu)

    if ActiveFPS == True:
        FPSText = pygame.font.Font('freesansbold.ttf',1)
        TextSurf, TextRect = TextObjects(str(round(clock.get_fps(),1)), largeText, Yellow)
        TextRect.center = (40,20)
        StartDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    clock.tick(120)