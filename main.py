import pandas as pd
import os

# Create test netlist

netlist_path = 'C:\\Users\\miksc\\OneDrive\\Documenten\\Study\\Minor AI\\Python Scripts\\PT\\chips-and-circuits\\Docs\\example\\netlist_1.csv'

with open(netlist_path) as f:
    netlist = pd.read_csv(f)
    print(netlist)