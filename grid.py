''''grid.py

File containing the Grid class, used to create a grid-matrix and
to place gates'''

import numpy as np
#TODO name class Grid(), or Matrix()?

class Grid():
    def __init__(self, gate_list):
        self.matrix = self.make_matrix(gate_list)
        self.fill_matrix(gate_list)


    def make_matrix(self, gate_list):
        """ Determines the dimensions of the matrix based on
            the highest x and y value of a gate's location
            and creates a matrix with these dimensions""" 
        x_list = []
        y_list = []

        for gate in gate_list:
            x_list.append(gate.x)
            y_list.append(gate.y)

        self.x_dim = max(x_list) + 1
        self.y_dim = max(y_list) + 1
        return np.empty(shape=(self.x_dim, self.y_dim), dtype=object)
    

    def fill_matrix(self, gate_list):
        """ Places gates from gate_list at their respective 
            location on the grid-matrix"""
        # Add every gate into the matrix
        for gate in gate_list:
            self.matrix[gate.x][gate.y] = gate.id

        # Add list to every open space for possible wire.
        for row in range(self.x_dim):
            for column in range(self.y_dim):
                if not self.matrix[row][column]:
                    self.matrix[row][column] = [0,0]


    def show_matrix(self):
        """ Displays the grid-matrix filled thus far"""
        return self.matrix
