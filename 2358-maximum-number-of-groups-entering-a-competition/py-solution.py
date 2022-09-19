from typing import List


class Solution:
	# find the largest d such that d(d+1)/2 <= len(grades)
	def maximumGroups(self, grades: List[int]) -> int:
		lo, hi = 0, len(grades) - 1
		while lo != hi:  # ends when lo >= hi, note that lo > hi can occur if hi = mid - 1 calls right before the while loop ends
			# Why use Ceiling instead of Floor?
			# in binary search, we usually use floor instead of ceiling
			# The reason we use Ceiling here is due to the lo = mid and hi = mid - 1:
			# When the search space is 2 (i.e, [0, 1])
			# lo + 1 = hi, so, if mid is calculated using floor, then, mid = lo
			# which means, so the condition of searching in the left subspace trigger, and 
			# lo = mid runs, lo is set to itself (since mid = lo)
			# And we get stuck! Conversely, we don't get stuck in the condition that searching
			# in the right subspace trigger, whether or not mid is calculated with floor or ceiling
			# because hi is moved beyond mid with an extra -1
			mid = (lo + hi + 1) // 2  
			if (mid * (mid + 1)) / 2 <= len(grades):
				lo = mid  # don't move beyond mid, since mid can satisfy constraint
			else:
				hi = mid - 1  # move beyond mid since mid can't satisfy constraint

		# There is no difference between returning lo or hi
		# since the while loop always ends when lo == hi
		return lo


a = Solution()
print(a.maximumGroups([0, 0]))
# 0, 1, 3, 6, 10, 15, 21, 28
# 0, 1, 2, 3,  4,  5,  6,  7

# Say that we are in interval [2, 3] and the length appears to be
