import numpy
from Squares import Square


class MapStruct:
    # Run when a new map is loaded, needs all the info from the file
    def __init__(self, _size, _name, _creator, _totpoints, _maxghosts):
        self.Creator = _creator
        self.Name = _name
        self.Size = _size
        self.TotPoints = _totpoints
        self.MaxGhosts = int(_maxghosts)
        # Creates an array(of objects) of the inputted size, the datatype of
        # the Square class
        self.Array = numpy.empty(self.Size, dtype=object)

    # Stores a square object in the structure
    def InputSquare(self, TopLeft, BottomRight, Walls, Contents, Location):
        X = Location[0]
        Y = Location[1]

        self.Array[X][Y] = Square(TopLeft, BottomRight, Walls, Contents)

    # Returns the X and Y size of the whole map
    def GiveSize(self, Peram):
        if Peram == "X":
            return self.Size[0]

        elif Peram == "Y":
            return self.Size[1]

        else:
            return self.Size

    # Returns the total points availible on the map
    def GiveTotPoints(self):
        return self.TotPoints

    # Returns the max ammount of ghosts on the map
    def GiveMaxGhosts(self):
        return self.MaxGhosts

    # Returns a particular square object from map location
    def GiveSquare(self, Location):
        X = Location[0]
        Y = Location[1]

        return self.Array[X][Y]

    # Returns the nearby square to annother
    def FindNeighbour(self, Sprite, Direction):
        Location = Sprite.GiveLocation()

        # A try except loop if the square does not exist, the edge of the map
        try:
            if Direction == 0:
                return [Location[0], Location[1]-1], self.Array[Location[0]][Location[1]-1]

            elif Direction == 1:
                return [Location[0]+1, Location[1]], self.Array[Location[0]+1][Location[1]]

            elif Direction == 2:
                return [Location[0], Location[1]+1], self.Array[Location[0]][Location[1]+1]

            elif Direction == 3:
                return [Location[0]-1, Location[1]], self.Array[Location[0]-1][Location[1]]

        except:
            print("except")
            return [Location[0], Location[1]], self.Array[Location[0]][Location[1]]
