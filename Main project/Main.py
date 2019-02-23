#!/usr/bin/python3

# Importing all  the files and libraries needed
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

# Creates the clock variable to store the time and perform calculation later
clock = pygame.time.Clock()

# Stores the location of the map file depending on the users operating system
CurDir = os.path.dirname(os.path.realpath(__file__))
if os.name == 'nt':
    CurDir += "//Maps\\BaseMap1.txt"
else:
    CurDir += "/Maps/BaseMap1.txt"

# This initilises variables and pygame display components
pygame.init()
clock = pygame.time.Clock()
ExitBool = False
Menu = None
Fullscreen = True
ActiveFPS = False
GhostTimer = 0
Ghosts = list()
GhostLocations = list()
# This saves the native resolution of the users monitor
BaseW, BaseH = pygame.display.Info().current_w, pygame.display.Info().current_h
DisplaySize = [BaseW, BaseH]
CurrMap = LoadMap(CurDir, DisplaySize)
PreviousTime = 0
IntervalTime = 100
PastAniTime = 0
DistanceIncrease = 10

# Creates the colours and the Display
StartDisplay = pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
White = (255, 255, 255)
Blue = (0, 0, 255)
DarkBlue = (0, 0, 55)
Green = (0, 255, 0)
DarkGreen = (0, 55, 0)
Red = (255, 0, 0)
DarkRed = (55, 0, 0)
Yellow = (255, 255, 0)
Black = (0, 0, 0)


# This function loops through the map object and draws the squares stored in it
# Only run when the game board wants to be re-created
def LoadGame():
    global Player, GhostLocations
    GhostLocations = list()

    StartDisplay.fill(Black)
    for Row in range(CurrMap.GiveSize("X")):
        for Column in range(CurrMap.GiveSize("Y")):
            temp = CurrMap.GiveSquare([Row, Column]).GiveWalls()
            
            # Draws the walls of the square selected
            for wall in range(0, 4):
                # Remember that rect = [TopLeft([X,Y]), width, height]
                pygame.draw.rect(StartDisplay, Blue,
                                 (temp[wall][0][0], temp[wall][0][1],
                                  temp[wall][1][0], temp[wall][1][1]), 1)

            # Draws the score pellets of the square selected
            if CurrMap.GiveSquare([Row, Column]).GiveContents() == "S":
                pygame.draw.circle(StartDisplay, Yellow, CurrMap.
                                   GiveSquare([Row, Column]).GiveCentre(), 3)

            # Draws the upgrade pellets of the square selected
            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "U":
                pygame.draw.circle(StartDisplay, Red,
                                   CurrMap.GiveSquare([Row, Column]).
                                   GiveCentre(), 6)

            # Draws and adds the ghost spawn of the square selected to the location list
            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "G":
                pygame.draw.rect(StartDisplay, DarkRed,
                                 CurrMap.GiveSquare([Row, Column]).GiveRect())
                GhostLocations.append([Row, Column])

            # Draws the player in the square selected
            elif CurrMap.GiveSquare([Row, Column]).GiveContents() == "P":
                Player = PAC([Row, Column], CurrMap.GiveSquare([Row, Column])
                             .GiveRect()[1])
                StartDisplay.blit(Player.GiveImage(),
                                  CurrMap.GiveSquare([Row, Column])
                                  .GiveRect()[0])

    # Updates the display with the map changes when done loading
    pygame.display.update()


# When run this function loads up the game menu and its associated buttons
def LoadMenu(Mode):
    ActionList = list()
    ResActionList = list()

    # This just loads main menu buttons
    if Mode == "Escape":
        # This checks the buttons for input
        for item in EscapeButtons:
            ActionList.append(item.Check())

        # This runs all the actions wanted by the buttons
        for item in ActionList:
            if item is not None:
                item()

    # This loads main menu and resolution buttons
    elif Mode == "Resolution":
        global Menu

        # This checks the buttons for input
        for item in EscapeButtons:
            ActionList.append(item.Check())

        for item in ResolutionButtons:
            ResActionList.append(item.Check())

        # This runs all the actions wanted by the buttons
        for item in ResActionList:
            if item is not None:
                SetResolution(item)
                Menu = "Escape"

        for item in ActionList:
            if item is not None:
                item()
                Menu = "Escape"


