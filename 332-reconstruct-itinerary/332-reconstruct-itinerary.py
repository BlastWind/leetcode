from collections import defaultdict, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # construct departure nodes that store destinations
        adj = defaultdict(list)
        temp = defaultdict(list)
        for depart, arrive in tickets: 
            temp[depart].append(arrive)
        for l in temp: 
            adj[l] = list(sorted(temp[l]))

        # observation: iterinery should have len = len(tickets) + 1

        # if reached dead end yet iterinery is not desired len, backtrack.

        iterinary = ['JFK']

        def recur(depart):
            if len(adj[depart]) == 0 and len(iterinary) == len(tickets) + 1: 
                return True
            for i in range(len(adj[depart])): 
                arrive = adj[depart][i]
                iterinary.append(arrive)
                adj[depart] = adj[depart][:i] + adj[depart][i+1:] # remove at i 
                if recur(arrive): return True
                iterinary.pop()
                adj[depart] = adj[depart][:i] + [arrive] +  adj[depart][i:]# insert at i
                if not (all(adj[depart][i] <= adj[depart][i+1] for i in range(len(adj[depart]) - 1))): 
                    print(adj[depart])
                    print("NO")

        recur("JFK")

        return iterinary


    def findItinerary2(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
driver = Solution()
print(driver.findItinerary2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))