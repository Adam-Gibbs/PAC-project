from MapStruct import Map

# load map file from here, reading each line, interpreting it to MapSturct

ReadData = list()

with open("Maps\Test.txt") as infile:       # Context manager, automatically closes file
    for line in infile:
        ReadData.append(line.strip("\n"))