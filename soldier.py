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

    def __init__(self):
        """
        Initialise the brain of this soldier;
        the brain definition is a constant defined in constants.py
        """
        self.brain = ANN(constants.soldier_brain, Neuron.Sigmoid)

    def input(self, squares):
        """
        This is called on the instance by the map.
        The current data is input to the soldier's brain, and an analogue output
        is produced.
        The output tells the soldier where to move.
        """

        """ call the brain's run method (see the ANN class) """
        output = self.brain.run(squares)

        """
        decide what to do with the output
        """
