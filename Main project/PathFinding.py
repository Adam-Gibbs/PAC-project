from Structs import MapStruct


def PerformMove(From, To):
    pass


def CheckMove(Location, Direction):
    # Checks for walls in current square direction
    if Map.GiveSquare(Location).GiveWalls()[Direction] is False:
        # Finds square you wish to travel to
        SetSquare = Map.FiFindNeighbour(Direction)
        return SetSquare.GiveCoordinates()
    else:
        # Reuturns current square if cannot move
        return Map.GiveSquare(self.Location).GiveCoordinates()


def PlanMoves(MemoryLength):
    pass
