import random

import pygame

from GeneralSubs import TextObjects
from PathFinding import CheckMove, PerformMove
from Structs import MapStruct


class Ghost:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation
        Fname = "/Ghost" + random.randint(0, 9) + ".png"
        OriginalImage = pygame.image.load("Main project/Assets" + Fname)
        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))


class PAC:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation  # map struct locatio [x,y]
        self.Direction = 1
        self.SetImages(SqSize)
        self.Image = self.ImageList[1]

    def SetImages(self, SqSize):
        self.ImageList = list()

        for loop in range(4):
            OriginalImage = pygame.image.load("Main project/Assets/Pacman"
                                              + str(loop) + ".png")
            self.ImageList.append(pygame.transform.scale(OriginalImage,
                                                         (int(SqSize[0]),
                                                          int(SqSize[1]))))

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction
        self.Image = self.ImageList[self.Direction]

    def GetImage(self):
        return self.Image

    def GetLocation(self):
        return self.Location

    def Move(self, Map):
        Location, SetSquare = Map.FindNeighbour(self, self.Direction)

        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction][0] == [0, 0] and SetSquare.GiveContents() != "G":
            # Finds square you wish to travel to
            self.Location = Location

        return self.Location
