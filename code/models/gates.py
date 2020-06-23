"""
gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Lisa Eindhoven, Sebastiaan van der Laan & Mik Schutte

This file contains the class gates and all the functions of the class
"""
class Gate():
    """ Class containing gate object used to fill a grid and
        provide information on where gates lie.
    """
    def __init__(self, id, x, y):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.z = 0
        self.nets = []
        self.connections = []
        self.wires = {}

    def add_connection(self, connection):
        """ Add a gate object to the connections.
        """
        self.connections.append(connection)

    def add_net(self, net):
        """ Add a net object.
        """
        self.nets.append(net)

    def coordinate(self):
        """ Returns the (x,y,z) coordinates from this gate.
        """
        coordinate = (self.x, self.y, self.z)
        return coordinate

    def reset_wires(self, net):
        """ Remove the wires from the net and grid.
        """
        self.wires[net] = []