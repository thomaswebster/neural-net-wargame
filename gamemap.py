###GLOBAL IMPORTS
import pygame

from random import randint


###LOCAL IMPORTS
import constants

'''
Map object to store game data

Contains an array of map tiles

Also contains a list of soldiers on the map,
recording which side each of the soldiers is on
'''
class Map(object):
    def __init__(self, dims):

        self.dims = dims

        self.data = [[0]*dims[0] for i in range(dims[1])]

    def draw(self, screen, pos, tilesize):

        for i in range(self.dims[0]):

            for j in range(self.dims[1]):

                pygame.draw.rect(screen,
                    constants.tilecolours[self.data[i][j]],
                    [i * tilesize, j * tilesize,
                    tilesize, tilesize])

    def seedmap(self):

        for i in range(self.dims[0]):

            for j in range(self.dims[1]):

                self.data[i][j] = randint(0,2)
