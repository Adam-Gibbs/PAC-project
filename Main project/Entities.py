# Importing all  the files and libraries needed
import os
import random

import pygame


class Ghost:

    # Run when a new ghost is created, needs the location of its spawn and its size
    def __init__(self, GivenLocation, SqSize):
        self.Direction = 0
        self.Location = GivenLocation
        self.Previous = GivenLocation
        # Selects a random number for the ghost's colour
        self.ID = random.randint(0, 9)

        # Gets the image, the file structure depends on the OS
        if os.name == 'nt':
            Fname = "\\Ghost" + str(self.ID) + ".png"
            OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "\\Assets" + Fname)
        else:
            Fname = "/Ghost" + str(self.ID) + ".png"
            OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Assets" + Fname)

        # Scales the image to the size of the square
        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))

    # This decides on the best direction for the ghost
    def Move(self, Map, Player, Ghosts):
        Rating = list()
        GhostLocation = list()

        # Finds the location of all other ghosts
        for Item in Ghosts:
            GhostLocation.append(Item.GiveLocation())

        # Loops through all posible destinations and gives it a score
        for Direction in range(4):
            TempRating = list()
            Pos, Square = Map.FindNeighbour(self, Direction)

            if Map.GiveSquare(self.Location).GiveWalls()[Direction][0] != [0,
                                                                           0]:
                TempRating.append(-2)

            if Pos in GhostLocation:
                TempRating.append(-1)
            if self.Previous == Pos:
                TempRating.append(0)
            if Square.GiveContents() == "G":
                TempRating.append(1)
            if Square.GiveContents() == "E":
                TempRating.append(2)
            if Player.GiveLocation() == Pos:
                TempRating.append(4)

            if len(TempRating) == 0:
                Rating.append(3)
            elif -1 in TempRating or -2 in TempRating:
                Rating.append(-1)
            else:
                Rating.append(max(TempRating))

        # Selects the highest scoring direction, if more than one randomly selects one
        self.Previous = self.Location
        if max(Rating) >= 0:
            rannum = random.randint(0, 3)
            while Rating[rannum] != max(Rating):
                rannum = random.randint(0, 3)

            self.Direction = rannum
            self.Location, Sq = Map.FindNeighbour(self, rannum)

    # Returns the square it currently ocupies and the one it is moving into
    def ToCoverSquares(self):
        return self.Location, self.Previous

    # Returns the current location
    def GiveLocation(self):
        return self.Location

    # Returns the location it moved from
    def GivePrev(self):
        return self.Previous

    # Returns the current image
    def GiveImage(self):
        return self.Image

    # Returns the current direction of travel
    def GiveDirection(self):
        return self.Direction

    # Returns if the ghost is moving
    def CheckMovement(self):
        if self.Location == self.Previous:
            return False
        else:
            return True


class PAC:

    # Run when a new player is created, needs the location of its spawn and its size
    def __init__(self, GivenLocation, SqSize):
        self.Location = GivenLocation  # map struct location [x,y]
        self.Previous = GivenLocation
        self.Start = GivenLocation
        self.Direction = 1
        self.SetImages(SqSize)
        self.Image = self.ImageList[1]
        self.Points = 0
        self.Lives = 3
        self.Invincible = False

    def SetImages(self, SqSize):
        self.ImageList = list()

        # Gets the images, the file structure depends on the OS
        for loop in range(4):
            if os.name == 'nt':
                OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "\\Assets\\" +
                                                  "Pacman" + str(loop) + ".png"
                                                  )
            else:
                OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Assets/Pacman"
                                                  + str(loop) + ".png")

            # Scales the image to the size of the square and appends it to a list
            self.ImageList.append(pygame.transform.scale(OriginalImage,
                                                         (int(SqSize[0]),
                                                          int(SqSize[1]))))

    # Sets the current direction and alters the image
    def ChangeDirection(self, _Direction):
        self.Direction = _Direction
        self.Image = self.ImageList[self.Direction]

    # Gives the current directio of travel
    def GiveDirection(self):
        return self.Direction

    # Adds score to the player
    def AddPoints(self, _Value):
        self.Points + _Value

    # Returns the current ammount of points
    def GivePoints(self):
        return self.Points

    # Returns the ammount of lives left
    def GiveLives(self):
        return self.Lives

    # Checks that the player has moved
    def CheckMovement(self):
        if self.Location == self.Previous:
            return False
        else:
            return True

    # Returns the current image
    def GiveImage(self):
        return self.Image

    # Returns the current location of the player
    def GiveLocation(self):
        return self.Location

    # Returns the location they have moved from
    def GivePrev(self):
        return self.Previous

    # Returns the square they currently ocupies and the one they are moving into
    def ToCoverSquares(self):
        return self.Location, self.Previous

    # Returns weather or not the player is currently invincible
    def GiveInvincible(self):
        return self.Invincible

    # Timer to reset invincibliity
    def InvincibleTime(self):
        seconds = (pygame.time.get_ticks()-self.InvinTime) / 1000
        seconds = 10 - seconds
        if seconds <= 0:
            self.Invincible = False
        return round(seconds)

    # Resets the current player location and reduces the ammount of lives
    def TakeLife(self):
        self.Image = self.ImageList[1]
        self.Location = self.Start
        self.Direction = 1
        self.Lives -= 1
        # This checks there are lives left
        if self.Lives < 0:
            return True
        return False

    # This resets the player and score
    def Reset(self):
        self.Direction = 1
        self.Image = self.ImageList[1]
        self.Points = 0
        self.Lives = 3
        self.Location = self.Start

    # This finds the next square to move into and if it can
    def Move(self, Map):
        self.Previous = self.Location
        Location, SetSquare = Map.FindNeighbour(self, self.Direction)

        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction][0] == [0, 0] and SetSquare.GiveContents() != "G":
            # Finds square you wish to travel to
            self.Location = Location

            # Adds a pint if it collects a point pill
            if SetSquare.GiveContents() == "S":
                self.Points += 1

            # This makes it invincible if it collects an upgrade pill
            elif SetSquare.GiveContents() == "U":
                self.InvinTime = pygame.time.get_ticks()
                self.Invincible = True

        # Clears the contents of the square
        SetSquare.ClearContents()
