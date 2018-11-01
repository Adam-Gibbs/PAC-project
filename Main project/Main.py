import pygame, sys
from pygame.locals import *
from MapStruct import *
from LoadMap import *

pygame.init()
CurrMap = LoadMap("Maps\Test.txt", [1000, 640])
clock = pygame.time.Clock()
ExitBool = False

StartDisplay = pygame.display.set_mode((1000, 640))
White=(255,255,255)
Blue=(0, 0, 255)
Red=(255,0,0)
Yellow=(255,255,0)
Black=(0,0,0)
CList = [Red,Blue,Yellow,Black]

StartDisplay.fill(Black)

for Row in range(CurrMap.GiveSize("X")):
    for Column in range(CurrMap.GiveSize("Y")):
        temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
        for wall in range (0,4):
            print ("Row", Row,", Column", Column, " Wall", wall, ": ", temp[wall])
            # Remember that rect = [TopLeft([X,Y]), width, height]
            pygame.draw.rect(StartDisplay, CList[1], (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 10)

while not ExitBool:
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            sys.exit

