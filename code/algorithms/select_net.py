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
    count = []

    # Go through every gate and count the neighbour freedom
    for gate in gates:
        count.append(0)

        # Check if there is a net uncompleted in this gate
        not_completed = False
        for net in gate.nets:
            if net.completed == False:
                not_completed = True
                break
        
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
                        count[gate.id - 1] += 1

    # Get the gate with min freedom and return the first uncompleted net
    gate = count.index(min(count))
    for net in gate.nets:
        if net.completed == False:
            return net



        

