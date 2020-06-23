"""
helpers.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file contains the helper functions used in the code.
"""
import csv, ast
import random as rnd
from .models.gates import Gate
from .models.grid import Grid
from .models.nets import Nets

def get_gates(gate_csv_path):
    """ Returns a list of gates with the gate information.
    """
    # Get coordinates
    with open(gate_csv_path, mode='r') as f:
        reader = csv.reader(f)
        gates = []
        for row in reader:
            if row[0] != "chip":
                gate = Gate(row[0], row[1], row[2])
                gates.append(gate)
    return gates

def get_nets(gates, netlist_csv_path):
    """ Returns a list of nets and an updates list of gates with all the information.
    """
    with open(netlist_csv_path, mode='r') as f:
        reader = csv.reader(f)
        count = 1
        nets = []
        for row in reader:
            if row[0] != "chip_a":
                net = Nets(count, gates[int(row[0])-1], gates[int(row[1])-1])
                gates[int(row[0])-1].add_net(net)
                gates[int(row[0])-1].add_connection(int(row[1])-1)
                gates[int(row[1])-1].add_net(net)
                gates[int(row[1])-1].add_connection(int(row[0])-1)
                nets.append(net)
                count += 1
    return gates, nets

def random_netlist(gates, netlist_csv_path):
    """ Returns a list of nets and an updates list of gates with all the information.
        Netlist is self random made.
    """
    # Count the amount of nets
    with open(netlist_csv_path) as f:
        net_count = sum(1 for line in f) - 1
    
    nets = []

    # Create a net and save them in nets and gates
    for net_id in range(1, net_count + 1):
        # Find a correct begin gate
        while True:
            begin_gate = rnd.randint(0, len(gates))
            if (len(gates[begin_gate].connections) <= 4):
                break

        end_gate_options = list(range(0, len(gates)))
        rnd.shuffle(end_gate_options)

        # Find a correct end gate
        while True:
            end_gate = end_gate_options.pop()
            if (end_gate != begin_gate) and (not (end_gate in gates[begin_gate].connections)) and (len(gates[end_gate].connections) <= 4):
                break

        # Save the net and print the net 
        net = Nets(net_id, gates[begin_gate], gates[end_gate])
        gates[begin_gate].add_net(net)
        gates[begin_gate].add_connection(end_gate)
        gates[end_gate].add_net(net)
        gates[end_gate].add_connection(begin_gate)
        nets.append(net)
        print(f"Net {net_id} gaat van gate {begin_gate + 1} naar {end_gate + 1}")
    return gates, nets

def get_paths(path_csv):
    """ Gets the path coordinates from an output.csv file.
    """
    with open(path_csv, mode='r') as f:
        reader = csv.reader(f)
        paths = []
        for row in reader:
             if 'True' in row:
                paths.append(ast.literal_eval(row[2]))
    return paths

def uncompleted_nets(nets):
    """ Check if there are uncompleted nets, return True if there are, otherwise False.
    """
    for net in nets:
        if net.completed == False:
            return True
    return False

def create_bigpath(nets):
    """ Return a list with lists of wires from every net.
    """
    bigpath = []
    for net in nets:
        bigpath.append(net.wires)   
    return bigpath

def scary_gates(gate_list):
    """ Create dictionary of coordinates that neighbour gates. Dictionary keys are
        the coordinates and its value is the gate coordinate.
    """
    scary_dict = {}
    for gate in gate_list:
        gate_coordinate = (gate.x, gate.y, gate.z)
        options = find_options(gate_coordinate)

        for neighbour in options:
            scary_dict[neighbour] = gate_coordinate
    return scary_dict

def reset_net(grid, net):
    """ Reset wires in grid and net example.
    """
    net.begin_gate.wires.pop(net.id, None)
    net.end_gate.wires.pop(net.id, None)
    grid.reset_net(net)
    net.reset_wires()

def find_options(current_coordinates):
    """ List path options in all six directions, shuffled.
    """
    options = []
    for coordinate_index in range(0, 3):

        # Determine options neighbouring the current coordinate
        for neighbourcoordinate in range(-1, 2, 2):
            temp_coordinate = [current_coordinates[0], current_coordinates[1], current_coordinates[2]]
            temp_coordinate[coordinate_index] += neighbourcoordinate
            options.append(tuple(temp_coordinate))
    return options

def filter_options(options, grid):
    """ Check if options are within grid parameters.
    """
    valid_options = []
    for option in options:
        if not (min(option) <= -1 or option[0] >= grid.x_dim or option[1] >= grid.y_dim or option[2] >= grid.z_dim):
            valid_options.append(option)
    return valid_options
