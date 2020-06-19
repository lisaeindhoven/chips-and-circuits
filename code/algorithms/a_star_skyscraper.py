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
from code.algorithms.dijkstra import Dijkstra
import queue, math

class A_star_skyscraper(Dijkstra_skyscraper):
    """ Class containing dijkstra's shortes path algorithm with a heuristic
        that decreases the cost for neighbours that travel upwards.
    """
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
                cost = self.check_neighbour(neighbour, current)
                new_cost = current_cost[current] + cost 

                # Create archive shortest routes.
                if (neighbour not in current_cost or new_cost < current_cost[neighbour]):
                    current_cost[neighbour] = new_cost
                    priority = new_cost + measure(neighbour, self.end_coordinate)
                    frontier.put(neighbour, priority)
                    self.archive[neighbour] = current