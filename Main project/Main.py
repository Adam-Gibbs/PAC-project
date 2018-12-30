import pygame, sys
from pygame.locals import *
from Structs import *
from LoadMap import *
from Entities import *
from GeneralSubs import *
import tkinter as tk
from tkinter import filedialog

clock = pygame.time.Clock()
CurDir = "Maps\Test.txt"

pygame.init()
clock = pygame.time.Clock()
ExitBool = False
Menu = None
Fullscreen = True
ActiveFPS= False
BaseW, BaseH = pygame.display.Info().current_w, pygame.display.Info().current_h
DisplaySize = [BaseW, BaseH]
CurrMap = LoadMap(CurDir, DisplaySize)

StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
White=(255,255,255)
Blue=(0, 0, 255)
DarkBlue=(50,50,200)
Green=(0,255,0)
DarkGreen=(50,200,50)
Red=(255,0,0)
DarkRed=(200,50,50)
Yellow=(255,255,0)
Black=(0,0,0)

def LoadGame():
    StartDisplay.fill(Black)
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row,Column]).GiveWalls()
            for wall in range (0,4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue, (temp[wall][0][0], temp[wall][0][1], temp[wall][1][0], temp[wall][1][1]), 1)  

            if CurrMap.GiveSquare([Row,Column]).GiveContents() == "S":
                pygame.draw.circle(StartDisplay, Yellow, CurrMap.GiveSquare([Row,Column]).GiveCentre(), 3)
            elif CurrMap.GiveSquare([Row,Column]).GiveContents() == "U":
                pygame.draw.circle(StartDisplay, Red, CurrMap.GiveSquare([Row,Column]).GiveCentre(), 6)
            
    pygame.display.update()

def LoadMenu(Mode):
    ActionList = list()
    ResActionList = list()

    if Mode == "Escape":
        for item in EscapeButtons:
            ActionList.append(item.Check())

        for item in ActionList:
            if item != None:
                item()                

    elif Mode == "Resolution":
        global Menu
        for item in EscapeButtons:
            ActionList.append(item.Check())
        
        for item in ResolutionButtons:
            ResActionList.append(item.Check())

        for item in ResActionList:
            if item != None:
                SetResolution(item)
                Menu = "Escape"     
        
        for item in ActionList:
            if item != None:
                item()  
                Menu = "Escape"     

def ToggleFullscreen():
    global Fullscreen, DisplaySize
    if Fullscreen == True:
        StartDisplay = pygame.display.set_mode(DisplaySize)
        Fullscreen = False

    else:
        try:
            StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0], "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)  
            SetButtons()
            LoadMenu(Menu)
        Fullscreen = True

def Return():
    global Menu, CurrMap
    CurrMap = LoadMap(CurDir, DisplaySize)
    Menu = None
    LoadGame()

def Quit():
    pygame.quit() 
    sys.exit

def ToggleFPS():
    global ActiveFPS
    ActiveFPS = not ActiveFPS
    StartDisplay.fill(Black,(5,5,75,25))

def HideSubMenu():
    StartDisplay.fill(Black, (0,80,DisplaySize[0]/3,DisplaySize[1]-80))

def SetResolution(Res):
    global DisplaySize
    DisplaySize = Res

    if Fullscreen == False:
        StartDisplay = pygame.display.set_mode(DisplaySize)
    else:
        try:
            StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0], "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)            

    SetButtons()
    LoadMenu(Menu)
    HideSubMenu()

def ToggleResolution():
    global Menu
    if Menu == "Resolution":
        Menu = "Escape"

    else:
        Menu = "Resolution"
    HideSubMenu()

def MapSelect():
    global CurDir
    root = tk.Tk()
    root.withdraw()
    CurDir = filedialog.askopenfilename()

def SetButtons():
    ButtonProperties = [(0.5*(DisplaySize[0]))-((0.3*DisplaySize[0])/2), (2/3)*((DisplaySize[1]-150)/7), 0.3*DisplaySize[0], (DisplaySize[1]-150)/7] # X, Length, Width, GapTillNext
    global EscapeButtons, ResolutionButtons

    EscapeButtons = [Button("Change Map", White, ButtonProperties[0], 100, ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, MapSelect),
                    Button("Resolution", White, ButtonProperties[0], 100+ButtonProperties[3], ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, ToggleResolution),
                    Button("Toggle Fullscreen", White, ButtonProperties[0], 100+(ButtonProperties[3]*2), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, ToggleFullscreen),
                    Button("Toggle FPS", White, ButtonProperties[0], 100+(ButtonProperties[3]*3), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, ToggleFPS),
                    Button("UI Scale", White, ButtonProperties[0], 100+(ButtonProperties[3]*4), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay),
                    Button("Return", White, ButtonProperties[0], 100+(ButtonProperties[3]*5), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, Return),
                    Button("Quit", White, ButtonProperties[0], 100+(ButtonProperties[3]*6), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, Quit)] 

    ResolutionButtons = [Button("640x480", White, 20, 100, ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [640, 480]),
                        Button("1024x768", White, 20, 100+ButtonProperties[3], ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [1024, 768]),
                        Button("1280x1024", White, 20, 100+(ButtonProperties[3]*2), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [1280, 1024]),
                        Button("1440x900", White, 20, 100+(ButtonProperties[3]*3), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [1440, 900]),
                        Button("1680x1050", White, 20, 100+(ButtonProperties[3]*4), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [1680, 1050]),
                        Button("1920x1200", White, 20, 100+(ButtonProperties[3]*5), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [1920, 1200]),
                        Button("Auto", White, 20, 100+(ButtonProperties[3]*6), ButtonProperties[2], ButtonProperties[1], Black, DarkBlue, StartDisplay, [BaseW, BaseH])]         

SetButtons()
StartDisplay.fill(Black)
LoadGame()
Cycles = 0

while not ExitBool:
    if Cycles == 60:
        Cycles = 0


    else: 
        Cycles += 1

    if pygame.key.get_pressed()[K_ESCAPE]:
        Menu = "Escape"   
        StartDisplay.fill(Black)

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            ExitBool == True
            # if it is quit the game
            Quit()

    if Menu != None:
        TextSurf, TextRect = TextObjects("Debug Menu", pygame.font.Font('freesansbold.ttf',60), Blue)
        TextRect.center = ((DisplaySize[0]/2),(35))
        StartDisplay.blit(TextSurf, TextRect)
        LoadMenu(Menu)

    if ActiveFPS == True:
        StartDisplay.fill(Black,(5,5,75,25))
        FPSText = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = TextObjects(str(round(clock.get_fps(),1)), FPSText, Yellow)
        TextRect.center = (40,20)
        StartDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    clock.tick(60)