"""
a_star.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the A* class which uses heuristics to be more awesome
than the dijkstra shortest path algorithm.
"""

from code.models.gates import Gate
from code.algorithms.random_algo import find_options, filter_options
from code.algorithms.manhattan import measure
import queue, math

class A_star():
    """ Class containing the A* algorithm, which is an improvement upon
        dijkstra.py due to the added heuristic. 

        costs_tup = (normal_cost, intersection_cost, collision_cost, gate_cost, sky_cost)
    """
    def __init__(self, grid, net, scary_dict, costs_tup=(1,300,100000,0,0)):
        self.net = net
        self.begin_coordinate, self.end_coordinate = self.net.get_coordinates()
        self.grid = grid
        self.scary_dict = scary_dict

        # Set costs
        if not isinstance(costs_tup, tuple):
            raise TypeError("Costs must be given as tuple")
        self.costs_tup = costs_tup

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
        # own neighbours to the frontier
        while not frontier.empty():
            current = frontier.get()

            # Stop expanding frontier when end-coordinate is reached
            if current is self.end_coordinate:
                break

            # Don't allow a path to go through a gate
            if (isinstance(self.grid.matrix[current], Gate) and current != self.begin_coordinate
                and current != self.end_coordinate):
                continue
            
            options = filter_options(find_options(current), self.grid)
            for neighbour in options:

                # Determine move's cost
                cost = self.check_neighbour(neighbour, current)
                new_cost = current_cost[current] + cost 

                # Create archive of shortest routes
                if (neighbour not in current_cost or new_cost < current_cost[neighbour]):
                    current_cost[neighbour] = new_cost
                    priority = new_cost + measure(neighbour, self.end_coordinate)
                    frontier.put(neighbour, priority)
                    self.archive[neighbour] = current

    def make_path(self):
        """ Follow the archive of neighbours from end to start.
        """
        # Start at the goal and reverse to start position
        current = self.end_coordinate
        path = []

        # Reconstruct the path by checking where the current point came
        # from.
        while current != self.begin_coordinate:
            path.append(current)
            current = self.archive[current]
        path.append(self.begin_coordinate)
        path.reverse()

        # Add the wire path to the net
        self.net.wires = path
        self.net.completed = True
        
        # Place the nets along the path in the grid
        self.intersection_count = 0
        for coordinate in path[1:-1]:
            self.grid.matrix[coordinate].append(self.net)

        # Add the wirepath to the gate object.
        self.grid.matrix[self.begin_coordinate].wires[self.net.id] = path
        self.grid.matrix[self.end_coordinate].wires[self.net.id] = path

    def check_neighbour(self, neighbour, current):
        """ Takes in neighbour and current coordinate and returns 
            it's costs.
        """
        normal_cost, intersection_cost, collision_cost, gate_cost, sky_cost = self.costs_tup
        # Check if intersection or collision and adjust cost
        cost = normal_cost
        if (isinstance(self.grid.matrix[neighbour], list) and len(self.grid.matrix[neighbour]) >= 1):
            cost += intersection_cost

            # From gate to neighbour collision
            for neighbournet in self.grid.matrix[neighbour]:
                if (self.begin_coordinate == neighbournet.wires[-1] 
                    or self.begin_coordinate == neighbournet.wires[0]):
                    return collision_cost
            
                # Double intersection collision
                idx = neighbournet.wires.index(neighbour)
                if (neighbournet.wires[idx+1] == current
                    or neighbournet.wires[idx-1] == current):
                    return collision_cost

        # From current to gate collision
        elif isinstance(self.grid.matrix[neighbour], Gate):
            for net in self.grid.matrix[neighbour].wires:
                
                if (self.end_coordinate == self.grid.matrix[neighbour].wires[net][0]
                    and current == self.grid.matrix[neighbour].wires[net][1]):
                    return collision_cost

                elif (self.end_coordinate == self.grid.matrix[neighbour].wires[net][-1]
                    and current == self.grid.matrix[neighbour].wires[net][-2]):
                    return collision_cost

        # Gates are scary, set costs if neighbour is near a gate that isn't
        # from the net itsself. 
        if (neighbour in self.scary_dict and self.scary_dict[neighbour] != self.end_coordinate
            and self.scary_dict[neighbour] != self.begin_coordinate):
            cost += gate_cost

        # Costs for upward movements are decreased.
        if neighbour[2] > current[2]:
            cost += sky_cost

        return cost 

    def search(self):
        ''' Expands the frontier, determines shortest path and returns the 
            path that was laid.
        '''
        self.expand_frontier()
        return self.make_path()