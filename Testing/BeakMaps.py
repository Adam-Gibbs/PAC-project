import sys
Base = input("Slap it here: ")
Base = "True,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,True,False,False,S/False,False,False,True,E/False,True,False,False,E/True,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,True,False,False,S/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,True,False,True,U/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,U/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/False,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,False,False,S/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,False,False,E/False,False,False,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,False,False,S/False,False,False,True,E/False,True,False,False,E/False,False,True,True,S/True,False,True,False,S/True,False,True,False,S/True,True,False,False,S/False,False,False,True,E/False,True,False,False,E/True,False,False,True,S/True,False,True,False,S/True,False,True,False,S/False,True,True,False,S/False,False,False,True,E/False,True,False,False,E/False,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,True,False,S/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,E/False,False,False,True,E/False,True,False,False,E/False,True,False,True,E/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,E/False,False,True,True,E/False,True,True,False,E/False,True,False,True,E/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/True,False,False,True,E/True,False,True,False,E/True,False,True,False,E/False,False,True,False,E/True,False,False,False,E/True,False,False,False,E/False,False,True,False,E/True,False,True,False,E/True,False,True,False,E/True,True,False,False,E/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,True,True,E/False,True,True,False,E/False,True,False,True,E/True,False,False,True,E/True,False,True,False,E/True,True,True,False,E/False,False,False,True,E/False,True,False,False,E/True,False,True,True,E/True,False,True,False,E/True,True,False,False,E/False,True,False,True,E/False,False,True,True,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,False,False,True,S/True,False,False,False,E/True,False,False,False,E/False,True,False,False,E/False,True,False,True,E/True,False,False,True,G/True,False,False,False,G/False,False,False,False,G/False,False,False,False,G/True,False,False,False,G/True,True,False,False,G/False,True,False,True,E/False,False,False,True,E/True,False,False,False,E/True,False,False,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,False,False,True,S/True,False,True,False,E/False,True,False,False,E/False,True,False,True,E/True,False,True,True,G/True,False,True,False,G/False,False,True,False,G/False,False,True,False,G/True,False,True,False,G/True,True,True,False,G/False,True,False,True,E/False,True,False,True,E/False,False,False,True,E/True,False,True,False,E/True,False,True,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,False,False,True,S/True,False,True,False,E/False,True,False,False,E/False,True,False,True,E/True,False,True,True,G/True,False,True,False,G/True,False,False,False,G/True,False,False,False,G/True,False,True,False,G/True,True,True,False,G/False,True,False,True,E/False,True,False,True,E/False,False,False,True,E/True,False,True,False,E/True,False,True,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,False,False,True,S/False,False,True,False,E/False,False,True,False,E/False,True,False,False,E/False,True,False,True,E/False,False,True,True,G/False,False,True,False,G/False,False,False,False,G/False,False,False,False,G/False,False,True,False,G/False,True,True,False,G/False,True,False,True,E/False,False,False,True,E/False,False,True,False,E/False,False,True,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,True,False,False,E/False,True,False,True,E/False,False,True,True,E/True,False,True,False,E/True,True,True,False,E/False,False,False,True,E/False,True,False,False,E/True,False,True,True,E/True,False,True,False,E/False,True,True,False,E/False,True,False,True,E/True,False,False,True,E/True,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,False,True,True,E/True,False,True,False,E/True,False,True,False,E/True,False,False,False,E/False,False,True,False,E/False,False,True,False,E/True,False,False,False,E/True,False,True,False,E/True,False,True,False,E/False,True,True,False,E/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,E/True,False,False,True,E/True,True,False,False,E/False,True,False,True,E/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,E/False,False,False,True,E/False,True,False,False,E/False,True,False,True,E/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/True,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,False,False,S/False,False,False,True,E/False,True,False,False,E/True,False,False,True,S/True,False,True,False,S/True,False,True,False,S/False,True,True,False,S/False,False,False,True,E/False,True,False,False,E/False,False,True,True,S/True,False,True,False,S/True,False,True,False,S/True,True,False,False,S/False,False,False,True,E/False,True,False,False,E/False,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,True,False,False,S/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/False,False,False,False,E/False,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,False,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,False,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,False,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,False,False,S/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/True,False,False,True,E/True,False,False,False,E/True,False,False,False,E/True,True,False,False,E/False,True,False,True,S/False,True,False,True,U/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,False,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,S/False,False,False,True,E/False,False,False,False,E/False,False,False,False,E/False,True,False,False,E/False,True,False,True,U/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,False,True,E/False,True,False,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,E/False,False,True,False,E/False,False,True,False,E/False,True,True,False,E/False,True,False,True,S/False,False,True,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,True,False,S/False,False,False,True,E/False,True,False,False,E/False,False,True,True,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/True,False,True,False,S/False,True,True,False,S"
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