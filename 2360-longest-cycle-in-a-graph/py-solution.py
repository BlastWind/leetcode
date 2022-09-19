from typing import List


class Solution:
	def longestCycle(self, edges: List[int]) -> int:
		# naive solution: start from each node, travel n times, if starting node traversed again, upudate maxLen
		# what's bad about naive: nodes are often repeating paths.

		# insight: Two different cycles will never share the same node, since
		# each node has at most one outgoing edge
		# This also means: if a node is not in one cycle, it won't be in any cycle

		# This means, if I were to mark a node or cycle as "visited", then,
		# they can stay that way

		# better solution: traverse nodes, keep a dist and mark them visited
		# if we come across visited node, start at any unvisited node
		# if we come across the same node, update longest cycle len with dist
		def dfs(node, dist, traversed, edges):
			if node == -1 or edges[node] == -1:
				return -1
			if node in traversed and dist > 0:
				return dist - traversed[node]
			# mark visited
			temp = edges[node]
			traversed[node] = dist
			return dfs(temp, dist + 1, traversed, edges)

		longest = -1
		for i in range(len(edges)):
			if edges[i] != -1:  # not yet visited
				traversed = {}
				longest = max(longest, dfs(i, 0, traversed, edges))
				for i in traversed: # only set to not visited at the very end
					edges[i] = -1

		return longest

a = Solution()
print(a.longestCycle([3, 3, 4, 2, 3]))