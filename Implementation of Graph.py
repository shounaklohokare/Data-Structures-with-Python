from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

class Node:

    def __init__(self, num):
        self.num = num
        self.currentState = State.unvisited
        self.adjacent = OrderedDict()

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()

    def addNode(self, num):
        node = Node(num)
        self.nodes[num]=node
        return node

    def getNode(self, num):
        if num in self.nodes:
            return self.nodes[num]

        else:
            return None

    def addEdge(self, source, dest, weight=0):
        if source not in self.nodes:
            nv = self.addNode(source)

        if dest not in self.nodes:
            nv = self.addNode(dest)

        self.nodes[source].adjacent[self.nodes[dest]]=weight