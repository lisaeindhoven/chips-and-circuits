"""
gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the class gates and all the functions of the class
"""
class Gate():
    def __init__(self, id, x, y):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.nets = []
        self.connections = []

        # TODO variabele om verbindingen op te slaan en voltooid weer te geven en bij te houden

    def add_connection(self, connection):
        """add a gate object to connections"""
        self.connections.append(connection)

    def add_net(self, net):
        """add a net object"""
        self.nets.append(net)

    def coordinate(self):
        """returns the (x,y) from this gate"""
        coordinate = (self.x, self.y)
        return coordinate