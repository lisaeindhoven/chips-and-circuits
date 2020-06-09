import csv
import numpy as np

def get_results(nets, grid):
    wire_count = 0
    intersection_count = 0

    # Check nets and add wires
    for net in nets:
        wire_count += (len(net.wires) - 1)

    # Check grid matrix for intersections           
    for index, coordinate_value in np.ndenumerate(grid.matrix):
        if coordinate_value != []:
            continue

        # TODO: hier kan wire count worden gebruikt
        if len(coordinate_value) == 2:
            intersection_count += 1
        elif len(coordinate_value) > 2:
            print("CONFLIFT op", index) 

    # Count total costs
    total_costs = wire_count + 300 * intersection_count
    
    # TODO: create for each experiment a file and different result files
    result_doc = "Docs/Results/Random/output.csv"
    with open(result_doc, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["net", "wires"])
        for net in nets:
            writer.writerow([net.get_connection(), net.wires])
        # TODO: change name chip
        writer.writerow(["NAME CHIP", total_costs])

        
    return total_costs