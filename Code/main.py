"""
main.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file is the main python file
  
from code.classes import graph, transmitters

from code.algorithms import randomize
from code.algorithms import greedy as gr
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
from code.algorithms import hillclimber as hc
from code.code.algorithms import simulatedannealing as sa

import numpy as np

from helpers import *
from save_results import *
from algorithms.random import *
# TODO: dit allemaal in if main = main gebeuren?

# TODO: maak de map voor resultaten anders per ander algoritme door keuzemenu
# Get results and create csv file
save_folder = "Docs/Results/Random/"
# TODO: de chipnaam moet veranderd worden aan de variabele die bij de gate en nets geimporteerd wordden
chip_name = "chip_0_net_1"
print(get_results(save_folder, chip_name, nets, grid))

