from typing import List


class Solution:
	def dfs(self, node, dist,  edges, memo):
		if node != -1 and memo[node] == -1: # node is traversable into and not yet visited
			memo[node] = dist 
			self.dfs(edges[node], dist + 1, edges, memo)
	def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
		m1 = [-1] * len(edges) # begin unvisited
		m2 = [-1] * len(edges) 
		self.dfs(node1, 0, edges, m1)
		self.dfs(node2, 0, edges, m2)
		minDist = 100000
		minNode = -1
		for i in range(len(edges)):
			if min(m1[i], m2[i]) >= 0 and max(m1[i], m2[i]) < minDist:
				minDist = max(m1[i], m2[i])
				minNode = i
		return minNode

a = Solution()

print(a.closestMeetingNode([1, 2, 0], 0, 2))  # expect 2
