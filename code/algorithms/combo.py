from code.models.gates import Gate
from code.algorithms.avoid_gates import Avoid_gates

class Combo(Avoid_gates):
    """ relaxes soft intersection constraint (for initial run) """
    def check_neighbour(self, neighbour, current):
        """ Takes in neighbour and current coordinate and returns 
            it's costs.
        """
        # Check if intersection or collision and adjust cost
        cost = 1
        if (isinstance(self.grid.matrix[neighbour], list) and len(self.grid.matrix[neighbour]) >= 1):
            cost = 150 # set intersection tax here

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

        # scary gates addition 
        if (neighbour in self.scary_dict and self.scary_dict[neighbour] != self.end_coordinate
            and self.scary_dict[neighbour] != self.begin_coordinate):
            return 20 # set gate tax here
        
        # Costs for upward movements are decreased.
        if neighbour[2] > current[2]:
            cost = 0 # set upward value here

        return cost 