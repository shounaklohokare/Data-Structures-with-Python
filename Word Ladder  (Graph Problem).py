class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr]=weight

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([i.id for i in self.connectedTo])


class Graph:

    def __init__(self):
        self.numberOfVertices = 0
        self.vertList = {}

    def addVertex(self, key):
        self.numberOfVertices+=1
        newVertex = Vertex(key)
        self.verList[key]=newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]

        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

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

def buildGraph(wordfile):

    d = {}
    g = Graph()

    wfile = open(wordfile, 'r')

    for line in wordfile:

        word = line[:-1]

        for i in range(len(word)):

            bucket = word[:i] + '_' + word[i+1:]

            if bucket in d:
                d[bucket].append(word)

            else:
                d[bucket]=[word]


    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1, word2)

    return g