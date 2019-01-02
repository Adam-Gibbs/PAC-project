from GeneralSubs import TextObjects
from Structs import MapStruct
from PathFinding import PerformMove, CheckMove
import pygame


class Ghost:

    def __init__(self, GivenLocation, SetImage):
        self.Location = GivenLocation
        self.Image = SetImage


class PAC:

    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation  # map struct locatio [x,y]
        OriginalImage = pygame.image.load("PAC-project/Assets/Pacman.png")
        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]), int(SqSize[1])))
        
    def ChangeDirection(self, _Direction):
        self.Direction = _Direction

    def GetImage(self):
        return self.Image

    def Move(self, Map):
        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction] is False:
            # Finds square you wish to travel to
            SetSquare = Map.FiFindNeighbour(self.Direction)
            return SetSquare.GiveCoordinates()

        else:
            # Reuturns current square if cannot move
            return Map.GiveSquare(self.Location).GiveCoordinates()

    # def ChangeProperty(self,Modifier as property, Value):
        # self.Modifier = Value
