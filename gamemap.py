###GLOBAL IMPORTS
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

        self.dims = dims

        #self.team1 = [Soldier()]

        self.data = [[0]*dims[0] for i in range(dims[1])]

    def draw(self, screen, pos, tilesize):

        for i in range(self.dims[0]):

            for j in range(self.dims[1]):

                pygame.draw.rect(screen,
                    C.tilecolours[self.data[i+pos[0]][j+pos[1]]],
                    [i * tilesize, j * tilesize,
                    tilesize, tilesize])

    def seedmap(self):
        """ seeds the map with random values from either grass, water or sand """
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                rand = random()

                self.data[i][j] = C.TILE_GRASS if rand < 0.3333 else (\
                        C.TILE_WATER if rand < 0.66666 else C.TILE_SAND)

