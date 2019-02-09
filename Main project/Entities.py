import os
import random

import pygame


class Ghost:

    def __init__(self, GivenLocation, SqSize):
        self.Direction = 0
        self.Location = GivenLocation
        self.Previous = GivenLocation
        self.ID = random.randint(0, 9)

        if os.name == 'nt':
            Fname = "\\Ghost" + str(self.ID) + ".png"
            OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "\\Assets" + Fname)
        else:
            Fname = "/Ghost" + str(self.ID) + ".png"
            OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Assets" + Fname)

        self.Image = pygame.transform.scale(OriginalImage, (int(SqSize[0]),
                                                            int(SqSize[1])))

    def Move(self, Map, Player, Ghosts):
        Rating = list()
        GhostLocation = list()

        for Item in Ghosts:
            GhostLocation.append(Item.GiveLocation())

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

        self.Previous = self.Location
        if max(Rating) >= 0:
            rannum = random.randint(0, 3)
            while Rating[rannum] != max(Rating):
                rannum = random.randint(0, 3)

            self.Direction = rannum
            self.Location, Sq = Map.FindNeighbour(self, rannum)

    def ToCoverSquares(self):
        return self.Location, self.Previous

    def GiveLocation(self):
        return self.Location

    def GivePrev(self):
        return self.Previous

    def GiveImage(self):
        return self.Image

    def GiveDirection(self):
        return self.Direction

    def CheckMovement(self):
        if self.Location == self.Previous:
            return False
        else:
            return True


class PAC:

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

        for loop in range(4):
            if os.name == 'nt':
                OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "\\Assets\\" +
                                                  "Pacman" + str(loop) + ".png"
                                                  )
            else:
                OriginalImage = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Assets/Pacman"
                                                  + str(loop) + ".png")
            self.ImageList.append(pygame.transform.scale(OriginalImage,
                                                         (int(SqSize[0]),
                                                          int(SqSize[1]))))

    def ChangeDirection(self, _Direction):
        self.Direction = _Direction
        self.Image = self.ImageList[self.Direction]

    def GiveDirection(self):
        return self.Direction

    def AddPoints(self, _Value):
        self.Points + _Value

    def GivePoints(self):
        return self.Points

    def GiveLives(self):
        return self.Lives

    def CheckMovement(self):
        if self.Location == self.Previous:
            return False
        else:
            return True

    def GiveImage(self):
        return self.Image

    def GiveLocation(self):
        return self.Location

    def GivePrev(self):
        return self.Previous

    def ToCoverSquares(self):
        return self.Location, self.Previous

    def GiveInvincible(self):
        return self.Invincible
    
    def InvincibleTime(self):
        seconds = (pygame.time.get_ticks()-self.InvinTime) / 1000
        seconds = 10 - seconds
        if seconds <= 0:
            self.Invincible = False
        return round(seconds)

    def TakeLife(self):
        self.Image = self.ImageList[1]
        self.Location = self.Start
        self.Direction = 1
        self.Lives -= 1
        if self.Lives < 0:
            return True
        return False

    def Reset(self):
        self.Direction = 1
        self.Image = self.ImageList[1]
        self.Points = 0
        self.Lives = 3
        self.Location = self.Start

    def Move(self, Map):
        self.Previous = self.Location
        Location, SetSquare = Map.FindNeighbour(self, self.Direction)

        # Checks for walls in current square direction
        if Map.GiveSquare(self.Location).GiveWalls()[self.Direction][0] == [0, 0] and SetSquare.GiveContents() != "G":
            # Finds square you wish to travel to
            self.Location = Location

            if SetSquare.GiveContents() == "S":
                self.Points += 1

            elif SetSquare.GiveContents() == "U":
                self.InvinTime = pygame.time.get_ticks()
                self.Invincible = True

        SetSquare.ClearContents()
