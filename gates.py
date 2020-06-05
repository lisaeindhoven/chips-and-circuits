"""
gates.py

Minor Programmeren, Programmeertheorie, Chips & Circuits
Misbaksels: Mik Schutte, Sebastiaan van der Laan & Lisa Eindhoven

This file contains the class gates and all the functions of the class
"""
class Gate():
    def __init__(self, x, y):
        self.x = x
        self.y = x
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

# TODO: functie die connecties maakt
# TODO: functies maken die bijvoorbeeld coordinaten teruggeeft of de connections