
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id) + ' ConnectedTo: ' + str([i.id for i in self.connectedTo])

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numberOfVertices = 0

    def addVertex(self, key):
        self.numberOfVertices+=1

        newVertex = Vertex(key)
        self.vertList[key]=newVertex

        return newVertex


    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]

        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

