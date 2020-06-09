"""
helpers.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the helper function for main.py
"""
import csv

from gates import *
from grid import *
from nets import *

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