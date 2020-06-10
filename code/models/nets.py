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
        """ Return tuple of the connected gate ids"""
        return (self.begin_gate.id, self.end_gate.id)

    def add_wire(self, coordinate):
        """ Add new coordinate to the route"""
        self.wires.append(coordinate)

    def wire_count(self):
        """ Return the amount of units for this net"""
        return len(self.wires) - 1

    def get_coordinates(self):
        """ Return coordinates from begin and end gate"""
        return [self.begin_gate.coordinate(), self.end_gate.coordinate()]

