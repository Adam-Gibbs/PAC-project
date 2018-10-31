import pygame, sys
from pygame.locals import *
from MapStruct import Map

CurrMap = Map([4,3],"TestMap","Adam")
clock = pygame.time.Clock()
ExitBool = False

CurrMap.InputSquare([20,20],[260,220],[True,False,False,True],"E",[0,0]) 
CurrMap.InputSquare([260,20],[500,220],[True,True,False,False],"E",[1,0])
CurrMap.InputSquare([500,20],[740,220],[True,False,False,True],"P",[2,0])
CurrMap.InputSquare([740,20],[980,220],[True,True,False,False],"E",[3,0])
CurrMap.InputSquare([20,220],[260,420],[False,False,False,True],"E",[0,1])
CurrMap.InputSquare([260,220],[500,420],[False,False,True,False],"S",[1,1])
CurrMap.InputSquare([500,220],[740,420],[False,False,False,False],"S",[2,1])
CurrMap.InputSquare([740,220],[980,420],[False,True,False,False],"E",[3,1])
CurrMap.InputSquare([20,420],[260,620],[False,False,True,True],"E",[0,2])
CurrMap.InputSquare([260,420],[500,620],[False,True,True,False],"G",[1,2])
CurrMap.InputSquare([500,420],[740,620],[False,False,True,True],"E",[2,2])
CurrMap.InputSquare([740,420],[980,620],[False,True,True,False],"U",[3,2])

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

