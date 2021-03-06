"""
select_net.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file contains functions to get nets in different orders.
"""
import random as rnd
from code.helpers import filter_options, find_options
from code.algorithms.manhattan import min_nets, max_nets

def get_random_nets(nets):
    """ Returns a list of net ids in random order from the not 
        completed nets.
    """
    random_net_ids = []
    for net in nets:
        random_net_ids.append(net.id - 1)
    rnd.shuffle(random_net_ids)
    return random_net_ids

def get_min_freedom_net(gates, grid):
    """ Returns the net id for the algorithm based on freedom 
        around the gate and the uncompleted nets from the gate.
    """
    count_freedom_and_uncompleted = []

    # Go through every gate to find the information needed
    for gate in gates:
        count_freedom_and_uncompleted.append([0, 0])
        completed = True
        # Count uncompleted nets
        for net in gate.nets:
            if net.completed == False:
                completed = False
                count_freedom_and_uncompleted[gate.id - 1][1] += 1
        
        # Count the freedom around the gate
        if not completed:
            coordinates = gate.coordinate()
            options = filter_options(find_options(coordinates), grid)
            for option in options:
                if grid.item(option) == []:
                    count_freedom_and_uncompleted[gate.id - 1][0] += 1
    
    # Create a dictionary of the uncompleted gates with their values
    calculate = {}
    for index in range(len(count_freedom_and_uncompleted)):
        gate_info = count_freedom_and_uncompleted[index]
        if gate_info[1] != 0:
            calculate[index + 1] = gate_info[0] - gate_info[1]
    
    # Get the gate with the min value
    minimum =  [key for key in calculate if 
        all(calculate[temp] >= calculate[key] 
        for temp in calculate)]
    gate = gates[rnd.choice(minimum) - 1]

    # Return the net id from an uncompleted net
    for net in gate.nets:
        if net.completed == False:
            return net.id - 1

def get_min_manhattan_net(nets):
    """ Finds the uncompleted net with the shortest Manhattan distance. 
    """
    uncompleted_nets = []
    for net in nets:
        if net.completed == False:
            uncompleted_nets.append(net)
    return (min_nets(uncompleted_nets) - 1)

def get_max_manhattan_net(nets):
    """ Finds the uncompleded net with the longest Manhattan distance. 
    """
    uncompleted_nets = []
    for net in nets:
        if net.completed == False:
            uncompleted_nets.append(net)
    return (max_nets(uncompleted_nets) - 1)
    