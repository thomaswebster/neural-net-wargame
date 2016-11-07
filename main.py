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
size = cnst.param["SCREENSIZE"]

###Create pygame distplay object
screen = pygame.display.set_mode(size)

###Initialise our game map
gamemap = gamemap.Map(cnst.param["MAPSIZE"])

#for debugging, seeds random values
gamemap.seedmap()

###Camera position on the map
###Start at 0, 0
camera = [0, 0]

###Gameloop
while True:
    #get pygame events (input)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                camera[0] -= 1
            if event.key == pygame.K_RIGHT:
                camera[0] += 1
            if event.key == pygame.K_UP:
                camera[1] -= 1
            if event.key == pygame.K_DOWN:
                camera[1] += 1


    #draw gamemap
    gamemap.draw(screen, camera, cnst.param["TILE"])



    #draw screen
    pygame.display.flip()
