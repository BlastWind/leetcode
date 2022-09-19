from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallestSubsequenceSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        heap = [(nums[0], 0)]
        sums = []
        for _ in range(k):
            last, lastInd = heappop(heap)
            sums.append(last)
            if lastInd + 1 == len(nums):
                continue
            heappush(heap, (last + nums[lastInd + 1], lastInd + 1))
            heappush(
                heap, (last + nums[lastInd + 1] - nums[lastInd], lastInd + 1))
        print(sums)
        return heappop(heap)[0]


driver = Solution()
print(driver.kthSmallestSubsequenceSum([3, 3, 5, 5], 7))
# assert(driver.kthSmallestSubarraySum([2, 1, 3], 4) == 3)
