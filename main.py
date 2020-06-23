"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file is the main python file
"""
import csv
import math
import numpy as np

from code.models.grid import Grid
from code.results import get_results, costs
from code.algorithms.random_algo import random
from code.algorithms.dijkstra import Dijkstra
from code.algorithms.a_star import A_star
from code.helpers import get_gates, get_nets, get_paths, uncompleted_nets, create_bigpath, scary_gates, reset_net, random_netlist, find_options, filter_options
from code.algorithms.downhill import hilldescent, conflict_remover
from code.algorithms.select_net import get_min_freedom_net, get_random_nets, get_min_manhattan_net, get_max_manhattan_net
from code.visualisation.visualiser import visualiser 

def menu():
    print("Welkom bij Chips-and-Circuits van Lisa, Mik en Sebas (de Misbaksels)",
        "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",
        sep="\n")

    # Specify what chip to take and save the gates into gate objects
    chip = int(input("Kies de chip (van klein tot groot: 0, 1 of 2): "))
    gate_csv_path = f"data/input/gates&netlists/chip_{chip}/print_{chip}.csv"
    gates = get_gates(gate_csv_path)

    # Specify what netlist to take and save the nets into nets objects and append the nets to the gates
    netlist = int(input("Kies de netlist (van simpel tot complex: 1, 2 of 3): ")) + 3 * chip
    netlist_method = int(input("Wilt u een random (0) of een bestaande (1) netlist gebruiken? "))
    netlist_csv_path = f"data/input/gates&netlists/chip_{chip}/netlist_{str(netlist)}.csv"
    if netlist_method == 1:
        gates, nets = get_nets(gates, netlist_csv_path)
    else:
        gates, nets = random_netlist(gates, netlist_csv_path)

    # Create a matrix of the grid with all the gates
    grid = Grid(gates)

    algorithm_dict = {
        "1": "random",
        "2": "dijkstra",
        "3": "a_star",
        "4": "avoid_gates",
        "5": "skyscraper",
        "6": "hilldescent",
        "7": "cheap_intersections"
    }

    net_select_dict = {
        "1": "Net met minste extra vrijheid rond de gate",
        "2": "Net met minste manhattan distance eerst",
        "3": "Net met meeste manhattan distance eerst"
    }

    # Choose and run algorithm
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",
        "Kies het algoritme nummer (1, 2, 3, 4, 5, 6, of 7) of 0 voor meer informatie over welk nummer bij welk algoritme hoort",
        "3 is snel, maar 6 garandeert een mooi resultaat - duur van 6 bedraagt < :30, < 2:00, < 5:00 voor chip 0, 1 en 2, resp",
        sep="\n")

    algorithm = int(input("Lees de read me voor een nog duidelijkere omschrijving van de algoritmes: "))
    if algorithm == 0:
        print(algorithm_dict)
        algorithm = int(input("Kies het algoritme (1, 2, 3, 4, 5, 6, of 7): "))
        
    # Random
    if algorithm == 1:
        random_net_ids = get_random_nets(nets)
        random(grid, gates, random_net_ids, nets)

    else:
        # Let the user choose the way the nets are selected
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",
        "Kies de net keuze (1, 2 of 3) of 0 voor meer informatie",
        "Let op, alle opties maken gebruik van een random keuze als er meerdere mogelijkheden zijn,",
        "hierdoor is het verstandig meerdere keren hetzelfde te runnen om het beste resultaat te krijgen.",
        "De resultaten zijn terug te vinden in de map data/results.",
        sep="\n")
        select_net = int(input("Optie 1 heeft onze voorkeur: "))
        if select_net == 0:
            print(net_select_dict)
            select_net = int(input("Kies de net keuze (1, 2 of 3): "))

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        # Greate scary gate dictionary
        scary_dict = scary_gates(gates)

        # Dijkstra
        if algorithm == 2:
            costs_tup=(1,300,100000,0,0)
        # A star
        elif algorithm == 3:
            costs_tup=(1,300,100000,0,0)
        # Avoid gates (A star)
        elif algorithm == 4:
            costs_tup=(1,300,100000,10,0)
        # Skyscraper (A star)
        elif algorithm == 5:
            costs_tup=(1,300,100000,0,-1)
        # Hilldescent (after Avoid gates)
        elif algorithm == 6:
            costs_tup=(1,300,100000,10,0)
        # Cheap intersections(Avoid A star) + Conflict_remover and Avoid gates + Hilldescent
        elif algorithm == 7:
            costs_tup=(1,3,100000,10,0)
            
        while uncompleted_nets(nets):
            # Get the right net
            if select_net == 1:
                net_id = get_min_freedom_net(gates, grid)
            elif select_net == 2:
                net_id = get_min_manhattan_net(nets)
            elif select_net == 3:
                net_id = get_max_manhattan_net(nets)

            # Select net
            net = nets[net_id]

            # Lay paths
            if "dijkstra" in algorithm_dict[str(algorithm)]:
                dijk = Dijkstra(grid, net, scary_dict, costs_tup)
                dijk.search()
            else:
                a_star = A_star(grid, net, scary_dict, costs_tup)
                a_star.search()
            
    # The wombo combo
    if algorithm == 7:
        total_costs, wire_count, intersection_count = costs(nets, grid)
        print(f"First run (cheap_intersections) costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")

        # Remove all the nets involved in conflicts
        removed_nets = conflict_remover(grid, nets)
        print("Removed all nets involved in intersections")
        costs_tup=(1,300,100000,10,0)

        # Create paths again
        for net in removed_nets:
            a_star = A_star(grid, net, scary_dict, costs_tup)
            a_star.search()
    
    # Hilldescent
    if algorithm == 6 or algorithm == 7:
        total_costs, wire_count, intersection_count = costs(nets, grid)
        print(f"Kosten voorafgaande aan hilldescent zijn {total_costs}, voortkomend uit {wire_count} draad-eenheden en {intersection_count} intersections.")

        hilldescent(grid, nets, scary_dict, gates)
        print(f"Hilldescent completed. ")

    # Collect all nets for the visualisation
    bigpath = create_bigpath(nets)

    # Get results and create csv file
    # We edit net.wires to fit check50 results (why we make bigpath first so the visualisation can work with it)
    algorithm_name = algorithm_dict[f"{algorithm}"]
    save_folder = f"data/results/{algorithm_name}/chip_{chip}_net_{netlist}/"
    chip_name = f"chip_{chip}_net_{netlist}"
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(get_results(save_folder, chip_name, nets, grid))

    # Visualisation
    visualiser(grid, gates, bigpath)


if __name__ == "__main__":
    try:
        menu()
    except:
        print("Het lijkt erop dat er iets fout is gegaan. Probeer het nog een keer of contacteer de Misbaksels!",
        "Als je wilt weten wat er precies fout gaat, kan deze try except uitgezet worden, zodat het de main alleen het menu aanroept en de orginele foutmelding in de terminal verschijnt!",
        sep="\n")
