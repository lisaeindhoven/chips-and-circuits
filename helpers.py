import csv

def get_gates_coordinates():
    """returns a dictionary with the coordinates of the gates"""
    gates_csv_path = "Docs\example\print_0.csv"

    with open(gates_csv_path, mode='r') as f:
        reader = csv.reader(f)
        gates = {}
        for row in reader:
            gates[row[0]] = row[1] + "," + row[2]
        gates.pop("chip")
        
    return gates