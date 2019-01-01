from GeneralSubs import TextObjects
from Structs import MapStruct
from PathFinding import PerformMove, CheckMove
import pygame


class Ghost:

    def __init__(self, GivenLocation, SetImage):
        self.Location = GivenLocation
        self.Image = SetImage


class PAC:

    def __init__(self, GivenLocation):
        self.Location = GivenLocation  # map struct locatio [x,y]
        self.Direction

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction

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
