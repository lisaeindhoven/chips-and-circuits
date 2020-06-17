"""
gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the class gates and all the functions of the class
"""
class Gate():
    # header
    def __init__(self, id, x, y):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.z = 0
        self.nets = []
        self.connections = []
        self.wires = {}

        # TODO variabele om verbindingen op te slaan en voltooid weer te geven en bij te houden

    def add_connection(self, connection):
        """add a gate object to connections"""
        self.connections.append(connection)

    def add_net(self, net):
        """add a net object"""
        self.nets.append(net)

    def coordinate(self):
        """returns the (x,y, z) from this gate"""
        coordinate = (self.x, self.y, self.z)
        return coordinate