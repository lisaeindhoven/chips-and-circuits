import random as rnd
import copy

# TODO: prints weghalen!!
# TODO: header schrijven
# TODO: huisvesten in een class?

def random(grid, gates, nets):
    """ Header"""
    # TODO: conflict weghalen, het is nu voor ons om te kijken hoeveel paden niet volledig gemaakt zijn
    conflict = 0

    # Create a random list with all net index in nets
    random_net_ids = []
    for net in nets:
        random_net_ids.append(net.id - 1)
    rnd.shuffle(random_net_ids)

    # for every net in random order
    for random_net in random_net_ids:
        current_net = nets[random_net]

        # Get start and end coordinates
        coordinate = current_net.get_coordinates()
        start_coordinate = coordinate[0]
        end_coordinates = coordinate[1]
        current_coordinate = copy.deepcopy(start_coordinate)
        # print()
        # print(f"start {start_coordinate}, end {end_coordinates}")

        # Find paths  until no options or path is at the end gate
        while current_coordinate != end_coordinates:
            # print(f"current {current_coordinate}")

            # Find path options
            north = (current_coordinate[0], current_coordinate[1]+1, current_coordinate[2])
            south = (current_coordinate[0], current_coordinate[1]-1, current_coordinate[2])
            west = (current_coordinate[0]-1, current_coordinate[1], current_coordinate[2])
            east = (current_coordinate[0]+1, current_coordinate[1], current_coordinate[2])
            up = (current_coordinate[0], current_coordinate[1], current_coordinate[2]+1)
            down = (current_coordinate[0], current_coordinate[1], current_coordinate[2]-1)
            options = [north, south, west, east, up, down]
            rnd.shuffle(options)
            # print(f"options {options}")

            # This boolean will change if there if a path found and saved
            found_path = False

            # Check if one of the option is already the end gate
            for current_option in options:
                if not (min(current_option) < 0 or current_option[0] >= grid.x_dim or current_option[1] >= grid.y_dim or current_option[2] >= grid.z_dim):
                    item = grid.item(current_option)
                    if item == current_net.end_gate:
                        # print("One of the options is already the end gate")
                        current_net.add_wire(current_option)
                        current_coordinate = copy.deepcopy(current_option)
                        current_net.completed = True
                        found_path = True

            if not found_path:
                # Create valid path if possible
                for current_option in options:
                    # print(f"current option = {current_option}")

                    # Filter invalid options
                    if min(current_option) < 0 or current_option[0] >= grid.x_dim or current_option[1] >= grid.y_dim or current_option[2] >= grid.z_dim:
                        # print("not a valid option, next option")
                        continue
                    
                    item = grid.item(current_option)
            
                    # In this algorithm, we only add a wire if there isnt one already
                    if item == []:
                        # Add wire coordinate to net and grid
                        current_net.add_wire(current_option)
                        grid.add_wire(current_option, current_net.id)
                        # print(f"stap gezet naar {current_option}")
                        current_coordinate = copy.deepcopy(current_option)
                        found_path = True

                        # We do not need to try another option
                        break
                    
            if not found_path:
                conflict += 1
                # print("add conflict")
                break

    print(f"conflict count (not found complete path {conflict}")