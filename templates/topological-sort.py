from collections import defaultdict

class Graph:
    def __init__(self):
        # Note the usage of set, sometimes list may suffice
        self.adjList = defaultdict(set)
        self.incomingLengths = defaultdict(int)

    def addEdge(self, u, v):
        if v in self.adjList[u]:
            return
        self.adjList[u].add(v)
        self.incomingLengths[v] += 1
        self.incomingLengths[u] += 0

    def topologicalSort(self):
        res = []
        if len(self.incomingLengths) == 0:
            return res
        q = []
        for node, edgesToNodeCount in self.incomingLengths.items():
            if edgesToNodeCount == 0:
                q.append(node)
        for node in q:  # The for .. in loop automatically "pops", is not memory efficient though
            res.append(node)
            for outgoing in self.adjList[node]:
                self.incomingLengths[outgoing] -= 1
                if self.incomingLengths[outgoing] == 0:
                    q.append(outgoing)
        return res

a = Graph()
a.addEdge('c', 'b')
a.addEdge('a', 'z')
print(a.adjList)
print(a.topologicalSort())
