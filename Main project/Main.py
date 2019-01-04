import os
import sys
import tkinter as tk
from tkinter import filedialog

import pygame
from pygame.locals import *

from Entities import *
from GeneralSubs import *
from LoadMap import *
from Structs import *

clock = pygame.time.Clock()

if os.name == 'nt':
    CurDir = "Main project\\Maps\\BaseMap1.txt"
else:
    CurDir = "Main project/Maps/BaseMap1.txt"

pygame.init()
clock = pygame.time.Clock()
ExitBool = False
Menu = None
Fullscreen = True
ActiveFPS = False
GhostTimer = 0
GhostLocations = list()
Ghosts = list()
BaseW, BaseH = pygame.display.Info().current_w, pygame.display.Info().current_h
DisplaySize = [BaseW, BaseH]
CurrMap = LoadMap(CurDir, DisplaySize)

StartDisplay = pygame.display.set_mode(DisplaySize)  # , pygame.FULLSCREEN)
White = (255, 255, 255)
Blue = (0, 0, 255)
DarkBlue = (0, 0, 55)
Green = (0, 255, 0)
DarkGreen = (0, 55, 0)
Red = (255, 0, 0)
DarkRed = (55, 0, 0)
Yellow = (255, 255, 0)
Black = (0, 0, 0)
int(CurrMap.GiveMaxGhosts())


def LoadGame():
    global Player, GhostLocations

    StartDisplay.fill(Black)
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row, Column]).GiveWalls()
            for wall in range(0, 4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue,
                                 (temp[wall][0][0], temp[wall][0][1],
                                  temp[wall][1][0], temp[wall][1][1]), 1)

            if CurrMap.GiveSquare([Row, Column]).GiveContents() == "S":
                pygame.draw.circle(StartDisplay, Yellow, CurrMap.
                                   GiveSquare([Row, Column]).GiveCentre(), 3)

            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "U":
                pygame.draw.circle(StartDisplay, Red,
                                   CurrMap.GiveSquare([Row, Column]).
                                   GiveCentre(), 6)

            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "G":
                pygame.draw.rect(StartDisplay, DarkRed,
                                 CurrMap.GiveSquare([Row, Column]).GiveRect())
                GhostLocations.append([Row, Column])

            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "P":
                Player = PAC([Row, Column], CurrMap.GiveSquare([Row, Column])
                             .GiveRect()[1])
                StartDisplay.blit(Player.GiveImage(),
                                  CurrMap.GiveSquare([Row, Column])
                                  .GiveRect()[0])

    pygame.display.update()


def LoadMenu(Mode):
    ActionList = list()
    ResActionList = list()

    if Mode == "Escape":
        for item in EscapeButtons:
            ActionList.append(item.Check())

        for item in ActionList:
            if item is not None:
                item()

    elif Mode == "Resolution":
        global Menu
        for item in EscapeButtons:
            ActionList.append(item.Check())

        for item in ResolutionButtons:
            ResActionList.append(item.Check())

        for item in ResActionList:
            if item is not None:
                SetResolution(item)
                Menu = "Escape"

        for item in ActionList:
            if item is not None:
                item()
                Menu = "Escape"


def ToggleFullscreen():
    global Fullscreen, DisplaySize
    if Fullscreen is True:
        pygame.display.set_mode(DisplaySize)

    else:
        try:
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0],
                  "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
            SetButtons()
            LoadMenu(Menu)

    Fullscreen = not Fullscreen


def Return():
    global Menu, CurrMap, GhostTimer
    CurrMap = LoadMap(CurDir, DisplaySize)
    Menu = None
    GhostTimer = 0
    LoadGame()


def Quit():
    pygame.quit()
    sys.exit


def ToggleFPS():
    global ActiveFPS
    ActiveFPS = not ActiveFPS
    StartDisplay.fill(Black, (5, 5, 75, 25))


def HideSubMenu():
    StartDisplay.fill(Black, (0, 80, DisplaySize[0]/3, DisplaySize[1]-80))


