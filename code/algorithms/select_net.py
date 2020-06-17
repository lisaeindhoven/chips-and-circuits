"""
select_net.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains every function to get nets in different orders.
"""
import random as rnd

def get_random_nets(nets):
    """Returns a list of net ids in random order from the not completed nets"""
    random_net_ids = []
    for net in nets:
        if not net.completed:
            random_net_ids.append(net.id - 1)
    rnd.shuffle(random_net_ids)

def get_min_freedom_net(gates, grid):
    """Returns a net id based on the freedom around the gate"""
    count_freedom_and_uncompleted = []

    # Go through every gate and count the neighbour freedom
    for gate in gates:
        # first item is the available freedom and the second is the not nr not completed nets of the gate
        count_freedom_and_uncompleted.append([0, 0])

        # Check if there is a net uncompleted in this gate
        not_completed = False
        for net in gate.nets:
            if net.completed == False:
                not_completed = True
                break
            else:
                count_freedom_and_uncompleted[gate.id - 1][1] += 1
        
        # Count number of free spots
        if not_completed:
            coordinates = gate.coordinate()

            # TODO: is kopie van random_algo
            north = (coordinates[0], coordinates[1]+1, coordinates[2])
            south = (coordinates[0], coordinates[1]-1, coordinates[2])
            west = (coordinates[0]-1, coordinates[1], coordinates[2])
            east = (coordinates[0]+1, coordinates[1], coordinates[2])
            up = (coordinates[0], coordinates[1], coordinates[2]+1)
            down = (coordinates[0], coordinates[1], coordinates[2]-1)

            options = [north, south, west, east, up, down]

            for option in options:
                if not (min(option) < 0 or option[0] >= grid.x_dim or option[1] >= grid.y_dim or option[2] >= grid.z_dim):
                    if grid.item(option) == []:
                        count_freedom_and_uncompleted[gate.id - 1][0] += 1

    for gate in count_freedom_and_uncompleted:
        if gate[1] != 0:
            gate = gate[0] / gate[1]

    # Get the gate with min freedom and return the first uncompleted net
    gate_index = count_freedom_and_uncompleted.index(min(count_freedom_and_uncompleted))
    for net in gates[gate_index
    ].nets:
        if net.completed == False:
            return net.id

    # TODO afwegen tegen hoeveel open connecties



        

