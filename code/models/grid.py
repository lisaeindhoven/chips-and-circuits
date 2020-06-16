''''grid.py

File containing the Grid class, used to create a grid-matrix and
to place gates'''
import numpy as np

#TODO name class Grid(), or Matrix()?

class Grid():
    def __init__(self, gate_list):
        self.x_dim = 0
        self.y_dim = 0
        self.z_dim = 8
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

        # Dimensions increased by 2 to excede gate by one and adjust
        # adjust for indexing.
        self.x_dim = max(x_list) + 2
        self.y_dim = max(y_list) + 2
        return np.empty(shape=(self.x_dim, self.y_dim, self.z_dim), dtype=object)
    

    def fill_matrix(self, gate_list):
        """ Places gates from gate_list at their respective 
            location on the grid-matrix"""
        # Add every gate into the matrix
        for gate in gate_list:
            self.matrix[gate.x][gate.y][gate.z] = gate

        # Add list to every open space for possible wire.
        for index, obj in np.ndenumerate(self.matrix):
            if not obj:
                self.matrix[index] = []

    def show_matrix(self):
        """ Displays the grid-matrix filled thus far"""
        return self.matrix

    def item(self, coordinate):
        """ Returns the item in the given coordinate"""
        return self.matrix.item(coordinate)

    def add_wire(self, coordinate, net):
        """ Add a net to the grid-matrix"""
        self.matrix[coordinate].append(net)