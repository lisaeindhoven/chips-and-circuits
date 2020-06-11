"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
"""
# TODO: op elke pagina imports goedkrijgen
import os
import random
import csv
import numpy as np

#from helpers import *
from code.save_results import *
from code.algorithms.random import *
from code.helpers import *
# from code.visualisation.visualiser import *

if __name__ == "__main__":

    # Specify what gate and what nets csv file to take
    gate_coordinates_csv_path = "data/input/gates&netlists/chip_0/print_0.csv"
    gate_connections_csv_path = "data/input/gates&netlists/chip_0/netlist_1.csv"

    # Get gates and nets list with all the gates and nets
    gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

    # Create a matrix of the grid with all the gates
    grid = Grid(gates)

    # TODO: keuzemenu voor verschillende algoritmes die ook de resultaten ervan in de goede map weergeeft
    # Algorithm/heuristics, create wires and save them in the nets and matrix
    random(grid, gates, nets)

    # TODO: maak de map voor resultaten anders per ander algoritme door keuzemenu
    # Get results and create csv file
    save_folder = "data/results/random/chip_0_net_1/"
    # TODO: de chipnaam moet veranderd worden aan de variabele die bij de gate en nets geimporteerd wordden
    chip_name = "chip_0_net_1"
    print(get_results(save_folder, chip_name, nets, grid))

    # # Visualisation
    # paths = []
    # paths.append([(1,5,0),(2,5,0),(3,5,0),(3,5,1),(4,5,1),(4,5,0),(5,5,0),(6,5,0)])
    # paths.append([(6,2,0),(6,3,0),(6,4,0),(6,5,0)])

    # visualiser(grid, gates, paths)