"""
dijkstra.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the dijkstra class which uses heuristics to be awesome.
"""

from .random_algo import *
import queue 

class Dijkstra():
    def __init__(self, grid, net):
        self.begin_coordinate, self.end_coordinate = net.get_coordinates()
        self.frontier = queue.Queue()
        self.archive = {}
        self.grid = grid

    def make_path(self):
        """ Use Dijkstra's shortest path algorithm to determine the
            shortest path between the two point of a net.
        """
        self.frontier.put(self.begin_coordinate)
        self.archive[self.begin_coordinate] = None

        # Pick neighbour from the frontier and expand it by adding its
        # own neighbours to the frontier.
        while not self.frontier.empty():
            current = self.frontier.get()
            options = filter_options(find_options(current), self.grid)

            for neighbour in iter(options):
                if neighbour not in self.archive:
                    self.frontier.put(neighbour)
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

        # Lay wire on the grid
        

        return self.path