# This function switches between wfullscreen and windowed mode
def ToggleFullscreen():
    global Fullscreen, DisplaySize
    if Fullscreen is True:
        pygame.display.set_mode(DisplaySize)

    else:
        # This is resiliency for an unsupported resolution
        try:
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0],
                  "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
            SetButtons()
            LoadMenu(Menu)

    # This switches the boolean
    Fullscreen = not Fullscreen


# This is the function for the retun button on the menu screen
# This function resets everything and completly reloads the map
# This includes resetting the ghosts and score
def Return():
    global Menu, CurrMap, GhostTimer
    CurrMap = LoadMap(CurDir, DisplaySize)
    Menu = None
    for Item in Ghosts:
        ClearScreen(Item)
        pygame.display.update()
    del Ghosts[:]
    GhostTimer = 0
    LoadGame()


# This function quits the game and pythone for the menu button
def Quit():
    pygame.quit()
    sys.exit


# This function toggles weather the game loop displays the FPS
def ToggleFPS():
    global ActiveFPS
    ActiveFPS = not ActiveFPS
    StartDisplay.fill(Black, (5, 5, 75, 25))


# This function hides the resolution buttons in the main menu
def HideSubMenu():
    StartDisplay.fill(Black, (0, 80, DisplaySize[0]/3, DisplaySize[1]-80))


# This function changes the resolutionof the application
def SetResolution(Res):
    global DisplaySize
    DisplaySize = Res

    if not Fullscreen:
        pygame.display.set_mode(DisplaySize)

    # This is resiliency for an unsupported fullscreen resolution
    else:
        try:
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)
        except:
            print("Error, display cannont support ", DisplaySize[0],
                  "x", DisplaySize[1])
            DisplaySize = [BaseW, BaseH]
            pygame.display.set_mode(DisplaySize, pygame.FULLSCREEN)

    # Reloads the menu and buttons for the new resolution
    SetButtons()
    LoadMenu(Menu)
    HideSubMenu()


# This toggles between showing the resolution buttons
def ToggleResolution():
    global Menu
    if Menu == "Resolution":
        Menu = "Escape"

    else:
        Menu = "Resolution"
    HideSubMenu()


# This clears the screen, it is used when an entity is moving as it clears the surrounding squares
def ClearScreen(obj):
    # This clears both the next square to move into
    if obj.GiveDirection() == 0:
        pygame.draw.rect(StartDisplay, Black, (CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0], (CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[1][0], (CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0][1] - CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0][1]))))

    if obj.GiveDirection() == 1:
        pygame.draw.rect(StartDisplay, Black, (CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0], ((CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0][0] - CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0][0]), CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[1][1])))

    if obj.GiveDirection() == 2:
        pygame.draw.rect(StartDisplay, Black, (CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0], (CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[1][0], (CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0][1] - CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0][1]))))

    if obj.GiveDirection() == 3:
        pygame.draw.rect(StartDisplay, Black, (CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0], ((CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[0][0] - CurrMap.GiveSquare(obj.ToCoverSquares()[1]).GiveRect()[0][0]), CurrMap.GiveSquare(obj.ToCoverSquares()[0]).GiveRect()[1][1])))

    # This clears the currently occupiued square
    for Coord in obj.ToCoverSquares():
        pygame.draw.rect(StartDisplay, Black,
                         CurrMap.GiveSquare(Coord).GiveRect())

        # if the entity is a chost it does not consume pills so they are redrawn
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


# This checks if the player is touching a ghost
def CheckTouching():
    for Item in Ghosts:
        if Player.GiveLocation() == Item.GiveLocation():
            return True, Item

    return False, None


# This animates the movement of entities
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


# This is counts the time when animating entities
def AnimateTime():
    global PastAniTime
    if round(pygame.time.get_ticks()) > PastAniTime + (IntervalTime/10):
        PastAniTime = round(pygame.time.get_ticks())
        return True

    else:
        return False


# This is run when the choose map button is selected and open the file explorer
def MapSelect():
    global Fullscreen, CurDir

    pygame.display.set_mode(DisplaySize)
    root = tk.Tk()
    root.withdraw()
    CurDir = filedialog.askopenfilename()
    Fullscreen = not Fullscreen
    ToggleFullscreen()


