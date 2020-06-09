import random, copy

def random_algo(grid, gates, nets):
    """ Header"""
    # Get a random connection from the netlist
    nets_copy = copy.deepcopy(nets)
    random.shuffle(nets_copy)
    conflict = 0
    while nets_copy:
        current_net = nets_copy.pop()
        coordinate = current_net.get_coordinates()
        
        # Randomize begin and end
        # Coordinate[0] = x, [1] = y
        random.shuffle(coordinate)
        print(coordinate)
        start_coordinate = coordinate.pop()
        goal_coordinate = coordinate.pop()
        current_coordinate = copy.deepcopy(start_coordinate)
        print(f"start_coordinate: {start_coordinate}")
        print(f"goal_coordinate: {goal_coordinate}")
        #TODO start&goal boven de while / current in een nieuwe while

        

    # TODO 3) bedenk en sla op punten: die 1 verschillen in abs(x)+abs(y)
    #           behalve: niet naar vorige punt (incl gate/startpunt zelf), bijhouden in wire_visited lijst waarin ook GATE zelf zit?
    #           alternatief: werk gelijk in nets.wires?
    #           verwijder punten die niet leeg zijn in matrix?
    #           a) KIES overgebleven WILLEKEURIG PUNT
    #           b) error, resultaat ongeldig
        while current_coordinate != goal_coordinate:    
            north = (current_coordinate[0], current_coordinate[1]+1)
            south = (current_coordinate[0], current_coordinate[1]-1)
            west = (current_coordinate[0]-1, current_coordinate[1])
            east = (current_coordinate[0]+1, current_coordinate[1])
            options = [north, south, west, east]
            random.shuffle(options)

            while len(options) > 0:
                print(options)
                current_option = options.pop()
                print(f"current option = {current_option}")
                # if current_option
                try: 
                    item = grid.item(current_option)
                    print(f"try: {item}")
                    print(if item == [])
                    if item and item == []:
                        # TODO: wat gebeurd er als options leeg is
                        current_net.add_wire(current_option)
                        print(f"current {current_coordinate}")
                        print(f"goal {goal_coordinate}")
                        if current_option != goal_coordinate:
                            print("hier")
                            grid.add_wire(current_option, current_net)
                            print(grid.show_matrix())
                        current_coordinate = copy.deepcopy(current_option)
                        print(f"stap gezet naar {current_coordinate}")
                        break
                except:
                    print("except")

                # TODO: kijken of er omheen al het eindpunt zit
            # TODO: wat gebeurd er als options leeg is en we niet opnieuw naar while current_coordinate 
            conflict += 1
            break
            

                

        # TODO 4) stukje gelegd
        #           a) wire af? -> stap 5
        #           b) volgende stukje -> stap 3

        # TODO 5) hele wire gelegd
        #           a) alle wires gemaakt? -> print resultaten naar een CSV
        #           b) volgende wire -> stap 1
