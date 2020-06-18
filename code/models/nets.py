"""
nets.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the class nets and all the functions of the class
"""
class Nets():
    def __init__(self, id, begin_gate, end_gate):
        self.id = id
        self.begin_gate = begin_gate
        self.end_gate = end_gate
        self.wires = []
        self.completed = False

        self.wires.append(begin_gate.coordinate())

    def get_connection(self):
        """ Return tuple of the connected gate ids """
        return (self.begin_gate.id, self.end_gate.id)

    def add_wire(self, coordinate):
        """ Add new coordinate to the route """
        self.wires.append(coordinate)

    def wire_count(self):
        """ Return the amount of units for this net """
        return len(self.wires) - 1

    def get_coordinates(self):
        """ Return coordinates from begin and end gate """
        return [self.begin_gate.coordinate(), self.end_gate.coordinate()]

    # def reset_wires(self, grid):
    #     """ Remove the wires in the net and grid """
    #     print(self.wires)
    #     print(tuple(self.end_gate.coordinate()))
    #     self.wires = self.wires[0].remove((self.end_gate.coordinate()))
    #     print(self.wires)
    #     while len(self.wires) > 1:
    #         coordinate = self.wires[-1]
    #         self.wires = self.wires[:-1]
    #         grid.delete_net(coordinate, self.id)

        # TODO: verwijder uit de wires en dan ook gelijk op de grid


