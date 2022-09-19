from typing import List


class Solution:
	def edgeScore(self, edges: List[int]) -> int:
		# Convert to adjency list. 
		# Simply add up and find max 
		scores = [0] * len(edges) 
		for i in range(len(edges)):
			pointTo = edges[i]
			scores[pointTo] += i

		return scores.index(max(scores))