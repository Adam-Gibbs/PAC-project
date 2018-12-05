from GeneralSubs import TextObjects
from Structs import MapStruct
import pygame

class Ghost:
        
    def __init__(self, GivenLocation, SetImage):
        self.Location = GivenLocation
        self.Image = SetImage

class PAC:
    
    def __init__(self, GivenLocation):
        self.Location = GivenLocation # map struct locatio [x,y]
        self.Direction

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction
    
    def Move(self, Map):
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction] == False:      # Checks for walls in current square direction
            SetSquare = Map.FiFindNeighbour(self.Direction)                         # Finds square you wish to travel to
            return SetSquare.GiveCoordinates()                                      

        else:                       
            return Map.GiveSquare(self.Location).GiveCoordinates()                  # Reuturns current square if cannot move
        
    #def ChangeProperty(self,Modifier as property, Value):
        #self.Modifier = Value