from collections import defaultdict
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = [height[0]] # leftMax[i] gives max height from i to end 
        rightMax = [height[len(height)-1]] # rightMax[i] gives max height from i to start
        for h in height[1:]: 
            leftMax.append(max(leftMax[-1], h))
        for h in height[len(height)-2::-1]: 
            rightMax.append(max(rightMax[-1], h))
        rightMax = rightMax[::-1]
        for i, h in enumerate(height):
            res += min(leftMax[i], rightMax[i]) - h
        return res


driver = Solution()
print(driver.trap([4, 2, 0, 3, 2, 5]))
