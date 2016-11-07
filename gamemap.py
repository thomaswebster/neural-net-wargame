###GLOBAL IMPORTS
import pdb
import pygame

from random import random

###LOCAL IMPORTS
import constants as C
import soldier

'''
Map object to store game data

Contains an array of map tiles

Also contains a list of soldiers on the map,
recording which side each of the soldiers is on
'''
class Map(object):
    def __init__(self, dims):

        self.dims = dims # size of the map

        #self.team1 = [Soldier()]

        self.data = [[0]*dims[1] for i in range(dims[0])]

    def draw(self, screen, camera, tilesize):
        """ draws the state of the map on the screen, at the current camera position """

        """ the bounds of what can fit on the screen """
        bounds = [C.param["SCREENSIZE"][i] // tilesize for i in range(2)]

        """ make sure the camera isn't out of bounds """
        for i in range(2):
            camera[i] = min(self.dims[i] - bounds[i], max(0, camera[i]))

        for i in range(camera[0], camera[0] + bounds[0]):
            if i > self.dims[0] - 1:
                raise Exception(C.E_OUT_OF_BOUNDS)

            for j in range(camera[1], camera[1] + bounds[1]):
                if j > self.dims[1] - 1:
                    raise Exception(C.E_OUT_OF_BOUNDS)

                pygame.draw.rect(screen,
                    C.tilecolours[self.data[i][j]],
                    [(i - camera[0]) * tilesize, (j - camera[1]) * tilesize,
                        tilesize, tilesize])

    def seedmap(self):
        """ seeds the map with random values from either grass, water or sand """
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                rand = random()

                self.data[i][j] = C.TILE_GRASS if rand < 0.3333 else (\
                        C.TILE_WATER if rand < 0.66666 else C.TILE_SAND)

