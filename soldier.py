from ann import ANN, Neuron

import constants

class Soldier(object):
    """
    Class to hold the data for a soldier object.
    Each soldier has a "brain", which is a Sigmoid neural network with 120 inputs.

    The inputs represent squares in an 11x11 grid around the soldier's current position.
    Each square in the grid has an integer value representing the current status of that square.

    For example, if the value for "soldier" was 1, and there was another soldier at (4, 5) relative to this
    soldier, that input would have value 1. Other values may represent grass, water etc.
    """

    def __init__(self, x, y):
        self.brain = ANN(constants.soldier_brain, Neuron.Sigmoid)

        self.pos = [x, y]

    def think(self, squares):
        
        output = self.brain.run(squares)

        """ tolerance must be less than the minimum difference between defining values below """
        tolerance = 0.1

        """ values of the output defining behaviour """
        move_none   = 0
        move_left   = 0.25
        move_up     = 0.5
        move_right  = 0.75
        move_down   = 1

        """ decide where to move the soldier """
        if abs(output - move_none) < tolerance:
            pass
        elif abs(output - move_left) < tolerance:
            self.move(-1, 0)
        elif abs(output - move_up) < tolerance:
            self.move(0, -1)
        elif abs(output - move_right) < tolerance:
            self.move(1, 0)
        elif abs(output - move_down) < tolerance:
            self.move(0, 1)


    def move(self, dx, dy):
        """
        Move this solder on the map
        The actual updating of the map grid is done in gamemap.py
        """
        self.x += dx
        self.y += dy


