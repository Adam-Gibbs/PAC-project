from Structs import MapStruct
import os

# load map file from here, reading each line, interpreting it to MapSturct.


# This loads in the map file
def LoadMap(FileName, ScreenSize):
    ReadData = list()
    ScreenSize = [ScreenSize[0]-200, ScreenSize[1]]

    # Load in File to memory:
    # Context manager, automatically closes file.
    with open(FileName) as infile:
        for line in infile:
            ReadData.append(line.strip("\n"))

    # List(map, converts list of strings to ints.
    # Could use a list comprehension here instead.
    Size = list(map(int, ReadData[0].split(",")))

    # Then load in MetaData:
    CurrMap = MapStruct(Size, os.path.basename(FileName)[:-4], ReadData[1],
                        ReadData[2], ReadData[3])

    # Now load in squares:
    ReadData = ReadData[4].split("/")
    TempData = list()

    SquareSize = [(ScreenSize[0]-40)/Size[0], (ScreenSize[1]-40)/Size[1]]

    # This loads and splits the wall data for each square
    for index, data in enumerate(ReadData):
        TempData = data.split(",")
        Row = index // Size[0]
        Column = index % Size[0]

        # This creates a square object with this data, saved into map object
        CurrMap.InputSquare([220+((Column)*SquareSize[0]),
                             20+(Row*SquareSize[1])],
                            [220+SquareSize[0]+((Column)*SquareSize[0]),
                             20+SquareSize[1]+((Row)*SquareSize[1])],
                            [TempData[0], TempData[1], TempData[2],
                             TempData[3]], TempData[4], [Column, Row])

    # Map object is returned
    return CurrMap
