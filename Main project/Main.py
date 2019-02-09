#!/usr/bin/python3

import os
import random
import sys
import tkinter as tk
from tkinter import filedialog
import time
import pygame
from pygame.locals import *

from Entities import PAC, Ghost
from GeneralSubs import Button, TextObjects
from LoadMap import LoadMap

clock = pygame.time.Clock()

CurDir = os.path.dirname(os.path.realpath(__file__))
if os.name == 'nt':
    CurDir += "//Maps\\BaseMap1.txt"
else:
    CurDir += "/Maps/BaseMap1.txt"

pygame.init()
clock = pygame.time.Clock()
ExitBool = False
Menu = None
Fullscreen = False
ActiveFPS = False
GhostTimer = 0
Ghosts = list()
GhostLocations = list()
BaseW, BaseH = pygame.display.Info().current_w, pygame.display.Info().current_h
DisplaySize = [BaseW, BaseH]
CurrMap = LoadMap(CurDir, DisplaySize)
PreviousTime = 0
IntervalTime = 1
PastAniTime = 0


StartDisplay = pygame.display.set_mode(DisplaySize)#, pygame.FULLSCREEN)
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
    GhostLocations = list()

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
    for Item in Ghosts:
        ClearScreen(Item, True)
        pygame.display.update()
    del Ghosts[:]
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
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
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


def ClearScreen(obj):
    for Coord in obj.ToCoverSquares():
        pygame.draw.rect(StartDisplay, Black,
                        CurrMap.GiveSquare(Coord).GiveRect())

        if type(obj) is Ghost:
            if CurrMap.GiveSquare(Coord).GiveContents() == "S":
                pygame.draw.circle(StartDisplay, Yellow, CurrMap.
                                GiveSquare(Coord).GiveCentre(), 3)

            elif CurrMap.GiveSquare(Coord).GiveContents() == "U":
                pygame.draw.circle(StartDisplay, Red,
                                CurrMap.GiveSquare(Coord).
                                GiveCentre(), 6)

            elif CurrMap.GiveSquare(Coord).GiveContents() == "G":
                pygame.draw.rect(StartDisplay, DarkRed,
                                CurrMap.GiveSquare(Coord)
                                .GiveRect())


def CheckTouching():
    for Item in Ghosts:
        if Player.GiveLocation() == Item.GiveLocation():
            return True, Item
    
    return False, None


def Animate(Item, DistanceIncrease, CurrMap):
    if Item.CheckMovement() is True:
        StartDisplay.blit(Item.GiveImage(),
                          CurrMap.GiveSquare(Item.GivePrev()).
                          GiveModifiedRect(Item.GiveDirection(),
                          DistanceIncrease))
    else:
        StartDisplay.blit(Item.GiveImage(),
                          CurrMap.GiveSquare(Item.GiveLocation()).
                          GiveRect())


def AnimateTime():
    global PastAniTime
    if round(pygame.time.get_ticks()) > PastAniTime + (IntervalTime/10):
        PastAniTime = round(pygame.time.get_ticks())
        return True

    else:
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
                                StartDisplay, [1366, 768]),
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

            elif event.key == pygame.K_d:
                Player.ChangeDirection(1)

            elif event.key == pygame.K_s:
                Player.ChangeDirection(2)

            elif event.key == pygame.K_a:
                Player.ChangeDirection(3)

    if round(pygame.time.get_ticks()) > PreviousTime + IntervalTime and Menu is None:
        PreviousTime = round(pygame.time.get_ticks())
        Player.Move(CurrMap)
        for Item in Ghosts:
            Item.Move(CurrMap, Player, Ghosts)

        for DistanceIncrease in range(10):
            ClearScreen(Player)
            for Item in Ghosts:
                ClearScreen(Item)

            for Item in Ghosts:
                Animate(Item, DistanceIncrease + 1, CurrMap)
            Animate(Player, DistanceIncrease + 1, CurrMap)
            pygame.display.update()
            pygame.time.wait(20)

        # Ghost Spawn
        if len(Ghosts) < CurrMap.GiveMaxGhosts():
            if GhostTimer == 0:
                GhostTimer = random.randint(3, 7)
                Ghosts.append(Ghost(random.choice(GhostLocations), CurrMap
                              .GiveSquare([0, 0]).GiveRect()[1]))
                StartDisplay.blit(Ghosts[-1].GiveImage(),
                                  CurrMap.GiveSquare(Ghosts[-1].GiveLocation())
                                  .GiveRect()[0])
            GhostTimer -= 1

    Touching, Interceptor = CheckTouching()
    if Touching is True and Player.GiveInvincible() is False:
        pygame.display.update()
        pygame.time.delay(500)
        ClearScreen(Player)

        for Item in Ghosts:
            ClearScreen(Item)
            pygame.display.update()
        del Ghosts[:]
        GhostTimer = 0

        StartDisplay.blit(Player.GiveImage(),
                          CurrMap.GiveSquare(Player.GiveLocation())
                          .GiveRect()[0])

        if Player.TakeLife() is True:
            Menu = "Escape"
            StartDisplay.fill(Black)
            Player.Reset()

    if Touching is True and Player.GiveInvincible() is True:
        ClearScreen(Interceptor)
        Player.AddPoints(1)

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            ExitBool is True
            # if it is quit the game
            Quit()

    if Menu is not None:
        TextSurf, TextRect = TextObjects("Menu",
                                         pygame.font.Font('freesansbold.ttf',
                                                          60), Blue)
        TextRect.center = ((DisplaySize[0]/2), (35))
        StartDisplay.blit(TextSurf, TextRect)
        LoadMenu(Menu)

    if not Menu:
        StartDisplay.fill(Black, (0, 0, 200, DisplaySize[1]))
        ScoreFont = pygame.font.Font('freesansbold.ttf',
                                     int(DisplaySize[0]/40))
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

        if Player.GiveInvincible() is True:
            time = Player.InvincibleTime()
            ScoreFont = pygame.font.Font('freesansbold.ttf',
                                         int(DisplaySize[0]/40))
            TextSurf, TextRect = TextObjects(str(time),
                                             ScoreFont, Blue)
            TextRect.center = (100, DisplaySize[0]/3)
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
    clock.tick(200)
