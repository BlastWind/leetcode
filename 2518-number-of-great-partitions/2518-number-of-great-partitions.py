from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # find the number of subset < k
        # dp[0] ~ dp[k - 1]
        if sum(nums) < 2 * k: return 0
        n = len(nums)
        total = 2 ** n
        MOD = 10 ** 9 + 7 
        dp = [[0] * k for _ in range(n + 1)]
        
        #base case, the single, empty subset always sums up to 0
        for i in range(n + 1):
            dp[i][0] = 1    

        # dp[i][j] = # of subsets from the first i-elements that can sum up to j.
        # so, the sum of the last row, dp[n-1], includes all of the subsets that has a sum of less than k 
        
        # build the table
        for i in range(1, n+1): # want n at the end since this is by length, not index
            for j in range(1, k): # don't want k itself, since we're finding subset sums less than k
                if j - nums[i-1] >= 0: 
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else: # no way to include current, so just maintain the count
                    dp[i][j] = dp[i-1][j]


        return (total - sum(dp[-1]) * 2) % MOD

        # the first 5 elements have 3 subsets that sums up to 5. The 5th element is 5.
        # we know this from 1) the first 4 elements have 2 subsets that sums up to 5
            # well, these subsets can stay the same and still sum up to 5.
        # the 5th element is 5, the first 4 elements has 1 subset that sums up to 0
            # these subsets, when the 5th element is included, will get the desired sum.



driver = Solution()
print(driver.countPartitions([1, 2, 3, 4, 5], 7))
