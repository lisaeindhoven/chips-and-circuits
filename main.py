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

from code.models.grid import Grid
from code.save_results import get_results
from code.algorithms.random_algo import *
from code.algorithms.dijkstra import Dijkstra
from code.helpers import get_gates_and_nets, get_paths
from code.visualisation.visualiser import visualiser 

if __name__ == "__main__":

    # Specify what gate and what nets csv file to take
    gate_coordinates_csv_path = "data/input/gates&netlists/chip_0/print_0.csv"
    gate_connections_csv_path = "data/input/gates&netlists/chip_0/netlist_1.csv"
    paths_csv = "data/highlighted_results/random/chip_0_net_1/output_06.11.2020_10.44.27.csv"

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

    # Dijkstra
    bigpath =[]
    for net in nets:
        dijk = Dijkstra(grid, net)
        dijk.make_path()
        bigpath.append(dijk.path)
    print(bigpath)

    # Visualisation
    #paths = get_paths(paths_csv)
    visualiser(grid, gates, bigpath)
    
    


