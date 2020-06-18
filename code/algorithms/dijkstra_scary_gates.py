"""
dijkstra_scary_gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the dijkstra_scary_gates class which searches
for the shortest path from gate to gate with a heuristic that 
increases the cost for neighbours near gates that are not the net's.
"""
from code.models.gates import Gate
from code.algorithms.random_algo import find_options, filter_options
from code.algorithms.manhattan import measure
from code.algorithms.dijkstra import Dijkstra
from code.helpers import scary_gates
import queue, math

class Dijkstra_scary_gates(Dijkstra):
    """ Class containing dijkstra's shortes path algorithm with a heuristic
        that increases the cost for neighbours near gates that are not the net's.
    """
    def __init__(self, grid, net, scary_dict):
        self.net = net
        self.begin_coordinate, self.end_coordinate = self.net.get_coordinates()
        self.grid = grid
        self.scary_dict = scary_dict

    def expand_frontier(self):
        """ Picks and removes a location from the frontier and expands it by looking at
            it's neighbours. Any neighbours not visited will be added to the frontier.
        """
        frontier = queue.PriorityQueue()
        frontier.put(self.begin_coordinate, 0)
        self.archive = {}
        self.archive[self.begin_coordinate] = None
        current_cost = {}
        current_cost[self.begin_coordinate] = 0

        # Pick neighbour from the frontier and expand it by adding its
        # own neighbours to the frontier.
        while not frontier.empty():
            current = frontier.get()

            # Stop expanding frontier when end-coordinate is reached.
            if current is self.end_coordinate:
                break

            # Don't allow a path to go through a gate.
            if (isinstance(self.grid.matrix[current], Gate) and current != self.begin_coordinate
                and current != self.end_coordinate):
                continue
            
            options = filter_options(find_options(current), self.grid)
            for neighbour in options:

                # Determine move's cost.
                cost = self.check_neighbour(neighbour, current, self.scary_dict)
                new_cost = current_cost[current] + cost 

                # Create archive shortest routes.
                if (neighbour not in current_cost or new_cost < current_cost[neighbour]):
                    current_cost[neighbour] = new_cost
                    priority = new_cost
                    frontier.put(neighbour, priority)
                    self.archive[neighbour] = current

    def check_neighbour(self, neighbour, current, scary_dict):
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