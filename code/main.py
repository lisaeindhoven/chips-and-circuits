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
from algorithms.random import *

# TODO: dit allemaal in if main = main gebeuren?

# Specify what gate and what nets csv file to take
gate_coordinates_csv_path = "Docs/example/print_0.csv"
gate_connections_csv_path = "Docs/example/netlist_1.csv"

# Get gates and nets list with all the gates and nets
gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

# Create a matrix of the grid with all the gates
grid = Grid(gates)

# TODO: keuzemenu voor verschillende algoritmes die ook de resultaten ervan in de goede map weergeeft
# Algorithm/heuristics, create wires and save them in the nets and matrix
run = random(grid, gates, nets)

# TODO: maak de map voor resultaten anders per ander algoritme door keuzemenu
# Get results and create csv file
save_folder = "Docs/Results/Random/"
# TODO: de chipnaam moet veranderd worden aan de variabele die bij de gate en nets geimporteerd wordden
chip_name = "chip_0_net_1"
print(get_results(save_folder, chip_name, nets, grid))