"""
dijkstra.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file contains the dijkstra class which searches for the shortest
path from gate to gate by exploring all the options
and tracking back to the start upon arriving at its goal.
"""
import queue, math
from code.models.gates import Gate
from code.algorithms.a_star import A_star
from code.helpers import find_options, filter_options

class Dijkstra(A_star):
    """ Class containing dijkstra's shortes path algorithm which 
        searches for the shortest path from gate to gate.
    """
    def expand_frontier(self):
        """ Picks and removes a location from the frontier and expands it by looking at
            it's neighbours. Any neighbours not visited will be added to the frontier.
        """
        frontier = queue.PriorityQueue()
        frontier.put(self.begin_coordinate, 0)
        self.archive = {}
        self.archive[self.begin_coordinate] = None
        self.current_cost = {}
        self.current_cost[self.begin_coordinate] = 0

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
                new_cost = self.current_cost[current] + cost 

                # Create archive shortest routes
                if (neighbour not in self.current_cost or new_cost < self.current_cost[neighbour]):
                    self.current_cost[neighbour] = new_cost
                    priority = new_cost
                    frontier.put(neighbour, priority)
                    self.archive[neighbour] = current
    