"""
dijkstra_skyscraper.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the dijkstra_skyscrapper class which searches
for the shortest path from gate to gate with a heuristic that 
prefers paths to travel upwards.
"""
from code.models.gates import Gate
from code.algorithms.random_algo import find_options, filter_options
from code.algorithms.manhattan import measure
from code.algorithms.a_star import A_star
import queue, math

class Skyscraper(A_star):
    """ Class containing dijkstra's shortes path algorithm with a heuristic
        that decreases the cost for neighbours that travel upwards.
    """
    def check_neighbour(self, neighbour, current):
        """ Takes in neighbour and current coordinate and returns 
            it's costs.
        """
        # Check if intersection or collision and adjust cost
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

        # Costs for upward movements are decreased.
        if neighbour[2] > current[2]:
            cost = 0

        return cost 
        