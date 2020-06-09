"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
"""
import os
import random
import csv
import numpy as np

from helpers import *
from save_results import *
from random_algo import *

# Get gates and nets list with all the gates and nets
gates, nets = get_gates_and_nets()

# Create a matrix of the grid with all the gates
grid = Grid(gates)

# TODO: algorithm/heuristics, create wires and save them in the nets and matrix
run = random_algo(grid, gates, nets)

# Get results and create csv file
get_results(nets, grid)

