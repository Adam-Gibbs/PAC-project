import random

import pygame

from GeneralSubs import TextObjects
from PathFinding import CheckMove, PerformMove
from Structs import MapStruct


class Ghost:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation
        Fname = "/Ghost" + random.randint(0, 9) + ".png"
        OriginalImage = pygame.image.load("PAC-project/Assets" + Fname)
        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))


class PAC:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation  # map struct locatio [x,y]
        OriginalImage = pygame.image.load("PAC-project/Assets/Pacman.png")
        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction

    def GetImage(self):
        return self.Image

    def GetLocation(self):
        return self.Location

    def Move(self, Map):
        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction] is False:
            # Finds square you wish to travel to
            SetSquare = Map.FiFindNeighbour(self.Direction)
            self.Location = SetSquare.GiveCoordinates()
            return self.Location

        else:
            # Reuturns current square if cannot move
            return Map.GiveSquare(self.Location).GiveCoordinates()
