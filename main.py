"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
"""
# TODO: op elke pagina imports goedkrijgen
import random
import csv
import math
import numpy as np

from code.models.grid import Grid
from code.results import get_results, costs
from code.algorithms.random_algo import *
from code.algorithms.dijkstra import Dijkstra
from code.algorithms.avoid_gates import Avoid_gates
from code.algorithms.a_star import A_star
from code.algorithms.skyscraper import Skyscraper
from code.algorithms.free_intersections import Free_intersections
from code.algorithms.combo import Combo
from code.helpers import get_gates_and_nets, get_paths, uncompleted_nets, create_bigpath, scary_gates, reset_net
from code.visualisation.visualiser import visualiser 
from code.algorithms.select_net import get_min_freedom_net, get_random_nets, get_min_manhattan_net, get_max_manhattan_net
from code.algorithms.metaclimber import Metaclimber

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
        "3": "A_star",
        "4": "avoid_gates",
        "5": "skyscraper",
        "6": "free_intersections_first",
        "7": "Chefs_special"
    }

    net_select_dict = {
        "1": "Net met minste extra vrijheid rond de gate",
        "2": "Net met minste manhattan distance eerst",
        "3": "Net met meeste manhattan distance eerst"
    }

    # Choose and run algorithm
    algorithm = int(input("Kies het algoritme (1, 2, 3, 4, 5, 6 of 7) of 0 voor meer informatie: "))
    if algorithm == 0:
        print(algorithm_dict)
        algorithm = int(input("Kies het algoritme (1, 2, 3, 4, 5, 6 of 7): "))
        
    # Random
    if algorithm == 1:
        # TODO: optie geven om te loopen tot er een goede oplossing is gevonden
        random_net_ids = get_random_nets(nets)
        random(grid, gates, random_net_ids, nets)

        # Great bigpath for the visualisation
        # bigpath = create_bigpath(nets)

    # Dijkstra
    elif algorithm == 2:
        # Let the user choose the way the nets are selected
        select_net = int(input("Kies de net keuze (1, 2 of 3) of 0 voor meer informatie: "))
        if select_net == 0:
            print(net_select_dict)
            select_net = int(input("Kies de net keuze (1, 2 of 3): "))
            
        uncompleted = True
        scary_dict = scary_gates(gates)
        while uncompleted:
            # Get the right net
            if select_net == 1:
                net_id = get_min_freedom_net(gates, grid)
            elif select_net == 2:
                net_id = get_min_manhattan_net(nets)
            elif select_net == 3:
                net_id = get_max_manhattan_net(nets)

            # Dijkstra
            net = nets[net_id]
            dijk = Dijkstra(grid, net, scary_dict, costs_tup=(1,301,100000,1,1))
            path = dijk.search()
            uncompleted = uncompleted_nets(nets)

    # A star
    elif algorithm == 3:
        uncompleted = True
        scary_dict = scary_gates(gates)
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            a_star = A_star(grid, net, scary_dict, costs_tup=(1,301,100000,1,1))
            path = a_star.search()
            uncompleted = uncompleted_nets(nets)

    # Avoid gates (A star)
    elif algorithm == 4:
        uncompleted = True
        scary_dict = scary_gates(gates)
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            avoider = A_star(grid, net, scary_dict, costs_tup=(1,301,100000,10,1))
            path = avoider.search()
            uncompleted = uncompleted_nets(nets)
    
    # Skyscraper (A star)
    elif algorithm == 5:
        uncompleted = True
        scary_dict = scary_gates(gates)
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            skyscraper = A_star(grid, net, scary_dict, costs_tup=(1,301,100000,1,0))
            path = skyscraper.search()
            uncompleted = uncompleted_nets(nets)

    # Free intersections (A star)
    elif algorithm == 6:
        uncompleted = True
        scary_dict = scary_gates(gates)
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            freeway = A_star(grid, net, scary_dict, costs_tup=(1,0,100000,1,1))
            path = freeway.search()
            uncompleted = uncompleted_nets(nets)

    # Combination run
    elif algorithm == 7:
        uncompleted = True   
        scary_dict = scary_gates(gates)
        while uncompleted:
            net_id = get_min_freedom_net(gates, grid)
            net = nets[net_id]
            avoider = A_star(grid, net, scary_dict, costs_tup=(1,301,100000,10,1))
            path = avoider.search()
            uncompleted = uncompleted_nets(nets)
        total_costs, wire_count, intersection_count = costs(nets, grid)
        print(f"First run (avoid) costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")
        
        # Metaclimber.conflict_remover(grid, nets)
        # uncompleted = uncompleted_nets(nets)
        
        # while uncompleted:
        #     net_id = get_min_freedom_net(gates, grid)
        #     net = nets[net_id]
        #     finish = A_star(grid, net)
        #     path = finish.search()
        #     uncompleted = uncompleted_nets(nets)

        # total_costs, wire_count, intersection_count = costs(nets, grid)
        # print(f"Third run (A star) costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")
        
        grid, nets = Metaclimber.hilldescent(grid, nets)
        total_costs, wire_count, intersection_count = costs(nets, grid)
        print(f"Hilldescent completed. Costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")


    # Reset the net.wires and delete net from grid
    # TODO deze example weghalen
    # reset_net(grid, nets[2])

    # TODO: OVERAL BIGPATH WEG HALEN, EN PAS CREEREN MET BEHULP VAN DE FUNCTIE CREATE_BIGPATH VOOR DE VISUALITATIE
    # Great bigpath for the visualisation
    bigpath = create_bigpath(nets)

    # Get results and create csv file
    # TODO let op, bigpath maken moet eerder dan dit, omdat anders de visualisatie het op een vage wijze niet doet
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
    # gate_coordinates_csv_path = "data/input/gates&netlists/chip_0/print_0.csv"
    # gate_connections_csv_path = "data/input/gates&netlists/chip_0/netlist_2.csv"

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
