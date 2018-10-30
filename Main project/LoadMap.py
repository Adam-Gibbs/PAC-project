from MapStruct import Map
import os

# load map file from here, reading each line, interpreting it to MapSturct

ReadData = list()
FileName = "Maps\Test.txt"

with open(FileName) as infile:       # Context manager, automatically closes file
    for line in infile:
        ReadData.append(line.strip("\n"))

print(os.path.basename(FileName)[:-4])
CurrMap = Map(ReadData[0].split(","),os.path.basename(FileName),ReadData[1])