import collections
from heapq import heappop, heappush, heappushpop
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        for i, num in enumerate(nums):
            left, right = i-k+1, i+1
            while dq and dq[0] < left: # actually the while is replaceable by if since the 2nd element is always >= left
                dq.popleft()
            while dq and num > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if right >= k:
                res.append(nums[dq[0]])
        return res

driver = Solution()
print(driver.maxSlidingWindow([1, -1], 1))
