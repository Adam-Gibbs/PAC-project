import os
import random

import pygame

from GeneralSubs import TextObjects
from Structs import MapStruct


class Ghost:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation
        self.Previous = GivenLocation

        if os.name == 'nt':
            Fname = "\\Ghost" + str(random.randint(0, 9)) + ".png"
            OriginalImage = pygame.image.load("Main project\\Assets" + Fname)
        else:
            Fname = "/Ghost" + str(random.randint(0, 9)) + ".png"
            OriginalImage = pygame.image.load("Main project/Assets" + Fname)

        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))

    def Move(self, Map, Player, Ghosts):
        Rating = list()
        GhostLocation = list()

        for Direction in range(4):
            Pos, Square = Map.FindNeighbour(self, Direction)

            for Item in Ghosts:
                GhostLocation.append(Item.GiveLocation())

            if Map.GiveSquare(self.Location).GiveWalls()[Direction][0] != [0,
                                                                           0]:
                Rating.append(-1)

            elif Pos in GhostLocation:
                Rating.append(-1)
            elif self.Previous == Pos:
                Rating.append(0)
            elif Square.GiveContents() == "G":
                Rating.append(1)
            elif Square.GiveContents() == "E":
                Rating.append(2)
            elif Player.GiveLocation() == Pos:
                Rating.append(4)
            else:
                Rating.append(3)

        if max(Rating) >= 0:
            self.Location, Sq = Map.FindNeighbour(self,
                                                    Rating.index(max(Rating)))

        return self.Location

    def GiveLocation(self):
        return self.Location

    def GiveImage(self):
        return self.Image


class PAC:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation  # map struct location [x,y]
        self.Direction = 1
        self.SetImages(SqSize)
        self.Image = self.ImageList[1]
        self.Points = 0
        self.Lives = 3

    def SetImages(self, SqSize):
        self.ImageList = list()

        for loop in range(4):
            if os.name == 'nt':
                OriginalImage = pygame.image.load("Main project\\Assets\\" +
                                                  "Pacman" + str(loop) + ".png"
                                                  )
            else:
                OriginalImage = pygame.image.load("Main project/Assets/Pacman"
                                                  + str(loop) + ".png")
            self.ImageList.append(pygame.transform.scale(OriginalImage,
                                                         (int(SqSize[0]),
                                                          int(SqSize[1]))))

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction
        self.Image = self.ImageList[self.Direction]

    def GivePoints(self):
        return self.Points

    def GiveLives(self):
        return self.Lives

    def GiveImage(self):
        return self.Image

    def GiveLocation(self):
        return self.Location

    def Reset(self):
        self.Direction = 1
        self.Image = self.ImageList[1]
        self.Points = 0
        self.Lives = 0

    def Move(self, Map):
        Location, SetSquare = Map.FindNeighbour(self, self.Direction)

        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction][0] == [0, 0] and SetSquare.GiveContents() != "G":
            # Finds square you wish to travel to
            self.Location = Location

            if SetSquare.GiveContents() == "S":
                self.Points += 1
                SetSquare.ClearContents()

        return self.Location
