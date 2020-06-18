"""
manhattan.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

These functions calculate the (minimum/maximum) manhattan distance
between (a multitude of) two sets of coordinates.
Use min/max_net for the determined shortest distance, 
use min/max_nets to randomize the result in case of a tie.
"""
import random

def measure(a_coordinates, b_coordinates):
    """ This function returns the manhattan distance
        as measured between two sets of coordinates """
    x_diff = abs(a_coordinates[0] - b_coordinates[0])
    y_diff = abs(a_coordinates[1] - b_coordinates[1])
    z_diff = abs(a_coordinates[2] - b_coordinates[2])
    return x_diff + y_diff + z_diff

def measurement_list(nets):
    """ This function returns a dict of the different manhattan
        distances between all the provided nets """
    manh_netlist = {}
    for net in nets:
        manh_diff = measure(net.begin_gate.coordinate(), net.end_gate.coordinate())
        manh_netlist[net.id] = manh_diff
    return manh_netlist

def min_net(nets):
    """ Returns {net.id: distance} of the shortest manhattan distance
        in the provided netlist """
    manh_netlist = measurement_list(nets)
    min_net = min(manh_netlist, key=lambda k: manh_netlist[k])
    min_distance = manh_netlist[min_net]
    return {min_net: min_distance}

def min_nets(nets):
    """ returns a random net.id of all the equally shortest distances
        in a netlist """
    manh_netlist = measurement_list(nets)
    min_value = min(manh_netlist.values())
    min_netlist = [net_id for net_id in manh_netlist if manh_netlist[net_id] == min_value]
    return random.choice(min_netlist)

def max_net(nets):
    """ Returns {net.id: distance} of the longest manhattan distance
        in the provided netlist """
    manh_netlist = measurement_list(nets)
    max_net = max(manh_netlist, key=lambda k: manh_netlist[k])
    max_distance = manh_netlist[max_net]
    return {max_net: max_distance}

def max_nets(nets):
    """ Returns a random net.id of all the equally longest
        distances in a netlist """
    manh_netlist = measurement_list(nets)
    max_value = max(manh_netlist.values())
    max_netlist = [net_id for net_id in manh_netlist if manh_netlist[net_id] == max_value]
    return random.choice(max_netlist)
