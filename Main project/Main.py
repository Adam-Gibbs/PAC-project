import pygame, sys
from pygame.locals import *
from Squares import Square
#from Entities import Ghost

clock = pygame.time.Clock()
ExitBool = False

S1 = Square([100,100],[0,0],[False,False,False,True],"E")
S2 = Square([100,100],[0,0],[False,False,False,False],"E")
S3 = Square([100,100],[0,0],[False,False,True,False],"E")
S4 = Square([100,100],[0,0],[False,False,False,True],"E")
# S2 = Square([170,20],[320,-130],[True,False,True,True])
# S3 = Square([20,170],[170,20],[True,False,True,True])
# S4 = Square([170,170],[320,20],[True,False,True,True])
SList = [S1,S2,S3,S4]

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


temp = S1.GiveWalls()
for loop in range (0,4):
    # temp = SList[loop].GiveCoordinates()
    # print(temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength())
    # pygame.draw.rect(StartDisplay, CList[loop], (temp[0][0],temp[0][1],SList[loop].GiveWidth(),SList[loop].GiveLength()),10)
    print(temp[loop])
    pygame.draw.rect(StartDisplay, CList[0], (temp[loop][0][0], temp[loop][0][1], temp[loop][1][1], temp[loop][1][0]),10)

while not ExitBool:
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            sys.exit

