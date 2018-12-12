lines = list()
line = "temp"
First = ""

while line != "":
    line = input("Add lines (RETURN for finished)")
    if line != "":
        lines.append(line)

for line in lines:
    for i,cha in enumerate(line):
        if i / 10 == 0:
            First = cha
        elif (i-4) / 10 == 0:
            line[i-4] = cha
            cha = First        

for loop in range(len(lines)-1,-1,-1):
    print(lines[loop])