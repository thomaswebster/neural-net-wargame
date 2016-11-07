'''Dictionaries of the project's constants, to allow for iteration over'''

# error messages
E_OUT_OF_BOUNDS = "Camera out of bounds!"

#general constants for the project
param = {
    "SCREENSIZE": [320,320],
    "TILE": 16,
    "MAPSIZE": [40,40],
    "TEAM1": 6,
    "TEAM2": 6
}

# define tile types as integers
TILE_GRASS      = 0
TILE_WATER      = 1
TILE_SAND       = 2
TILE_LAVA       = 3
TILE_COVER      = 4
TILE_SOLDIER    = 5

# define tile type colours as rgb value tuples
tilecolours = {
    TILE_GRASS: (0, 200, 0), # green
    TILE_WATER: (0, 0, 255), # blue
    TILE_SAND:  (200, 180, 200),
    TILE_LAVA:  (255, 0, 0),
    TILE_COVER: (255, 255, 255),
}

soldier_brain = [120, 10, 1]

