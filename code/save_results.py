import csv
import numpy as np
from datetime import datetime

def get_results(save_folder, chip_name, nets, grid):
    """"Save the results in a csv file in the given folder,
    as a file called output with the date and time.
    Returns a string with the total costs and conflicts.
    Conflicts are faults in the results, like more a collision or two wires on one path. """

    wire_count = 0
    intersection_count = 0
    conflict_count = 0

    # Check nets and add wires
    for net in nets:
        wire_count += net.wire_count()

    # Check grid matrix for intersections           
    for index, coordinate_value in np.ndenumerate(grid.matrix):
        if coordinate_value != []:
            continue

        if len(coordinate_value) == 2:
            intersection_count += 1
        # TODO: deze weghalen bij het officieel inleveren, dit is alleen voor onze check dat we zien dat er iets fout gaat
        elif len(coordinate_value) > 2:
            conflict_count += 1
        # TODO: misschien nog testen op dat geen verbinding twee keer wordt gebruikt

    # Count total costs
    total_costs = wire_count + 300 * intersection_count
    
    # Create folder name with current date and time
    now = datetime.now()
    date_time = now.strftime("%m.%d.%Y_%H.%M.%S")
    result_doc = save_folder + "output_" + date_time + ".csv"

    # Create new csv file and write it
    with open(result_doc, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["connected","net","wires"])
        # TODO: coordinaten worden nu met spaties gegeven, check50 vind dit niet okay
        # TODO: verwijder net.completed uit de csv
        for net in nets:
            # TODO: kan dit makkelijker zonder spaties?
            net.wires = str(net.wires)
            net.wires = net.wires.replace(" ", "")
            connection = str(net.get_connection())
            connection = connection.replace(" ", "")
            writer.writerow([net.completed, connection, net.wires])
        writer.writerow([chip_name, total_costs])

    return f"Total costs: {total_costs}. Total conflicts: {conflict_count}"