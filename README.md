# Chips-and-Circuits
Microchips, like those in your PC, consist of a circuit with connected gates. Short connections convey information swiftly and cost only little material.

In this assignment, the chips are all but finished: a circuit is provided with gates in place and the netlist specifies which gates to connect.

Our mission is to arrange the totality of nets between all connectable gates in the shortest manner possible. This results in cheap and fast chips!

## Setup
The [requirements.txt](https://github.com/lisaeindhoven/chips-and-circuits/blob/master/requirements.txt) file contains the packages that have been used to run the code and determine chip layout. Install packages using: <br/>
`pip install -r requirements.txt`

Or by

`conda install --file requirements.txt`

## Usage
Run "python main.py", to generate results (with the newest version installed as per requirements.txt). This will prompt the user for specifics (in Dutch) on which algorithm to run and what heuristics to use. Dutch prompting was chosen due to the nationality of our supervisers. After the option is selected, the algorithm will run and conclude with a matplotlib visualisation.
![matplotlib visualisation](/docs/visualised_chip.png).

## Structure
The repository is organised into three main folders: code, data and docs. The root additionally contains the main.py file, used to run the program.

* /code: Contains all code used in this project.
    * /algorithms: Contains the random, Dijkstra, A*, downhill, Manhattan and select-net algorithms.   
    * /models: Contains the gates, grid and nets classes used to represent a chip.
    * /visualisation: Contains the code to create a 3D matplotlib visualisation.

* /data: Contains both the input as well as the generated output data.

* /docs: Contains files used to create an amazing A+ presentation.

## Algorithms 
Several algorithms, used to determine a (optimal) wiring are implemented within this program. These can be found within code/algoritms and are selected via a prompt when running main.py.    
Upon running main.py the user can choose from 7 algorithms.
1. random<br/>
    The random algorithm randomly chooses its neighbour (which step it will take) from a set of options.

2. Dijkstra<br/>
    The Dijkstra algorithm takes the costs of each neighbour in to account in determining it's path.

3. A* <br/>
    The A* algorithm, like Dijkstra also takes the costs of each neighbour in to account. Additionally, adds a heursitic cost based on the Manhattan distance between the neighbour and the end point.

4. A* AvoidGates<br/>
    Neighbours that are located near gates that isn't the paths end or begin gate have increased costs.

5. A* Skyscraper<br/>
    Costs for upward movements are decreased to stimulate paths travelling away from the ground layer where all the gates are located to minimize costs.

6. Hilldescent<br/>
    Improves upon earlier solution by removing and rebuilding individual paths. It's possible to use different algorithms for the instatiation and the rebuilding.

7. Cheap intersections<br/>
    Initially creates a solution with lower intersection costs. All nets involved in intersections are removed and rebuild by a hillclimber with the avoid gates costs.

## Visualisation
A matplotlib 3D plot will be shown at the end of a main.py run. This visualisation shall show the chip's grid with the layers being shown on the z-axis. Gates are represented as red squares and paths between gates as coloured lines.

## Team Misbaksels
Lisa Eindhoven, Sebastiaan van der Laan and Mik Schutte - as part of Programmeertheorie, Minor Programmeren aan de UvA. A special tip of the fedora to TA Quinten for challenging and helping us.

## License 
This repository has been licensed under the MIT licence. Read [LICENCE.txt](https://github.com/lisaeindhoven/chips-and-circuits/blob/master/LICENSE.txt) for the full terms and conditions.

## Project Status
As of 23-06-2020 work on this project has ended.