def SetResolution(Res):
    global DisplaySize
    DisplaySize = Res

    if not Fullscreen:
        pygame.display.set_mode(DisplaySize)
    else:
        try:
            pygame.display.set_mode(DisplaySize)  # , pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0],
                  "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)

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


def ClearScreen(obj, Gh = False):
    pygame.draw.rect(StartDisplay, Black,
                     CurrMap.GiveSquare(obj.GiveLocation()).GiveRect())

    if Gh is True:
        if CurrMap.GiveSquare(obj.GiveLocation()).GiveContents() == "S":
            pygame.draw.circle(StartDisplay, Yellow, CurrMap.
                               GiveSquare(obj.GiveLocation()).GiveCentre(), 3)

        elif CurrMap.GiveSquare(obj.GiveLocation()).GiveContents() == "U":
            pygame.draw.circle(StartDisplay, Red,
                               CurrMap.GiveSquare(obj.GiveLocation()).
                               GiveCentre(), 6)

        elif CurrMap.GiveSquare(obj.GiveLocation()).GiveContents() == "G":
            pygame.draw.rect(StartDisplay, DarkRed,
                             CurrMap.GiveSquare(obj.GiveLocation())
                             .GiveRect())


def CheckTouching():
    for Item in Ghosts:
        if Player.GiveLocation() == Item.GiveLocation():
            return True
    
    return False


def MapSelect():
    global Fullscreen, CurDir

    pygame.display.set_mode(DisplaySize)
    root = tk.Tk()
    root.withdraw()
    CurDir = filedialog.askopenfilename()
    Fullscreen = not Fullscreen
    ToggleFullscreen()


def SetButtons():
    global EscapeButtons, ResolutionButtons
    # X, Length, Width, GapTillNext
    ButtonProperties = [(0.5*(DisplaySize[0]))-((0.3*DisplaySize[0])/2),
                        (2/3)*((DisplaySize[1]-150)/7), 0.3*DisplaySize[0],
                        (DisplaySize[1]-150)/7
                        ]
    
    EscapeButtons = [Button("Change Map", White, ButtonProperties[0], 100,
                            ButtonProperties[2], ButtonProperties[1], Black,
                            DarkBlue, StartDisplay, MapSelect),
                     Button("Resolution", White, ButtonProperties[0],
                            100+ButtonProperties[3], ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue,
                            StartDisplay, ToggleResolution),
                     Button("Toggle Fullscreen", White, ButtonProperties[0],
                            100+(ButtonProperties[3]*2), ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue,
                            StartDisplay, ToggleFullscreen),
                     Button("Toggle FPS", White, ButtonProperties[0],
                            100+(ButtonProperties[3]*3), ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue,
                            StartDisplay, ToggleFPS),
                     Button("UI Scale", White, ButtonProperties[0],
                            100+(ButtonProperties[3]*4), ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue,
                            StartDisplay),
                     Button("Return", White, ButtonProperties[0],
                            100+(ButtonProperties[3]*5), ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue, StartDisplay,
                            Return),
                     Button("Quit", White, ButtonProperties[0],
                            100+(ButtonProperties[3]*6), ButtonProperties[2],
                            ButtonProperties[1], Black, DarkBlue, StartDisplay,
                            Quit)
                     ]

    ResolutionButtons = [Button("640x480", White, 20, 100, ButtonProperties[2],
                                ButtonProperties[1], Black, DarkBlue,
                                StartDisplay, [640, 480]),
                         Button("1024x768", White, 20, 100+ButtonProperties[3],
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [1024, 768]),
                         Button("1280x1024", White, 20,
                                100+(ButtonProperties[3]*2),
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [1280, 1024]),
                         Button("1440x900", White, 20,
                                100+(ButtonProperties[3]*3),
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [1440, 900]),
                         Button("1680x1050", White, 20,
                                100+(ButtonProperties[3]*4),
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [1680, 1050]),
                         Button("1920x1080", White, 20,
                                100+(ButtonProperties[3]*5),
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [1920, 1080]),
                         Button("Auto", White, 20, 100+(ButtonProperties[3]*6),
                                ButtonProperties[2], ButtonProperties[1],
                                Black, DarkBlue, StartDisplay, [BaseW, BaseH])
                         ]


