"""
nets.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file holds nets with all data and functions essential to a good net.
"""
class Nets():
    """ Class containing nets object used to fill a grid and
        provide information on where paths lie.
    """
    def __init__(self, id, begin_gate, end_gate):
        self.id = id
        self.begin_gate = begin_gate
        self.end_gate = end_gate
        self.wires = []
        self.completed = False
        self.wires.append(self.begin_gate.coordinate())

    def get_connection(self):
        """ Return tuple of the connected gate ids.
        """
        return (self.begin_gate.id, self.end_gate.id)

    def add_wire(self, coordinate):
        """ Add new coordinate to the net.wires path. 
        """
        self.wires.append(tuple(coordinate))

    def wire_count(self):
        """ Return the amount of wire-units for this net.
        """
        return len(self.wires) - 1

    def get_coordinates(self):
        """ Return the begin and end gate coordinates.
        """
        return [self.begin_gate.coordinate(), self.end_gate.coordinate()]

    def reset_wires(self):
        """ Remove the wires from the net and grid.
        """
        self.wires = []
        self.wires.append(self.begin_gate.coordinate())
        self.completed = False
