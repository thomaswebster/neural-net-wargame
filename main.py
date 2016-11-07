#!/usr/bin/python3

''' Wargame made in python fought between Neural-network trained teams '''

##GLOBAL IMPORTS
import pygame

###LOCAL IMPORTS
import constants as cnst
import gamemap

###Initialise pygame
pygame.init()

###Set screensize from constants
size = cnst.cnsts["SCREENSIZE"]

###Create pygame distplay object
screen = pygame.display.set_mode(size)

###Initialise our game map
gamemap = gamemap.Map(cnst.cnsts["MAPSIZE"])

gamemap.seedmap()

###Camera position on the map
###Start at 0, 0
camera = [0, 0]

###Gameloop
while True:
    #draw gamemap
    gamemap.draw(screen, camera, cnst.cnsts["TILE"])

    #draw screen
    pygame.display.flip()
