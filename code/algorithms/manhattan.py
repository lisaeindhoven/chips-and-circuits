"""
manhattan.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

These functions calculate the (minimum/maximum) manhattan distance
between (a multitude of) two sets of coordinates.
"""

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
    """ This function returns {net.id: distance}
        of the shortest manhattan distance in the provided netlist """
    manh_netlist = measurement_list(nets)
    min_net = min(manh_netlist, key=lambda k: manh_netlist[k])
    min_distance = manh_netlist[min_net]
    return {min_net: min_distance}

def min_nets(nets):
    """ returns the net.id and distance of the (equally) 
        shortest distances in a netlist """
        #TODO return all options in case of tie
    pass

def max_net(nets):
    """ This function returns {net.id: distance}
        of the longest manhattan distance in the provided netlist """
    manh_netlist = measurement_list(nets)
    print(manh_netlist)
    max_net = max(manh_netlist, key=lambda k: manh_netlist[k])
    print(min_net)

def max_nets(nets):
    """ returns the net.id and distance of the (equally) 
        longest distances in a netlist """
        #TODO return all options in case of tie
    pass





