from typing import List


def generate_subset_sums(nums: List[int], discardMax):
    sums = set()

    def recur(index, acc):
        if acc > discardMax: 
            return
        if index >= len(nums):
            sums.add(acc)
            return
        recur(index+1, acc)
        recur(index+1, acc+nums[index])
    recur(0, 0)
    return sums

class Solution:

    def minPatches(self, nums: List[int], n: int) -> int:
        def find_first_hole():
            for i, bool in enumerate(dp): 
                if not bool: return i
            return -1
        patchCnt = 0
        dp = [False] * (n+1) # dp[i] denotes whether or not the sum i can be formed
        sums = generate_subset_sums(nums, n)
        for acc in sums:
            dp[acc] = True

        while -1: 
            holeIndex = find_first_hole()
            print(holeIndex)
            if holeIndex == -1: return patchCnt
            
            new_sums = set()
            # add new subset_sums
            for sum in sums: 
                new_sum = holeIndex + sum
                if new_sum <= n: 
                    new_sums.add(new_sum)    
            sums = sums.union(new_sums)        
            # fill holes, previous subsets gets holeIndex set
            for i in range(len(nums) - holeIndex - 1, -1, -1):
                dp[i+holeIndex] = dp[i]
            # fill holes, subsets formed with holeIndex
            for sum in new_sums:
                dp[sum] = True


            # fill hole
            dp[holeIndex] = True

            patchCnt += 1
        return patchCnt

driver = Solution()
print(driver.minPatches([1,3], 6))
