from typing import List


class Solution:
	def validPartition(self, nums: List[int]) -> bool:
		dp = [False] * (len(nums) + 1)
		dp[0] = True 
		for i in range(len(nums)): 
			if not dp[i]: continue
			if i + 2 <= len(nums) and nums[i] == nums[i+1]:
				dp[i+2] = True 
			if i + 3 <= len(nums): 
				if nums[i] == nums[i+1] == nums[i+2] or nums[i] == nums[i+1] - 1 and nums[i+1] + 1 == nums[i+2]:
					dp[i+3] = True
		return dp[len(nums)]			  


# dp[i] represents arr[0:i] is a valid partition, note that [:i] does not inclusde i 
# so, dp[len(nums)] represents that arr[0:len(nums)] is a valid partition.
a = Solution()
print(a.validPartition([4, 4, 4, 5, 6]))