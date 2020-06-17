"""
results.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

Use this file to check and save results.
"""

import csv
import numpy as np
from datetime import datetime

def get_results(save_folder, chip_name, nets, grid):
    """" Saves results in a csv file in the given folder,
        as a file called output with date and time.
        Returns string of costs and conflicts summary.
        Conflicts are gridpoints containing 2+ nets.
        TODO yet to add actual collisions."""
    
    total_costs, wire_count, intersection_count, conflict_count = costs(nets, grid)
    
    save_results(save_folder, chip_name, nets, total_costs)
    
    return f"Costs are {total_costs}, made up of {wire_count} wirepieces and {intersection_count} intersections. Conflicts: {conflict_count}."

def costs(nets, grid):
    """ Returns total cost, number of wires, intersections and conflicts.
    """
    wire_count = count_wires(nets)
    intersection_count, conflict_count = count_intersections(grid)
    total_costs = wire_count + 300 * intersection_count
    return total_costs, wire_count, intersection_count, conflict_count

def count_wires(nets):
    """ Returns total number of wirepieces in each net """
    wire_count = 0
    for net in nets:
        wire_count += net.wire_count()
    return wire_count

def count_intersections(grid):
    """ Returns number of intersections and conflicts
        by counting gridpoint occupancy """         
    intersection_count = 0
    conflict_count = 0
    for index, coordinate_value in np.ndenumerate(grid.matrix):
        if coordinate_value != []:
            continue
        # TODO: het mag ook 3 zijn voor intersections dus conflict is niet per se collision. En lang niet elke collision wordt meegeteld
        if len(coordinate_value) == 2:
            intersection_count += 1
        elif len(coordinate_value) > 2:
            conflict_count += 1
        # TODO: echte collision count
    return intersection_count, conflict_count

def save_results(save_folder, chip_name, nets, total_costs):
    """ Creates folder name with current date and time
    """
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    result_doc = save_folder + "output_" + date_time + ".csv"

    with open(result_doc, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["connected","net","wires"])
        # TODO: verwijder net.completed uit de csv
        for net in nets:
            # TODO: kan dit makkelijker zonder spaties?
            net.wires = str(net.wires)
            net.wires = net.wires.replace(" ", "")
            connection = str(net.get_connection())
            connection = connection.replace(" ", "")
            writer.writerow([net.completed, connection, net.wires])
        writer.writerow([chip_name, total_costs])
