lines = list()
line = "temp"
First = ""

while line != "":
    line = input("Add lines (RETURN for finished)")
    if line != "":
        lines.append(line)

nlines = list()

for line in lines:
    group = line.split("/")
    ngroup = ""
    for index,items in enumerate(group):
        if items != "":
            items = (items[4] + "," + items[2] + "," + items[0] + "," + items[6] + "," + items[8])
            if index != 0:
                ngroup += "/"+items
            else:
                ngroup+= items

        else:
            ngroup += "/"

    nlines.append(ngroup)
lines = nlines
    
for loop in range(len(lines)-1,-1,-1):
    print(lines[loop])