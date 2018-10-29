from Entities import Ghost

class Square:

    CurrentlyContains = Ghost(15,"NotImg")

    def __init__(self, LocationTopLeft, LocationBottomRight, LocationWalls, Contents):
        #LocationTopLeft/BottomRight = [x,y], LocationWalls = [12,3,6,9]
        self.SetCoords(LocationBottomRight,LocationTopLeft)
        self.Walls = LocationWalls
        self.Contnet = Contents

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
        TempListA = list()

        for loop in range(0,4):
            TempListB = list()

            if self.Walls[loop] == True:
                TempListB.append(self.Coords[loop])
                if loop != 3:
                    TempListB.append(self.Coords[loop+1])
                else:
                    TempListB.append(self.Coords[0])
            
            else:
                TempListB.append(Nothing)
                TempListB.append(Nothing)
            
            TempListA.append(TempListB)

        return TempListA

    def DrawSquare(self):
        pass
    
    def DrawWalls(self):
        pass

    def DrawPill(self):
        pass

    def CheckRoute(self,Target):
        pass

    def MoveGhost(self,Target):
        pass

    def MovePac(self,Target):
        #Direction = FindDirection(Target)
        #pygame.draw.rect(Surface, color, Rect, width=0)
        pass

    def Animate(self,Target,Entity):
        pass

    def FindDirection(self,Target):
        if self.Coords[0] == Target.Coords[1]:
            return "L"
        elif self.Coords[0] == Target.Coords[3]:
            return "U"
        elif self.Coords[1] == Target.Coords[0]:
            return "R"
        elif self.Coords[3] == Target.Coords[0]:
            return "D"
        else:
            print("ERROR cannot find direction!")
            return "ERROR"

    def EntityEnter(self, Entity):
        self.CurrentlyContains = Entity
    
    #def FindImage(self):
    #    return (CurrentlyContains.Image)

