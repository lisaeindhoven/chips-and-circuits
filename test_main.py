import random
import csv
import math
import numpy as np

from code.models.grid import Grid
from code.results import get_results, costs
from code.algorithms.random_algo import *
from code.algorithms.dijkstra import Dijkstra
from code.algorithms.a_star import A_star
from code.helpers import get_gates, get_nets, get_paths, uncompleted_nets, create_bigpath, scary_gates, reset_net, random_netlist
from code.visualisation.visualiser import visualiser 
from code.algorithms.select_net import get_min_freedom_net, get_random_nets, get_min_manhattan_net, get_max_manhattan_net
from code.algorithms.metaclimber import Metaclimber

def get_data(algorithm, iterations):
    """ Runs an algorithm for a certain number of iterations and
        saves data.
    """
    # Specify what gate and what nets csv file to take
    chip = 1
    gate_csv_path = f"data/input/gates&netlists/chip_{chip}/print_{chip}.csv"
    netlist = 4
    netlist_csv_path = f"data/input/gates&netlists/chip_{chip}/netlist_{str(netlist)}.csv"
    select_net = 1
    algorithm = algorithm
    data = []

    algorithm_dict = {
    "1": "random",
    "2": "dijkstra",
    "3": "A_star",
    "4": "avoid_gates",
    "5": "skyscraper",
    "6": "free_intersections_first",
    "7": "Chefs_special"
    }

    # Random
    for i in range(iterations):
        print(f'Running {algorithm_dict[str(algorithm)]} {i+1} of {iterations}')
         # Get gates and nets list with all the gates and nets
        gates = get_gates(gate_csv_path)
        gates, nets = get_nets(gates, netlist_csv_path)
        # Create a matrix of the grid with all the gates
        grid = Grid(gates)

        if algorithm == 1:
            # TODO: optie geven om te loopen tot er een goede oplossing is gevonden
            random_net_ids = get_random_nets(nets)
            random(grid, gates, random_net_ids, nets)

        else:
            # Greate scary gate dictionary
            scary_dict = scary_gates(gates)

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
                # Free intersections (A star)
                elif algorithm == 6:
                    costs_tup=(1,0,100000,0,0)
                # Hilclimber
                elif algorithm == 7:
                    costs_tup=(1,300,100000,10,0)

                if "dijkstra" in algorithm_dict[str(algorithm)]:
                    dijk = Dijkstra(grid, net, scary_dict, costs_tup)
                    path = dijk.search()
                else:
                    a_star = A_star(grid, net, scary_dict, costs_tup)
                    path = a_star.search()
                
        if algorithm == 7:
            total_costs, wire_count, intersection_count = costs(nets, grid)
            print(f"First run (avoid) costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")
            
            grid, nets = Metaclimber.hilldescent(grid, nets, scary_dict, gates)
            total_costs, wire_count, intersection_count = costs(nets, grid)
            print(f"Hilldescent completed. Costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections.")

        # Great bigpath for the visualisation
        data.append(costs(nets, grid))
    return data

if __name__ == "__main__":
    data = {}
    data['A*'] = get_data(3, 0)
    data['scary_gates_hill'] = get_data(7, 5)
    #data['skyscraper'] = get_data(5, 0)

    # Save results
    with open('data/results/tests.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Costs'])
        for key, value in data.items():
            writer.writerow([key, value])
        print('Completed! Data stored in data/results/tests.csv')
