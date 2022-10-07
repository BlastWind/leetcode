# Cleanest and fastest
# Doesn't directly use kadane, but uses a similar hacky speedup
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596/Any-Accepted-Python-Solution/87892

import bisect

class Solution:
	def maxSumSubmatrix(self, matrix, k):
		def maxSumSublist(vals):
			maxSum = float('-inf')
			prefixSum = 0
			prefixSums = [float('inf')]
			for val in vals:
				bisect.insort(prefixSums, prefixSum)
				prefixSum += val
				i = bisect.bisect_left(prefixSums, prefixSum - k)
				maxSum = max(maxSum, prefixSum - prefixSums[i])
			return maxSum
		maxSum = float('-inf')
		columns = list(zip(*matrix))
		for left in range(len(columns)):
			rowSums = [0] * len(matrix)
			for column in columns[left:]:
				rowSums = list(map(int.__add__, rowSums, column))
				maxSum = max(maxSum, maxSumSublist(rowSums))
		return maxSum

Solution().maxSumSubmatrix([[1,0,1],[0,-2,3]], 2)
