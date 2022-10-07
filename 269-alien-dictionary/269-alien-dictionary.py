from collections import defaultdict
from itertools import chain
from typing import List


class Graph:
    def __init__(self):
        # Note the usage of set, sometimes list may suffice
        self.adjList = defaultdict(set)
        self.incomingLengths = defaultdict(int)

    def addEdge(self, u, v):
        if v in self.adjList[u]: return
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

def isSuffixOf(a: str, b: str) -> bool: # is a is strict substring of b
    if len(a) >= len(b): return False
    for i in range(len(a)):
        if a[i] != b[i]: return False 
    return True

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Error if any suffixes come before the prefixes
        acc = set()
        for word in reversed(words): 
            for prev in acc: 
                if isSuffixOf(prev, word): 
                    print(word, prev)
                    return ""
            acc.add(word)

        # Error if some same prefix is detected but separated
        acc = {}
        for i in range(len(words)): 
            if words[i][0] in acc and i - acc[words[i][0]] > 1: return "" 
            acc[words[i][0]] = i

        graph = Graph()
        letters = set([letter for word in words for letter in word])

        for i in range(1, len(words)):
            prevWord, curWord = words[i-1], words[i]
            # find first different letter
            for j in range(min(len(prevWord), len(curWord))):
                prevLetter, curLetter = prevWord[j], curWord[j]
                if prevLetter != curLetter: 
                    # Say a:b is in graph, we can't add b:a
                    if (curLetter in graph.adjList): 
                        if prevLetter in graph.adjList[curLetter]:
                            return ""
                    graph.addEdge(prevLetter, curLetter)
                    break 

        unused = letters.difference(graph.incomingLengths.keys())
        res = graph.topologicalSort()
        return ''.join(unused) + ''.join(res)


# print(Solution().alienOrder(["baa", "bbc", "aba"]))
print(Solution().alienOrder(["ac","ab","zc","zb"]))

