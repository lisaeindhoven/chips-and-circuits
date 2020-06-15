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
    def __init__(self, grid, net):
        self.net = net
        self.begin_coordinate, self.end_coordinate = self.net.get_coordinates()
        self.frontier = queue.PriorityQueue()
        self.archive = {}
        self.grid = grid

    def make_path(self):
        """ Use Dijkstra's shortest path algorithm to determine the
            shortest path between the two point of a net.
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

            options = filter_options(find_options(current), self.grid)
            for neighbour in options:

                # Check if intersection and adjust cost.
                cost = 1
                if isinstance(self.grid.matrix[neighbour], list):
                    if len(self.grid.matrix[neighbour]) > 0:
                        cost = 301

                        # Collision #TODO Collisions are still allowed when neighbour is gate
                        # LISA TIP if intersection, if end_coord in wirelist do not go there.
                        if isinstance(self.grid.matrix[current], list):
                            for net in self.grid.matrix[neighbour]:
                                if net in self.grid.matrix[current]:
                                    continue

                new_cost = self.current_cost[current] + cost 

                if (neighbour not in self.archive or new_cost < self.current_cost[neighbour]):
                    self.current_cost[neighbour] = new_cost
                    priority = new_cost + measure(current, neighbour)
                    self.frontier.put(neighbour, priority)
                    self.archive[neighbour] = current

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
        intersection_count = 0
        #print(self.path)
        for coordinate in self.path[1:-1]:
            #print(coordinate, self.grid.matrix[coordinate])
            self.grid.matrix[coordinate].append(self.net)

            # Intersections
            if len(self.grid.matrix[coordinate]) > 1:
                intersection_count += 1
     
        return self.path