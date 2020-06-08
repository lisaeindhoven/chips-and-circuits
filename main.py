"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
"""
import os

from helpers import *
from save_results import *

# Get gates and nets list with all the gates and nets
gates, nets = get_gates_and_nets()

# Create a matrix of the grid with all the gates
grid = Grid(gates)

# TODO: algorithm/heuristics, create wires and save them in the nets and matrix

# Get results and create csv file
get_results(nets, grid)