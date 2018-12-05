
class Square:

    def __init__(self, LocationTopLeft, LocationBottomRight, LocationWalls, Contents):
        # LocationTopLeft/BottomRight = [x,y], LocationWalls = [12,3,6,9]
        self.SetCoords(LocationBottomRight,LocationTopLeft)
        self.Walls = LocationWalls
        self.Contnet = Contents

    # priv
    def SetCoords(self,BottomRight,TopLeft):
        TopRight = list()
        TopRight.append(BottomRight[0])
        TopRight.append(TopLeft[1])
        BottomLeft = list()
        BottomLeft.append(TopLeft[0])
        BottomLeft.append(BottomRight[1])
        self.Coords = [TopLeft] + [TopRight] + [BottomRight] + [BottomLeft]

    def GiveCoordinates(self):
        return self.Coords

    def GiveWidth(self):    
        return (self.Coords[1][0] - self.Coords[0][0])

    def GiveLength(self):
        return (self.Coords[0][1] - self.Coords[3][1])

    def GiveCentre(self):
        TempList = list()
        x = ((self.Coords[0][0] - self.Coords[1][0])/2) + self.Coords[0][0]
        y = ((self.Coords[0][1] - self.Coords[3][1])/2) + self.Coords[0][1]
        TempList.append(x)
        TempList.append(y)
        return TempList

    def GiveWalls(self):
        Nothing = [0,0]
        MasterList = list()

        for loop in range(0,4):
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
                    WidthHeightList.append(abs(self.Coords[loop][0]-self.Coords[loop+1][0]))
                    WidthHeightList.append(abs(self.Coords[loop][1]-self.Coords[loop+1][1]))
                else:
                    WidthHeightList.append(abs(self.Coords[3][0]-self.Coords[0][0]))
                    WidthHeightList.append(abs(self.Coords[3][1]-self.Coords[0][1]))
                    
                TempList.append(WidthHeightList)
            
            else:
                # Provides null values for no walls
                TempList.append(Nothing)
                TempList.append(Nothing)
            
            MasterList.append(TempList)

        return MasterList

    def DrawPill(self):
        pass