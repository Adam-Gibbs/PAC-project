import numpy
from Squares import Square
from Entities import Button
from Main import Quit, Smaller, Bigger

class MapStruct:
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

class ButtonStruct:
    def __init__(self, Colour, Display):
        self.EscapeButtons = [Button("Quit", Colour[0], 550, 450, 100, 50, Colour[8], Colour[2], Display, Quit), Button("Big", Colour[0], 650, 450, 100, 50, Colour[8], Colour[2], Display, Bigger), Button("Small", Colour[0], 450, 450, 100, 50, Colour[8], Colour[2], Display, Smaller)]

    def GiveButtons(self, Environment):
        if environment == "escape":
            return self.EscapeButtons
               
            