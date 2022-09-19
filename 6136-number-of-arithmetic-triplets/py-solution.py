# boils down to subtracting (from small to pos) and finding when it is diff
from typing import List


# could use binary search to speed up?
class Solution:
	def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
		hash = {}
		ans = 0
		for num in nums: 
			hash[num] = 1 # just putting in the key "num", the value '1' has no significance
		for i in range(len(nums)): 
			for j in range(i): 
				if nums[i] + diff in hash and nums[j] + diff == nums[i]: 
					print(j, i)
					ans = ans + 1
					break
		return ans

a = Solution() 
a.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3)