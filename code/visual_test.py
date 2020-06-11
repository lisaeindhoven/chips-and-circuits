# import IPython
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from code.helpers import *

# Specify what gate and what nets csv file to take
gate_coordinates_csv_path = "docs/example/print_0.csv"
gate_connections_csv_path = "docs/example/netlist_1.csv"

# Get gates and nets list with all the gates and nets
gates, nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

# Create a matrix of the grid with all the gates
grid = Grid(gates)

path = [(1,5,0),(2,5,0),(3,5,0),(3,5,1),(4,5,1),(4,5,0),(5,5,0),(6,5,0)]


# RUN
visualizer(grid, gates, paths)
