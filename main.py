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
from code.results import get_results, costs
from code.algorithms.random_algo import *
from code.algorithms.dijkstra import Dijkstra
from code.algorithms.a_star import A_star
from code.helpers import get_gates_and_nets, get_paths, uncompleted_nets, create_bigpath
from code.visualisation.visualiser import visualiser 
from code.algorithms.select_net import get_min_freedom_net, get_random_nets

def menu():
    print("Welkom")

    # Specify what gate and what nets csv file to take
    chip = int(input("Kies de chip (0, 1 of 2): "))
    gate_coordinates_csv_path = f"data/input/gates&netlists/chip_{chip}/print_{chip}.csv"
    netlist = int(input("Kies de netlist(1, 2 of 3): ")) + 3 * chip
    gate_connections_csv_path = f"data/input/gates&netlists/chip_{chip}/netlist_{str(netlist)}.csv"
    
    # Get gates and nets list with all the gates and nets
    gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

    # Create a matrix of the grid with all the gates
    grid = Grid(gates)

    algorithm_dict = {
        "1": "random",
        "2": "dijkstra",
        "3": "astar"
        }

    # Choose and run algorithm
    algorithm = int(input("Kies het nummer van de algorithme (1, 2 of 3) of 0 voor meer informatie: "))
    if algorithm == 0:
        print(algorithm_dict)
        algorithm = int(input("Kies het nummer van de algorithme (1, 2 of 3): "))
        
    if algorithm == 1:
        # TODO: optie geven om te loopen tot er een goede oplossing is gevonden
        random_net_ids = get_random_nets(nets)
        random(grid, gates, random_net_ids, nets)

        # Great bigpath for the visualisation
        bigpath = create_bigpath(nets)

    elif algorithm == 2:
    #     Dijkstra??
        bigpath =[]
        uncompleted = True
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            dijk = Dijkstra(grid, net)
            path = dijk.search()
            bigpath.append(path)
            uncompleted = uncompleted_nets(nets)

    elif algorithm == 3:
        bigpath =[]
        uncompleted = True
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            a_star = A_star(grid, net)
            path = a_star.search()
            bigpath.append(path)
            uncompleted = uncompleted_nets(nets)

    # Get results and create csv file
    algorithm_name = algorithm_dict[f"{algorithm}"]
    save_folder = f"data/results/{algorithm_name}/chip_{chip}_net_{netlist}/"
    chip_name = f"chip_{chip}_net_{netlist}"
    print(get_results(save_folder, chip_name, nets, grid))

    # # TODO: weghalen voor final
    # # Alleen kosten printen
    # total_costs, wire_count, intersection_count, conflict_count = costs(nets, grid)
    # print(f"Costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections. Conflicts: {conflict_count}.")

    # Visualisation
    visualiser(grid, gates, bigpath)


if __name__ == "__main__":
    # TODO: dit uitcommenten voor t einde en de menu() alleenstaand wel verwijderen
    menu()
    # try:
    #     menu()
    # except:
    #     print("Het lijkt erop dat er iets fout is gegaan. Probeer het nog een keer!")




    # # Specify what gate and what nets csv file to take
    # gate_coordinates_csv_path = "data/input/gates&netlists/chip_1/print_1.csv"
    # gate_connections_csv_path = "data/input/gates&netlists/chip_1/netlist_4.csv"

    # # Get gates and nets list with all the gates and nets
    # gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

    # # Create a matrix of the grid with all the gates
    # grid = Grid(gates)

    # # TODO: keuzemenu voor verschillende algoritmes die ook de resultaten ervan in de goede map weergeeft
    # # Algorithm/heuristics, create wires and save them in the nets and matrix
    # random(grid, gates, nets)

    # # # Dijkstra`
    # # bigpath =[]
    # # uncompleted = True
    # # for net in nets:
    # #     dijkstra = Dijkstra(grid, net)
    # #     dijkstra.expand_frontier()
    # #     path = dijkstra.make_path()
    # #     bigpath.append(path)


    # # # Kies de net met minste extra freedom
    # # uncompleted = True
    # # while uncompleted:
    # #     net_id = get_min_freedom_net(gates, grid)
    # #     net = nets[net_id]
    # #     dijk = Dijkstra(grid, net)
    # #     dijk.expand_frontier()
    # #     path = dijk.make_path()
    # #     bigpath.append(path)
    # #     uncompleted = uncompleted_nets(nets)

    # # Visualisation
    # # visualiser(grid, gates, bigpath)

    # # # TODO: maak de map voor resultaten anders per ander algoritme door keuzemenu
    # # # Get results and create csv file
    # save_folder = "data/results/random/chip_2_net_7/"
    # # # TODO: de chipnaam moet veranderd worden aan de variabele die bij de gate en nets geimporteerd worden
    # chip_name = "chip_0_net_1"
    # print(get_results(save_folder, chip_name, nets, grid)) 
    

    # # # alleen kosten print
    # # total_costs, wire_count, intersection_count, conflict_count = costs(nets, grid)
    # # print(f"Costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections. Conflicts: {conflict_count}.")
