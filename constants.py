'''Dictionaries of the project's constants, to allow for iteration over'''


#general constants for the project
param = {
    "SCREENSIZE": [320,320],
    "TILE": 16,
    "MAPSIZE": [20,20],
    "TEAM1": 6,
    "TEAM2": 6
}

#0 = GRASS, 1 = WATER, 2 = SAND, 3 = LAVA, 4 = COVER
tilecolours = {0:(0,200,0), 
    1:(0,0,255), 
    2:(200,180,200),
    3:(255,0,0), 
    4:(255,255,255)
}

soldier_brain = [120, 10, 1]