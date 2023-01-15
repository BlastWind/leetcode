# greedy: Always increase your score with the largest value
# So, we need to be able to accessing the next largest value, always

# We can do so with a heap

from heapq import heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        for v in nums: 
            heappush(pq, -v)
        score = 0
        for _ in range(k):
            maxVal = -heappop(pq)
            # print(maxVal)
            score += maxVal
            # print(ceil(maxVal / 3))
            heappush(pq, -ceil(maxVal / 3))

        return score


Solution().maxKelements([1, 10, 3, 3, 3], 3)