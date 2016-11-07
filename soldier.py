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
        """
        Initialise the brain of this soldier;
        the brain definition is a constant defined in constants.py
        """
        self.brain = ANN(constants.soldier_brain, Neuron.Sigmoid)

        """
        Initialise the position property of the soldier
        This consists of an x and y coordinate in the map grid system
        """
        self.pos = [x, y]

    def think(self, squares):
        """ 
        This is called on the instance by the map.
        The current data is input to the soldier's brain, and an analogue output
        is produced.
        The output tells the soldier where to move.
        """

        """ call the brain's run method (see the ANN class) """
        output = self.brain.run(squares)

        """
        Decide what to do with the output
        The output is an analogue value between 0 and 1

        We take anything close to 0 to mean "don't move",
        while 0.25, 0.5, 0.75 and 1 respectively indicate moving left, up, right or down
        """

        """
        If the output is within `tolerance` of a particular value, decide to take that option
        Notice tolerance should be less than half the minimum distance between determining values

        Here, 0.1 < 0.5 * 0.25 so we're gucci.
        """
        tolerance = 0.1

        """ values of the output defining behaviour """
        move_none   = 0
        move_left   = 0.25
        move_up     = 0.5
        move_right  = 0.75
        move_down   = 1

        """ decide where to move the soldier """
        if abs(output - move_none) < tolerance:
            """ don't move """
            pass
        elif abs(output - move_left) < tolerance:
            """ move left """
            self.move(-1, 0)
        elif abs(output - move_up) < tolerance:
            """ move up """
            self.move(0, -1)
        elif abs(output - move_right) < tolerance:
            """ move right """
            self.move(1, 0)
        elif abs(output - move_down) < tolerance:
            """ move down """
            self.move(0, 1)


    def move(self, dx, dy):
        """
        Move this solder on the map
        Notice that the actual updating of the map grid is done in gamemap.py
        """
        self.x += dx
        self.y += dy


