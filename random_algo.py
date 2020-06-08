import os

def random_algo():
    # TODO 1) pak random connectie uit netlist

    # TODO 2) pak random beginpunt van die twee gates, sla ook eindpunt op als xy coordinaat

    # TODO 3) bedenk en sla op punten: die 1 verschillen in abs(x)+abs(y)
    #           behalve: niet naar vorige punt (incl gate/startpunt zelf), bijhouden in wire_visited lijst waarin ook GATE zelf zit?
    #           alternatief: werk gelijk in nets.wires?
    #           verwijder punten die niet leeg zijn in matrix?
    #           a) KIES overgebleven WILLEKEURIG PUNT
    #           b) error, resultaat ongeldig

    # TODO 4) stukje gelegd
    #           a) wire af? -> stap 5
    #           b) volgende stukje -> stap 3

    # TODO 5) hele wire gelegd
    #           a) alle wires gemaakt? -> print resultaten naar een CSV
    #           b) volgende wire -> stap 1
