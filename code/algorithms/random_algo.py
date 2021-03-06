"""
random.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file contains the random algorithm and some functions one could import.
"""
from code.helpers import find_options, filter_options
import random as rnd
import copy

def random(grid, gates, random_net_ids, nets):
    """ This algorithm attempts to connect all the gates in random order,
        randomly proceeding until it either reaches the connectable gate or is stuck.
    """
    # Count whenever an attempt to connect two gates fails
    conflicts = 0

    # For every net in random order we attempt to connect the two gates
    for random_net in random_net_ids:
        create_net(random_net, nets, grid)
        if nets[random_net].completed == False:
            conflicts += 1
            
    nets_count = len(nets)
    solved_nets = nets_count - conflicts
    print(f"Total nets: {nets_count}, solved: {solved_nets}, conflicts: {conflicts}.")

def create_net(random_net, nets, grid):
    """ Attempt to connect two gates via a net. 
    """
    current_net = nets[random_net]

    # Fet current -, start -, and end coordinates
    start_coordinates, end_coordinates, current_coordinates = set_coordinates(current_net)

    # Find paths and lay wire until the end is reached or no options remain
    while current_coordinates != end_coordinates:

        # Find path options
        options = find_options(current_coordinates)
        rnd.shuffle(options)
        options = filter_options(options, grid)

        # This boolean will change if there if a path is found and chosen
        found_path = False

        # Check if one of the option is already the end gate
        for current_option in options:
            found_path, current_coordinates = reached_end(current_option, grid, current_net)
            if found_path:
                break

        if not found_path:
            # Create valid path if possible
            for current_option in options:

                item = grid.item(current_option)
        
                # In this algorithm; only add a wire if there isnt one already
                if item == []:
                    current_coordinates = lay_wire(current_net, current_option, grid)
                    found_path = True
                    break
    
        if not found_path:
            break

def set_coordinates(current_net):
    """ Get start and end coordinates.
    """
    coordinate = current_net.get_coordinates()
    return coordinate[0], coordinate[1], copy.deepcopy(coordinate[0])
                    
def reached_end(current_option, grid, current_net):
    """ Check if option is destination.
    """
    item = grid.item(current_option)

    # Go to the end gate if it's one of the options
    if item == current_net.end_gate:
        current_net.add_wire(current_option)
        current_net.completed = True
        print(f"Net {current_net.id} is gelegd tussen gate {current_net.begin_gate.id} en {current_net.end_gate.id}")
        return True, copy.deepcopy(current_option)
    return False, current_option

def lay_wire(current_net, current_option, grid):
    """ Lay wire on grid, add it to net and change current coordinates. 
    """
    current_net.add_wire(current_option)
    grid.add_wire(current_option, current_net)
    return copy.deepcopy(current_option)
