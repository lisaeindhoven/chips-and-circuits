"""
helpers.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the helper function for main.py
"""
import csv

from gates import *

def get_gates():
    """returns a dictionary with the gate number, coordinate and connected gates"""
    gate_coordinates_csv_path = "Docs\example\print_0.csv"
    gate_connections_csv_path = "Docs\example\netlist_1.csv"

    # Get coordinates
    with open(gate_coordinates_csv_path, mode='r') as f:
        reader = csv.reader(f)
        gates = []
        for row in reader:
            if row[0] != "chip":
                gate = Gate(row[1], row[2])
                gates.append(gate)

    return gates