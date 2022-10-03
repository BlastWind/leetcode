
from typing import List


class Solution:

    def minPatches(self, nums: List[int], n: int) -> int:
        cover = 0 # covered up to
        numIndex = 0
        patchCnt = 0
        while cover < n: 
            miss = cover + 1 # first number missing
            if numIndex < len(nums) and nums[numIndex] <= miss: 
                cover += nums[numIndex]
                numIndex += 1
            else: 
                cover += miss 
                patchCnt += 1
        return patchCnt

s = Solution()
print(s.minPatches([1, 3], 6))