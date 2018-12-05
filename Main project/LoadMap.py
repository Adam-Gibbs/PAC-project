from Structs import MapStruct
import os

# load map file from here, reading each line, interpreting it to MapSturct.

def LoadMap(FileName, ScreenSize):
    ReadData = list()
    ScreenSize = [ScreenSize[0]-200,ScreenSize[1]]

    # Load in File to memory:
    with open(FileName) as infile:                  # Context manager, automatically closes file.
        for line in infile:
            ReadData.append(line.strip("\n"))

    Size = list(map(int, ReadData[0].split(",")))   # List(map, converts list of strings to ints. Could use a list comprehension here instead.

    # Then load in MetaData:
    CurrMap = MapStruct(Size, os.path.basename(FileName)[:-4], ReadData[1]) 

    # Now load in squares:
    ReadData = ReadData[2].split("/")
    TempData = list()

    SquareSize = [(ScreenSize[0]-40)/Size[0], (ScreenSize[1]-40)/Size[1]]

    for loop in range (len(ReadData)):
        TempData = ReadData[loop].split(",")
        Row = loop // Size[0]
        Column = loop % Size[0]
        
        CurrMap.InputSquare ([220+((Column)*SquareSize[0]), 20+(Row*SquareSize[1])], [220+SquareSize[0]+((Column)*SquareSize[0]), 20+SquareSize[1]+((Row)*SquareSize[1])], [TempData[0],TempData[1],TempData[2],TempData[3]],TempData[4], [Column,Row]) 

    return CurrMap
