from Structs import MapStruct

def PerformMove(From,To):
	pass

def CheckMove(Location, Direction):
	if Map.GiveSquare(Location).GiveWalls()[Direction] == False:    # Checks for walls in current square direction
		SetSquare = Map.FiFindNeighbour(Direction)                	# Finds square you wish to travel to
		return SetSquare.GiveCoordinates() 
	else:                       
        	return Map.GiveSquare(self.Location).GiveCoordinates()		# Reuturns current square if cannot move

def PlanMoves(MemoryLength):
	pass