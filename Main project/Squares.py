
class Square:

    # Run when a new square is created, needs the location and walls
    def __init__(self, LocationTopLeft, LocationBottomRight,
                 LocationWalls, Contents):
        # LocationTopLeft/BottomRight = [x,y], LocationWalls = [12,3,6,9]
        self._SetCoords(LocationBottomRight, LocationTopLeft)
        self.Walls = LocationWalls
        self.Content = Contents

    # Method to get the coords of all four corners
    def _SetCoords(self, BottomRight, TopLeft):
        TopRight = list()
        TopRight.append(BottomRight[0])
        TopRight.append(TopLeft[1])
        BottomLeft = list()
        BottomLeft.append(TopLeft[0])
        BottomLeft.append(BottomRight[1])
        self.Coords = [TopLeft] + [TopRight] + [BottomRight] + [BottomLeft]

    # Returns the coordinats of all four corners
    def GiveCoordinates(self):
        return self.Coords

    # Gives the pygame rect argument of square as a whole
    def GiveRect(self):
        return ((self.Coords[0][0]+1, self.Coords[0][1]+1),
                ((self.Coords[1][0] - self.Coords[0][0])-2,
                (self.Coords[2][1] - self.Coords[0][1])-2))

    # This gives a pygame rect argument for two squares combined
    def GiveModifiedRect(self, _Direction, _Magnitude):
        if _Direction % 2 == 0:
            ChangeValue = (self.GiveLength() / 10) * _Magnitude
        else:
            ChangeValue = (self.GiveWidth() / 10) * _Magnitude

        if _Direction == 0:
            return ((self.Coords[0][0]+1, self.Coords[0][1]+1+ChangeValue),
                    ((self.Coords[1][0] - self.Coords[0][0])-2,
                    (self.Coords[2][1] - self.Coords[0][1])-2))

        elif _Direction == 1:
            return ((self.Coords[0][0]+1+ChangeValue, self.Coords[0][1]+1),
                    ((self.Coords[1][0] - self.Coords[0][0])-2,
                    (self.Coords[2][1] - self.Coords[0][1])-2))

        elif _Direction == 2:
            return ((self.Coords[0][0]+1, (self.Coords[0][1]+1)-ChangeValue),
                    ((self.Coords[1][0] - self.Coords[0][0])-2,
                    (self.Coords[2][1] - self.Coords[0][1])-2))

        else:
            return (((self.Coords[0][0]+1)-ChangeValue, self.Coords[0][1]+1),
                    ((self.Coords[1][0] - self.Coords[0][0])-2,
                    (self.Coords[2][1] - self.Coords[0][1])-2))

    # This returns the width of the square
    def GiveWidth(self):
        return (self.Coords[1][0] - self.Coords[0][0])

    # This returns the length of the square
    def GiveLength(self):
        return (self.Coords[0][1] - self.Coords[3][1])

    # This gives the cordinates of the centre of the square
    def GiveCentre(self):
        TempList = list()
        x = ((self.Coords[1][0] - self.Coords[0][0])/2) + self.Coords[0][0]
        y = ((self.Coords[3][1] - self.Coords[0][1])/2) + self.Coords[0][1]
        TempList.append(int(round(x, 0)))
        TempList.append(int(round(y, 0)))
        return TempList

    # This returns the current contents of the square
    def GiveContents(self):
        return self.Content

    # This makes the contests empty
    def ClearContents(self):
        self.Content = "E"

    # This returns the walls and their size and location
    def GiveWalls(self):
        Nothing = [0, 0]
        MasterList = list()

        # Loops through all four cardinal directions
        for loop in range(0, 4):
            TempList = list()

            if self.Walls[loop] == 'True':
                # Sets X/Y for top left of each wall
                if loop < 2:
                    TempList.append(self.Coords[loop])
                elif loop == 2:
                    TempList.append(self.Coords[3])
                else:
                    TempList.append(self.Coords[0])

                # Sets Width/Height for wall
                WidthHeightList = list()
                if loop != 3:
                    # First appened value is the width, second is the height
                    WidthHeightList.append(abs(self.Coords[loop][0] -
                                               self.Coords[loop+1][0]))
                    WidthHeightList.append(abs(self.Coords[loop][1] -
                                               self.Coords[loop+1][1]))
                else:
                    WidthHeightList.append(abs(self.Coords[3][0] -
                                               self.Coords[0][0]))
                    WidthHeightList.append(abs(self.Coords[3][1] -
                                               self.Coords[0][1]))

                TempList.append(WidthHeightList)

            else:
                # Provides null values for no walls
                TempList.append(Nothing)
                TempList.append(Nothing)

            # Appends the current wall info
            MasterList.append(TempList)

        return MasterList
        