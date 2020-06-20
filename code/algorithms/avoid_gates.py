"""
scary_gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the scary_gates class which expands 
the A* algorithm with increased costs near gates.
"""

from code.models.gates import Gate
from code.algorithms.random_algo import find_options, filter_options
from code.algorithms.manhattan import measure
from code.algorithms.a_star import A_star

import queue, math

class Avoid_gates(A_star):
    """ Class containing the A* algorithm, which is an improvement upon
        dijkstra.py due to the added heuristic. 
    """
    def __init__(self, grid, net, scary_dict):
        self.net = net
        self.begin_coordinate, self.end_coordinate = self.net.get_coordinates()
        self.grid = grid
        self.scary_dict = scary_dict

    def check_neighbour(self, neighbour, current):
        """ Takes in neighbour and current coordinate and returns 
            it's costs.
        """
        # Check if intersection or collision and adjust cost.
        cost = 1
        if (isinstance(self.grid.matrix[neighbour], list) and len(self.grid.matrix[neighbour]) >= 1):
            cost = 301

            # From gate to neighbour collision
            for neighbournet in self.grid.matrix[neighbour]:
                if (self.begin_coordinate == neighbournet.wires[-1] 
                    or self.begin_coordinate == neighbournet.wires[0]):
                    return 100000
            
                # Double intersection collision
                idx = neighbournet.wires.index(neighbour)
                if (neighbournet.wires[idx+1] == current
                    or neighbournet.wires[idx-1] == current):
                    return 100000

        # From current to gate collision
        elif isinstance(self.grid.matrix[neighbour], Gate):
            for net in self.grid.matrix[neighbour].wires:

                if (self.end_coordinate == self.grid.matrix[neighbour].wires[net][0]
                    and current == self.grid.matrix[neighbour].wires[net][1]):
                    return 100000

                elif (self.end_coordinate == self.grid.matrix[neighbour].wires[net][-1]
                    and current == self.grid.matrix[neighbour].wires[net][-2]):
                    return 100000

        # Gates are scary, set costs if neighbour is near a gate that isn't
        # from the net itsself. 
        if (neighbour in self.scary_dict and self.scary_dict[neighbour] != self.end_coordinate
            and self.scary_dict[neighbour] != self.begin_coordinate):
            return 10

        return cost 


