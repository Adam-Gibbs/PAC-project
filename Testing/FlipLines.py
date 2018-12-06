lines = list()
line = "temp"

while line != "":
    line = input("Add lines (RETURN for finished)")
    if line != "":
        lines.append(line)

for loop in range(len(lines)-1,0,-1):
    print(lines[loop])