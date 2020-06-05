"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
"""
import os

from helpers import *

# Get a dictionary with gate names, coordinates and connections
gates = get_gates()
print(gates[0].x_coordinate)