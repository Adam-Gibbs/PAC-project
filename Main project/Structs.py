import numpy
from Squares import Square
from GeneralSubs import Button


class MapStruct:
    def __init__(self, _size, _name, _creator):
        self.Creator = _creator
        self.Name = _name
        self.Size = _size
        # Creates an array(of objects) of the inputted size, the datatype of
        # the Square class
        self.Array = numpy.empty(self.Size, dtype=object)

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

    def GiveSquare(self, Location):
        X = Location[0]
        Y = Location[1]

        return self.Array[X][Y]

    def FindNeighbour(self, Direction):
        if Direction == 0:
            return self.array[Direction[0]][Direction[1]+1]

        elif Direction == 1:
            return self.array[Direction[0]+1][Direction[1]]

        elif Direction == 2:
            return self.array[Direction[0]][Direction[1]-1]

        elif Direction == 3:
            return self.array[Direction[0]-1][Direction[1]]

        else:
            return self.array[Direction[0]][Direction[1]]