# This sets out all the buttons used in the program
def SetButtons():
    global EscapeButtons, ResolutionButtons
    # X, Length, Width, GapTillNext
    # This creates the size and proportions of buttons
    ButtonProperties = [(0.5*(DisplaySize[0]))-((0.3*DisplaySize[0])/2),
                        (2/3)*((DisplaySize[1]-150)/7), 0.3*DisplaySize[0],
                        (DisplaySize[1]-150)/7
                        ]

    # This creates and sets the main menu buttons
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

    # This creates the resolution buttons
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

# This is run at the start of the program to create and load the map
SetButtons()
StartDisplay.fill(Black)
LoadGame()

# This is the main game loop
while not ExitBool:
    Move = False

    # This loads animates the entities movement if the last movement finished
    if Menu is None and DistanceIncrease < 10 and round(pygame.time.get_ticks()) > (PreviousTime + ((IntervalTime/9)*DistanceIncrease)):
        ClearScreen(Player)
        for Item in Ghosts:
            ClearScreen(Item)

        for Item in Ghosts:
            Animate(Item, DistanceIncrease + 1, CurrMap)
        Animate(Player, DistanceIncrease + 1, CurrMap)
        pygame.display.update()
        DistanceIncrease += 1

    # This checks all the key presses and performs the relevent actions
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

    # This sets the next move of the ghosts
    if round(pygame.time.get_ticks()) > (PreviousTime + IntervalTime) and Menu is None:
        PreviousTime = round(pygame.time.get_ticks())
        Player.Move(CurrMap)
        for Item in Ghosts:
            Item.Move(CurrMap, Player, Ghosts)

        DistanceIncrease = 1

        # Ghost Spawn if the random timer is up and not beyond the max
        if len(Ghosts) < CurrMap.GiveMaxGhosts():
            if GhostTimer == 0:
                GhostTimer = random.randint(3, 7)
                Ghosts.append(Ghost(random.choice(GhostLocations), CurrMap
                              .GiveSquare([0, 0]).GiveRect()[1]))
                StartDisplay.blit(Ghosts[-1].GiveImage(),
                                  CurrMap.GiveSquare(Ghosts[-1].GiveLocation())
                                  .GiveRect()[0])
            GhostTimer -= 1

    # This checks if the player is touching a ghost
    Touching, Interceptor = CheckTouching()

    # This punishes the player if touched by a ghost
    if Touching is True and Player.GiveInvincible() is False:
        pygame.display.update()
        pygame.time.delay(500)
        ClearScreen(Player)

        # This clears all the ghosts
        for Item in Ghosts:
            ClearScreen(Item)
            pygame.display.update()
        del Ghosts[:]
        GhostTimer = 0

        StartDisplay.blit(Player.GiveImage(),
                          CurrMap.GiveSquare(Player.GiveLocation())
                          .GiveRect()[0])

        # This punushes the player
        if Player.TakeLife() is True:
            Menu = "Escape"
            StartDisplay.fill(Black)
            Player.Reset()

    # This gives the user a point when they kill a ghost
    if Touching is True and Player.GiveInvincible() is True:
        ClearScreen(Interceptor)
        Player.AddPoints(5)

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            ExitBool is True
            # if it is quit the game
            Quit()

    # This loads in the menu
    if Menu is not None:
        TextSurf, TextRect = TextObjects("Menu",
                                         pygame.font.Font('freesansbold.ttf',
                                                          60), Blue)
        TextRect.center = ((DisplaySize[0]/2), (35))
        StartDisplay.blit(TextSurf, TextRect)
        LoadMenu(Menu)

    # This loads in the side pannel displaying information to the user
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

    # This displays the current FPS counter
    if ActiveFPS is True:
        FPSText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = TextObjects(str(round(clock.get_fps(), 1)),
                                         FPSText, Yellow)
        TextRect.center = (40, 20)
        StartDisplay.blit(TextSurf, TextRect)

    # This checks if the player has eaten all the pills
    if Player.GivePoints() == int(CurrMap.GiveTotPoints()):
        Menu = "Escape"
        StartDisplay.fill(Black)
        Player.Reset()

    # This updates the display at a max FPS of 200
    pygame.display.update()
    clock.tick(200)
