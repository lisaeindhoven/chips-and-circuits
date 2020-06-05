# Initiate Grid

import numpy as np

class Grid():
    def __init__(self, gate_list):
        self.gate_list = gate_list

    def make_matrix(self, gate_list):
        """ Determines the dimension of the grid based on
            the highest x and y value of a gate's location
            and creates a matrix with these dimensions.""" 
        x_list = []
        y_list = []

        for gate in gate_list:
            x_list.append(int(gate.x))
            y_list.append(int(gate.y))

        self.x_dim = max(x_list) + 1
        self.y_dim = max(y_list) + 1

        return np.zeros(shape = (self.x_dim, self.y_dim))