SetButtons()
StartDisplay.fill(Black)
LoadGame()

while not ExitBool:
    Move = False

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                Menu = "Escape"
                StartDisplay.fill(Black)

            elif event.key == pygame.K_w:
                Player.ChangeDirection(0)
                Move = True

            elif event.key == pygame.K_d:
                Player.ChangeDirection(1)
                Move = True

            elif event.key == pygame.K_s:
                Player.ChangeDirection(2)
                Move = True

            elif event.key == pygame.K_a:
                Player.ChangeDirection(3)
                Move = True

    if Move is True:
        ClearScreen(Player)
        StartDisplay.blit(Player.GiveImage(),
                          CurrMap.GiveSquare(Player.Move(CurrMap))
                          .GiveRect()[0])

        for Item in Ghosts:
            ClearScreen(Item, Flase)
            StartDisplay.blit(Item.GiveImage(),
                              CurrMap.GiveSquare(Item.Move(CurrMap, Player,
                                                           Ghosts))
                              .GiveRect()[0])

        if len(Ghosts) < CurrMap.GiveMaxGhosts():
            if GhostTimer == 0:
                GhostTimer = random.randint(3, 7)
                Ghosts.append(Ghost(random.choice(GhostLocations), CurrMap
                              .GiveSquare([0, 0]).GiveRect()[1]))
                StartDisplay.blit(Ghosts[-1].GiveImage(),
                                  CurrMap.GiveSquare(Ghosts[-1].GiveLocation())
                                  .GiveRect()[0])

            GhostTimer -= 1

    if CheckTouching() is True:
        if Player.TakeLife() is True:
            Menu = "Escape"
            StartDisplay.fill(Black)
            Player.Reset()

        ClearScreen(Player)
        Player.Reset()
        StartDisplay.blit(Player.GiveImage(),
                          CurrMap.GiveSquare(Player.Move(CurrMap))
                          .GiveRect()[0])

        for Item in Ghosts:
            ClearScreen(Item, Flase)
        del Ghosts[:]
        GhostTimer = 0

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            ExitBool is True
            # if it is quit the game
            Quit()

    if Menu is not None:
        TextSurf, TextRect = TextObjects("Debug Menu",
                                         pygame.font.Font('freesansbold.ttf',
                                                          60), Blue)
        TextRect.center = ((DisplaySize[0]/2), (35))
        StartDisplay.blit(TextSurf, TextRect)
        LoadMenu(Menu)

    if Menu is None:
        StartDisplay.fill(Black, (0, 0, 200, DisplaySize[1]))
        ScoreFont = pygame.font.Font('freesansbold.ttf', int(DisplaySize[0]/40))
        TextSurf, TextRect = TextObjects("Score:", ScoreFont, Blue)
        TextRect.center = (100, DisplaySize[0]/10)
        StartDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = TextObjects(str(Player.GivePoints()),
                                         ScoreFont, Blue)
        TextRect.center = (100, DisplaySize[0]/8)
        StartDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = TextObjects("Lives:", ScoreFont, Blue)
        TextRect.center = (100, DisplaySize[0]/4.5)
        StartDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = TextObjects(str(Player.GiveLives()),
                                         ScoreFont, Blue)
        TextRect.center = (100, DisplaySize[0]/4)
        StartDisplay.blit(TextSurf, TextRect)

    if ActiveFPS is True:
        FPSText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = TextObjects(str(round(clock.get_fps(), 1)),
                                         FPSText, Yellow)
        TextRect.center = (40, 20)
        StartDisplay.blit(TextSurf, TextRect)

    if Player.GivePoints() == int(CurrMap.GiveTotPoints()):
        Menu = "Escape"
        StartDisplay.fill(Black)
        Player.Reset()

    pygame.display.update()
    clock.tick(60)
