#!/usr/bin/python3

''' Wargame made in python fought between Neural-network trained teams '''

##GLOBAL IMPORTS
import pygame

###LOCAL IMPORTS
import constants as cnst
import gamemap

pygame.init()

size = cnst.cnsts["SCREENSIZE"]
screen = pygame.display.set_mode(size)

gamemap = gamemap.Map()

while True:
    screen.fill((0,0,0))
    pygame.display.flip()
