import pygame, sys
from pygame.locals import *
from Squares import Square
#from Entities import Ghost

clock = pygame.time.Clock()
ExitBool = False

S1 = Square([20,20],[170,-130],[True,False,True,True])
S2 = Square([170,20],[320,-130],[True,False,True,True])
S3 = Square([20,170],[170,20],[True,False,True,True])
S4 = Square([170,170],[320,20],[True,False,True,True])
SList = [S1,S2,S3,S4]

StartDisplay = pygame.display.set_mode((340, 340))
White=(255,255,255)
Blue=(0, 0, 255)
Red=(255,0,0)
Yellow=(255,255,0)
Black=(0,0,0)
CList = [Red,Blue,Yellow,Black]

StartDisplay.fill(White)

for loop in range (0,4):
    temp = SList[loop].GiveCoordinates()
    print(temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength())
    pygame.draw.rect(StartDisplay, CList[loop], (temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength()),10)


while not ExitBool:
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 

