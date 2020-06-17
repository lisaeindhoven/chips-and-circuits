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
import math
import numpy as np

from code.models.grid import Grid
from code.save_results import get_results
from code.algorithms.random_algo import *
from code.algorithms.dijkstra import Dijkstra
from code.helpers import get_gates_and_nets, get_paths, uncompleted_nets
from code.visualisation.visualiser import visualiser 
from code.algorithms.select_net import get_min_freedom_net

if __name__ == "__main__":

    # Specify what gate and what nets csv file to take
    gate_coordinates_csv_path = "data/input/gates&netlists/chip_1/print_1.csv"
    gate_connections_csv_path = "data/input/gates&netlists/chip_1/netlist_6.csv"

    # Get gates and nets list with all the gates and nets
    gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

    # Create a matrix of the grid with all the gates
    grid = Grid(gates)

    # TODO: keuzemenu voor verschillende algoritmes die ook de resultaten ervan in de goede map weergeeft
    # Algorithm/heuristics, create wires and save them in the nets and matrix
    #random(grid, gates, nets)

    # Dijkstra
    bigpath =[]
    uncompleted = True
    # Kies de net met minste extra freedom
    while uncompleted:
        net_id = get_min_freedom_net(gates, grid)
        net = nets[net_id]
        dijk = Dijkstra(grid, net)
        dijk.expand_frontier()
        dijk.make_path(nets)
        bigpath.append(dijk.path)
        uncompleted = uncompleted_nets(nets)

    # TODO: maak de map voor resultaten anders per ander algoritme door keuzemenu
    # Get results and create csv file
    save_folder = "data/results/random/chip_0_net_1/"
    # TODO: de chipnaam moet veranderd worden aan de variabele die bij de gate en nets geimporteerd worden
    chip_name = "chip_0_net_1"
    print(get_results(save_folder, chip_name, nets, grid))

    # Visualisation
    visualiser(grid, gates, bigpath)
    