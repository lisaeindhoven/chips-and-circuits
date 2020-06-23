"""
algo_helpers.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

These functions are essential to our more complex algorithms.
"""
from code.results import count_intersections, conflict_analysis
from code.helpers import reset_net
from code.algorithms.a_star import A_star

def hilldescent(grid, nets, scary_dict, gates):
    """ Rebuilds nets one at a time using A*.
        No comparison needed because A* always delivers!
        Returns updates grid and nets
    """  
    for net in nets:
        reset_net(grid, net)
        a_star = A_star(grid, net, scary_dict)
        a_star.search()

def conflict_remover(grid, nets):
    """ Removes conflicting nets and returns a list of nets to rebuild.
    """ 
    removed_nets = []
    intersections = count_intersections(grid)
    if intersections:        
        problem_nets = conflict_analysis(grid, nets)
        # Remove repeated nets
        problem_nets = list(dict.fromkeys(problem_nets))

        # Reset the nets
        for net in problem_nets:
            removed_nets.append(net)
            reset_net(grid, net)
    return removed_nets
