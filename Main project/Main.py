import pygame, sys
from pygame.locals import *
from Structs import *
from LoadMap import *
from Entities import *

MapSize = [1200, 800]
pygame.init()
CurrMap = LoadMap("Maps\Test.txt", MapSize)
clock = pygame.time.Clock()
ExitBool = False
Menu = None

StartDisplay = pygame.display.set_mode(MapSize)
White=(255,255,255)
Blue=(0, 0, 255)
DarkBlue=(50,50,200)
Green=(0,255,0)
DarkGreen=(50,200,50)
Red=(255,0,0)
DarkRed=(200,50,50)
Yellow=(255,255,0)
Black=(0,0,0)
Colour=[White, Blue, DarkBlue, Green, DarkGreen, Red, DarkRed, Yellow, Black] 

def LoadGame():
    StartDisplay.fill(Black)
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
            for wall in range (0,4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue, (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 10)        

def LoadMenu(Mode):
    print("HI")
    if Mode == "Escape":
        for item in EscapeButtons:
            item.Check()  

def Smaller():
    StartDisplay = pygame.display.set_mode(MapSize)
    Menu = None
    LoadGame()

def Bigger():
    StartDisplay = pygame.display.set_mode(MapSize, pygame.FULLSCREEN)
    Menu = None
    LoadGame()

def Quit():
    pygame.quit() 
    sys.exit

EscapeButtons = [Button("Quit", Colour[0], 550, 450, 100, 50, Colour[8], Colour[2], StartDisplay, Quit), 
                Button("Big", Colour[0], 650, 450, 100, 50, Colour[8], Colour[2], StartDisplay, Bigger), 
                Button("Small", Colour[0], 450, 450, 100, 50, Colour[8], Colour[2], StartDisplay, Smaller)]

StartDisplay.fill(Black)
LoadGame()

while not ExitBool:
    print("ya")
    if pygame.key.get_pressed()[K_ESCAPE]:
        print("ummmmmmmmmmmmmmmmm")
        Menu = "Escape"   

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            ExitBool == True
            # if it is quit the game
            Quit()

    if Menu != None:
        print(Menu)
        StartDisplay.fill(Black)
        LoadMenu(Menu)

    pygame.display.update()
    clock.tick(15)