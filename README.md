# Chips-and-Circuits
Microchips, like those in your PC, consist of a circuit with connected gates. Short connections convey information swiftly and cost only little material.

In this assignment, the chips are all but finished: a circuit is provided with gates in place and the netlist specifies which gates to connect.

Our mission is to arrange the totality of nets between all connectable gates in the shortest manner possible. This results in cheap and fast chips!

## Setup
The following packages have been used to run the code and determine chip layout. For a more detailed guide on how to install these see requirements.txt.
* numpy
* matplotlib

## Usage
Run "python main.py", to generate results (with the newest version installed as per requirements.txt). This will prompt the user for specifics on which algorithm to run and what heuristics to use. After the option is selected the algorithm will run and conclude with a matplotlib visualisation
![matplotlib visualisation](/docs/visualised_chip.png).

## Files
The repository is organised into three main folders: code, data and docs. The root additionally contains the main.py file, used to run the program.

* /code  
    * /algorithms
    * /models
    * /visualisation
    * helpers.py
    * save_results.py

* /data
    * /highlighted_results
    * /input

* /docs

## Algorithms 
Several algorithms, used to determine a (optimal) wiring are implemented within this program. These can be found within code/algoritms and are selected via a prompt when running main.py.    

## Heuristics
TODO

## Visualisation
A matplotlib 3D plot will be shown at the end of a main.py run. This visualisation shall show the chip's grid with the layers being shown on the z-axis. Gates are represented as red squares and paths between gates as coloured lines.

## Team Misbaksels
Lisa Eindhoven, Sebastiaan van der Laan and Mik Schutte - as part of Programmeertheorie, Minor Programmeren aan de UvA. A special tip of the fedora to TA Quinten for challenging and helping us.

## License 
This repository has been licensed under the MIT licence. Read [LICENCE.txt](https://github.com/lisaeindhoven/chips-and-circuits/blob/master/LICENSE.txt) for the full terms and conditions.

## Project Status
As of 23-06-2020 work on this project has ended.