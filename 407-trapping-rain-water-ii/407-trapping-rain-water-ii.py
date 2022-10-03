from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
       # if edge less than or equal to inner: inner will flow out completely, recurse for more complete leaks. Mark all complete leaks
       # if edge greater than inner: There could still be leaks at this edge from inner, recurse and update minMax


       # For each cell, return 0 if a border cell can reach it in ascending or equal steps 
       # Else, return the minimum maximum value that it can travel to in ascending steps


       # from each edge, let in edge units of water
       # if let in is greater than edge, recurse with the same edge unis 
       # if let in is less than or equal to edge, stop recursing, but add the greater edge to queue

        res = 0

        return res 

driver = Solution()
print(driver.trapRainWater(
    [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))

# in trapping-rain-water-i, we could generate leftMax and rightMax, 

# now, we need to generate leftMax, rightMax, upMax, downMax.