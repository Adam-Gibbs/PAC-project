import numpy
from Squares import Square

class Map:
    def __init__(self, _size, _name, _creator):
        self.Creator = _creator
        self.Name = _name
        self.Size = _size
        self.Array = numpy.empty(self.Size, dtype=object) # Creates an array of the inputted size, the datatype of the Square class

    def InputSquare(self, TopLeft, BottomRight, Walls, Contents, Location):
        X = Location[0]
        Y = Location[1]

        self.Array[X][Y] = Square(TopLeft, BottomRight, Walls, Contents)

    def GiveSize(self, Peram):
        if Peram == "X":
            return self.Size[0]

        elif Peram == "Y":
            return self.Size[1]

        else:
            return self.Size

    def GiveSquare(self,Location):
        X = Location[0]
        Y = Location[1]

        return self.Array[X][Y]            
            