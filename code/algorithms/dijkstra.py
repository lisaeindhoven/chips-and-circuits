"""
dijkstra.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the dijkstra class which uses heuristics to be awesome.
"""

from code.models.gates import Gate
from code.algorithms.random_algo import *
from code.algorithms.manhattan import measure
import queue 

class Dijkstra():
    """ Class containing dijkstra's shortes path algorithm, which is improved upon using
        the A* pathfinder.
    """
    def __init__(self, grid, net):
        self.net = net
        self.begin_coordinate, self.end_coordinate = self.net.get_coordinates()
        self.frontier = queue.PriorityQueue()
        self.archive = {}
        self.grid = grid

    def expand_frontier(self):
        """ Picks and removes a location from the frontier and expands it by looking at
            it's neighbours. Any neighbours no visited will be added to the frontier.
        """
        self.frontier.put(self.begin_coordinate, 0)
        self.archive[self.begin_coordinate] = None
        self.current_cost = {}
        self.current_cost[self.begin_coordinate] = 0

        # Pick neighbour from the frontier and expand it by adding its
        # own neighbours to the frontier.
        while not self.frontier.empty():
            current = self.frontier.get()

            # Stop expanding frontier when end-coordinate is reached.
            if current is self.end_coordinate:
                break

            # Don't allow a path to go through a gate.
            if (isinstance(self.grid.matrix[current], Gate) and current != self.begin_coordinate):
                continue
            
            #print(self.grid.x_dim)
            options = filter_options(find_options(current), self.grid)
            for neighbour in options:
             #   print(neighbour)

                # Code was here again
                cost = self.check_neighbour(neighbour, current)
                if cost:
                    new_cost = self.current_cost[current] + cost 

                    if (neighbour not in self.archive or new_cost < self.current_cost[neighbour]):
                        self.current_cost[neighbour] = new_cost
                        priority = new_cost + measure(current, neighbour)
                        self.frontier.put(neighbour, priority)
                        self.archive[neighbour] = current


    def make_path(self):
        """ Follow the archive of neighbours from end to start
        """
        # Start at the goal and reverse to start position.
        current = self.end_coordinate
        self.path = []

        # Reconstruct the path by checking where the current point came 
        # from.
        while current != self.begin_coordinate:
            self.path.append(current)
            current = self.archive[current]
        self.path.append(self.begin_coordinate)
        self.path.reverse()

        # Add the wire path to the net. 
        self.net.wires = self.path
        self.net.completed = True
        
        # Place the nets along the path in the grid.
        self.intersection_count = 0
        for coordinate in self.path[1:-1]:
            self.grid.matrix[coordinate].append(self.net)

            # Keep track of the intersections
            if len(self.grid.matrix[coordinate]) > 1:
                self.intersection_count += 1
     
        return self.path

    def check_neighbour(self, neighbour, current):
        """ Head
        """
        # Check if intersection and adjust cost.
        cost = 1
        if (isinstance(self.grid.matrix[neighbour], list) and len(self.grid.matrix[neighbour]) == 1):
            cost = 301

            if (self.end_coordinate in self.grid.matrix[neighbour][0].wires):
                return False
        
        #TODO collisions not near gate

        return cost