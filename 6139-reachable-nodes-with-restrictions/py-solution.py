# how to check if there's an edge from node a to b?
# I think building adjacency list the cleanest

import collections
from typing import List


class Solution:
	def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
		adjList = [[] for _ in range(n)]
		for edge in edges: 
			adjList[edge[0]].append(edge[1])
			adjList[edge[1]].append(edge[0])
		visited = {} # golden nugget
		visited[node] = 1
		queue = collections.deque()
		queue.append(0)
		ans = 0
		while len(queue) > 0:
			node = queue.popleft()
			ans = ans + 1
			visited.append(node) 
			for neighbor in adjList: 
				if neighbor not in visited: 
					queue.append(neighbor)
		return ans
a = Solution()
print(a.reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]],[4,5] ))