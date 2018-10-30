from MapStruct import Map
import os

# load map file from here, reading each line, interpreting it to MapSturct

def LoadMap(FileName):
    ReadData = list()

    # Load in File to memory
    with open(FileName) as infile:       # Context manager, automatically closes file
        for line in infile:
            ReadData.append(line.strip("\n"))

    # Load in MetaData
    CurrMap = Map(list(map(int, ReadData[0].split(","))), os.path.basename(FileName)[:-4], ReadData[1]) # List(map, converts list of strings to ints
                                                                                                        # Could use a list comprehension here instead
    # Now load in squares
    while loop = True:
        

    return CurrMap

LoadMap("Maps\Test.txt")
