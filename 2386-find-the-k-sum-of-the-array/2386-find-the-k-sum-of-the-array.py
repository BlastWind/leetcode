from heapq import heappop, heappush
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # sum of positive elements
        oneSum = sum(filter(lambda x: x > 0, nums))
        # abs and sort
        nums = sorted(list(map(lambda x: abs(x), nums)))
        if k == 1: return oneSum
        pq = [(nums[0], 0)]
        results = [oneSum]
        for _ in range(k-2):
            prevSum, ind = heappop(pq)
            results.append(oneSum - prevSum)
            if ind + 1 == len(nums):
                continue
            heappush(pq, (prevSum + nums[ind + 1], ind + 1))
            heappush(pq, (prevSum + nums[ind + 1] - nums[ind], ind + 1))

        sequenceToSubtract = heappop(pq)[0]
        print(results)
        return oneSum - sequenceToSubtract


driver = Solution()
print(driver.kSum([2, 4, -2], 8))
