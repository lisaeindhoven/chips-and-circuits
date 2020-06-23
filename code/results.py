"""
results.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

Use this file to check and save results.
"""
import csv, os, errno, functools, random
import numpy as np
from datetime import datetime
from collections import defaultdict

def get_results(save_folder, chip_name, nets, grid):
    """ Saves results in a csv file in the given folder,
        as a file called output with date and time.
        Returns a nice f-string of costs.
    """
    total_costs, wire_count, intersection_count = costs(nets, grid)
    save_results(save_folder, chip_name, nets, total_costs)

    # Check if collision on grid
    if grid.collision is False:
        return f"Kosten zijn {total_costs}, voortkomend uit {wire_count} draad-eenheden en {intersection_count} intersections."
    else:
        return f"Een collision is gemaakt, het algorithme heeft gefaald."

def costs(nets, grid):
    """ Returns total cost, number of wires and intersections.
    """
    wire_count = count_wires(nets)
    intersection_count = count_intersections(grid)
    total_costs = wire_count + 300 * intersection_count
    return total_costs, wire_count, intersection_count

def count_wires(nets):
    """ Returns the total number of wirepieces in each net. 
    """
    wire_count = 0
    for net in nets:
        wire_count += net.wire_count()
    return wire_count

def count_intersections(grid):
    """ Returns number of intersections by counting gridpoint occupancy.
        Index denotes grid position, content is either a gate, 
        an empty list or a list of net(s).
    """         
    intersection_count = 0
    for index, content in np.ndenumerate(grid.matrix):
        if (isinstance(content, list) and len(content) > 1):
            intersection_count +=1
    return intersection_count

def conflict_analysis(grid, nets):
    """ Returns two dictionaries and the key with highest problem_nets value.
        problem_nets: {net: int}
        rivals: {net: [rival net, rival net]}
    """
    #TODO Header beter toelichten, wat zijn problem_nets en rivals?
    intersections = list_intersections(grid)

    # For each problematic net we track conflicts and their rivals
    problem_nets = []

    # Add both conflicting nets to the dictionary
    for intersection in intersections:
        problem_nets.append(intersection[0])
        problem_nets.append(intersection[1])
    return problem_nets

def list_intersections(grid):
    """ Returns a list with lists of two nets that intersect.
    """
    intersections = []
    for index, content in np.ndenumerate(grid.matrix):
        if (isinstance(content, list) and len(content) > 1):
            occupants = []
            for net in content:
                occupants.append(net)
            intersections.append(occupants)
    return intersections

def save_results(save_folder, chip_name, nets, total_costs):
    """ Creates folder name with current date and time.
    """
    # Get the current date and time for the file name
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    result_doc = save_folder + "output_" + date_time + ".csv"

    # Create folder if it doesn't exist yet
    try:
        os.makedirs(save_folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Create the results csv
    with open(result_doc, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["net","wires"])

        # For check50 the csv can't handle spaces, so filter the spaces
        for net in nets:
            net.wires = str(net.wires)
            net.wires = net.wires.replace(" ", "")
            connection = str(net.get_connection())
            connection = connection.replace(" ", "")
            writer.writerow([connection, net.wires])
        writer.writerow([chip_name, total_costs])