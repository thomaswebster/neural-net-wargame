###GLOBAL IMPORTS
import pygame

from random import randint


###LOCAL IMPORTS
import constants
import soldier

'''
Map object to store game data

Contains an array of map tiles

Also contains a list of soldiers on the map, 
recording which side each of the soldiers is on
'''
class Map(object):
    '''
    Initialises the map object

    Currently takes only dimensions as the input to initialise an array of map tiles.
    '''
    def __init__(self, dims):

        self.dims = dims
        
        self.data = [[0]*dims[0] for i in range(dims[1])]

        #self.team1 = [Soldier()]

    '''
    Draws the map to the current gamescreen

    Only draws tiles that are in range of the camera
    in order to save cycles
    '''
    def draw(self, screen, pos, tilesize):

        for i in range(self.dims[0]):

            for j in range(self.dims[1]):

                pygame.draw.rect(screen, 
                    constants.tilecolours[self.data[i+pos[0]][j+pos[1]]], 
                    [i * tilesize, j * tilesize, 
                    tilesize, tilesize])

    '''
    Temporary function for debugging

    Seeds the map with random tiles

    For release will use simplex noise to produce more realistic terrain,
    possibly with 3 or more octaves

    this is unusable except for debugging
    '''
    def seedmap(self):

        for i in range(self.dims[0]):

            for j in range(self.dims[1]):
                
                self.data[i][j] = randint(0,2)
