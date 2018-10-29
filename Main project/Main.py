import pygame, sys
from pygame.locals import *
from MapStruct import Map
#from Entities import Ghost

CurrMap = Map([1,1])
clock = pygame.time.Clock()
ExitBool = False

CurrMap.InputSquare([170,20],[320,130],[True,True,False,True],"E",[0,0])
CurrMap.InputSquare([170,20],[320,-130],[True,True,True,True],"E",[0,1])
CurrMap.InputSquare([20,170],[170,20],[True,True,True,True],"E",[1,0])
CurrMap.InputSquare([170,170],[320,20],[True,True,True,True],"E",[1,1])

StartDisplay = pygame.display.set_mode((340, 340))
White=(255,255,255)
Blue=(0, 0, 255)
Red=(255,0,0)
Yellow=(255,255,0)
Black=(0,0,0)
CList = [Red,Blue,Yellow,Black]

StartDisplay.fill(White)

def LoadMap():
    pass

for Row in range(CurrMap.GiveSize("X"))
    for Collumn in range(CurrMap.GiveSize("Y"))
        temp = CurrMap.GiveSquare([Row,Collumn]).GiveWalls()
        for wall in range (0,4):
            # temp = SList[loop].GiveCoordinates()
            # print(temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength())
            # pygame.draw.rect(StartDisplay, CList[loop], (temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength()),10)

            pygame.draw.rect(StartDisplay, CList[0], (temp[loop][0][0], temp[loop][0][1], temp[loop][1][0], temp[loop][1][1]), 10)

while not ExitBool:
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            sys.exit

