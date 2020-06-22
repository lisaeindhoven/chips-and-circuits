"""
metaclimber.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

contains intelligent hillclimbing tools
"""


import copy

from code.algorithms.a_star import A_star
from code.helpers import reset_net
from code.results import costs, list_intersections, conflict_analysis, count_intersections
from code.algorithms.select_net import get_min_freedom_net

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

    # def initialize_variables(self):
    #     print("Welkom")

    #     # Specify what gate and what nets csv file to take
    #     self.chip = int(input("Kies de chip (0, 1 of 2): "))
    #     gate_coordinates_csv_path = f"data/input/gates&netlists/chip_{self.chip}/print_{self.chip}.csv"
    #     self.netlist = int(input("Kies de netlist(1, 2 of 3): ")) + 3 * self.chip
    #     gate_connections_csv_path = f"data/input/gates&netlists/chip_{self.chip}/netlist_{str(self.netlist)}.csv"
        
    #     # Get gates and nets list with all the gates and nets
    #     self.gates, self.nets = get_gates_and_nets(gate_coordinates_csv_path, gate_connections_csv_path)

    #     # Create a matrix of the grid with all the gates
    #     self.grid = Grid(self.gates)

    # algorithm_dict = {
    #     "1": "random",
    #     "2": "dijkstra",
    #     "3": "astar",
    #     "4": "scary_astar"
    # }

    # net_select_dict = {
    #     "1": "Net met minste extra vrijheid rond de gate",
    #     "2": "Net met minste manhattan distance eerst",
    #     "3": "Net met meeste manhattan distance eerst"
    # }

    # # Choose and run algorithm
    # algorithm = int(input("Kies het nummer van de algorithme (1, 2, 3 of 4) of 0 voor meer informatie: "))
    # if algorithm == 0:
    #     print(algorithm_dict)
    #     algorithm = int(input("Kies het nummer van de algorithme (1, 2, 3 of 4): "))
        
    #         while uncompleted:
    #             # Get the right net
    #             if select_net == 1:
    #                 net_id = get_min_freedom_net(gates, grid)
    #             elif select_net == 2:
    #                 net_id = get_min_manhattan_net(nets)
    #             elif select_net == 3:
    #                 net_id = get_max_manhattan_net(nets)

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
    def hilldescent(grid, nets):
        """ descents towards new lows!
            rebuilds nets and keeps the score if it improves """
        grid = grid
        nets = nets  
        
        
        # Try to improve each net
        for net in nets:
            temp_grid = copy.deepcopy(grid)
            temp_nets = copy.deepcopy(nets)
            old_costs, y, z = costs(nets, grid)
            print(f"old costs {old_costs}")
            reset_net(grid, net)
            a_star = A_star(grid, net)
            a_star.search()
            new_costs, y, z = costs(nets, grid)
            print(f"new costs: {new_costs}")
            if new_costs > old_costs:
                grid = temp_grid
                nets = temp_nets

        return grid, nets
            # # new_costs, y, z = costs(nets, grid)
            # print(net.wires)
            # print(temp_net.wires)
            # print(new_costs)
            # print(old_costs)
            # if new_costs > old_costs:
            #     print("no luck")
            #     net = temp_net
            #     grid = temp_grid
            # elif new_costs == old_costs: 
            #     print("Tie. Wire replaced.")
            # else:
            #     x = old_costs - new_costs
            #     old_costs = new_costs
            #     print(f"Improvement! Costs decreased by {x}! ")    


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
                reset_net(grid, worst_net) # geeft worst_net id mee, moet misschien object zijn?
            break
        return removed_nets
    
if __name__ == "__main__":

    meta = Metaclimber()
