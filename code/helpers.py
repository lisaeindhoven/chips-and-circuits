"""
helpers.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the helper function for main.py
"""
import csv, ast

from .models.gates import Gate
from .models.grid import Grid
from .models.nets import Nets
from .algorithms.random_algo import find_options, filter_options

def get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path):
    """returns a dictionary with the gate number, coordinate and connected gates"""
    # Get coordinates
    with open(gate_coordinates_csv_path, mode='r') as f:
        reader = csv.reader(f)
        gates = []
        for row in reader:
            if row[0] != "chip":
                gate = Gate(row[0], row[1], row[2])
                gates.append(gate)

    # Get connections
    with open(gate_connections_csv_path, mode='r') as f:
        reader = csv.reader(f)
        count = 1
        nets = []
        for row in reader:
            if row[0] != "chip_a":
                net = Nets(count, gates[int(row[0])-1], gates[int(row[1])-1])
                gates[int(row[0])-1].add_net(net)
                gates[int(row[1])-1].add_net(net)
                nets.append(net)
                count += 1

    return gates, nets

def get_paths(path_csv):
    """gets the path coordinates from an output.csv file"""
    with open(path_csv, mode='r') as f:
        reader = csv.reader(f)
        paths = []
        for row in reader:
             if 'True' in row:
                paths.append(ast.literal_eval(row[2]))
    return paths

def uncompleted_nets(nets):
    """Check if there are uncompleted nets, return True if there are, otherwise False"""
    for net in nets:
        if net.completed == False:
            return True
    return False

def create_bigpath(nets):
    """Return a list with lists of wires from every net"""
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