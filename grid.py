''''
grid.py

File containing the Grid class, used to create a grid matrix and
to place gates.
'''

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
            x_list.append(gate.x)
            y_list.append(gate.y)

        self.x_dim = max(x_list) + 1
        self.y_dim = max(y_list) + 1

        self.grid = np.zeros(shape = (self.x_dim, self.y_dim))
    

    def set_gates(self, gate_list):
        """ Places gates from gate_list at their respective 
            location on the grid."""
        for gate in gate_list:
            self.grid[gate.x][gate.y] = 1 #Or Grid ID


    def show_grid(self):
        """ Displays the grid matrix filled thus far.""""
        print(self.grid)