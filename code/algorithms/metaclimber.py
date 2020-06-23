"""
metaclimber.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

contains intelligent hillclimbing tools
"""


import copy

from code.algorithms.a_star import A_star
from code.helpers import get_gates, get_nets, get_paths, uncompleted_nets, create_bigpath, scary_gates, reset_net
from code.results import costs, list_intersections, conflict_analysis, count_intersections
from code.algorithms.select_net import get_min_freedom_net
from code.visualisation.visualiser import visualiser 

# METACLIMBER WORDT AANGESTUURD VANUIT MAIN
# MAIN HEEFT DE INTERFACE EN ROEPT METACLIMBER AAN MET BEPAALDE INPUT

# PSEUDOCODE:
# 1 INPUT LADEN EN LEGE DINGEN GENEREREN # of in main doen?
# 2 EERSTE RUN MET ? CONSTRAINTS
# 3 PADEN VERWIJDEREN DIE ?
# 4 PADEN HERLEGGEN MET ? CONSTRAINTS
# ????
# 99 LOOP: 
# VERWIJDER DUURSTE PAD
# LEG OVERGEBLEVEN PADEN

class Metaclimber:
    """ 
    The Metaclimber class creates chip circuitry in multiple steps 
    by generating suboptimal results and gradually improving upon them.
    """
    # load input data and keep track of best value
    def __init__(self, grid, nets):
        self.grid = grid
        self.nets = nets
        self.best_value =  costs(nets, grid)
        # self.initialize_variables()

    # main function om stapsgewijs te runnen en descenden
    def execute(self):
        """ executes metaclimber x number of times or until there's no more improvement
        """
        # PSEUDOCODE:
        # 1 INPUT LADEN EN LEGE DINGEN GENEREREN
        # 2 EERSTE RUN MET ? CONSTRAINTS
        # 3 PADEN VERWIJDEREN DIE ?
        # 4 PADEN HERLEGGEN MET ? CONSTRAINTS
        # ????
        # 99 LOOP: 
        # VERWIJDER DUURSTE PAD
        # LEG OVERGEBLEVEN PADEN

    # run a pathfinding algorithm
    # with(out) 1) net selection 2) different constraints
    def run(self):
        pass
    # select criterium to erase path /// use nets.reset_wires with helpers.conflict_analysis or 
    def hilldescent(grid, nets, scary_dict, gates):
        """ Descents towards new lows!
            Rebuilds nets one at a time.
            Uncomment for a score check to keep new or reset old path,
            but our A-star never delivers a worse result!
            Conservatives change line 80 ">" into ">=" """  
        for net in nets:
            # temp_grid = copy.deepcopy(grid)
            # temp_nets = copy.deepcopy(nets)
            # old_costs, y, z = costs(nets, grid)
            # print(f"Old costs: {old_costs}")
            reset_net(grid, net)
            a_star = A_star(grid, net, scary_dict)
            a_star.search()
            # new_costs, y, z = costs(nets, grid)
            # print(f"New costs: {new_costs}")
            # if new_costs > old_costs:
            #     grid = copy.deepcopy(temp_grid)
            #     nets = copy.deepcopy(temp_nets)
        return grid, nets

    def conflict_remover(grid, nets):
        """ Removes conflicting nets and returns a list of nets to rebuild """ 
        removed_nets = []
        while True:
            intersections = count_intersections(grid)
            if intersections:        
                problem_nets, rivals, worst_net_id = conflict_analysis(grid, nets)
                for net in nets:
                    if net.id == worst_net_id:
                        removed_nets.append(net)
                        worst_net = net
                reset_net(grid, worst_net)
            break
        return removed_nets
    
if __name__ == "__main__":

    meta = Metaclimber()