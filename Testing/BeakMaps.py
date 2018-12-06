import sys
Base = input("Slap it here: ")
times = 0
print("------------------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n")

for character in Base:
    if character == "/":
        times += 1

    sys.stdout.write(character)

    if times == 26:
        sys.stdout.write("\n")
        times=0

    
input("\n\nDone!")