from queue import PriorityQueue
from typing import List

# O(N^2 log N): Each of the N^2 nodes require log N to perform the heap operations
class Solution:
    # simply find the path from left upper to right bottom with the smallest max element
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dp predetermines search order, probably not applicable because the optimal path is random
        R, C = len(grid), len(grid[0])
        q = PriorityQueue()
        q.put((grid[0][0], grid[0][0], (0,0))) # elements: (value, pathmax, index)
        visited = [[False] * C for _ in range(R)]
        # push neighbors, recalculate pathmax into min heap. 
        # if index is end, return max(cur, pathmax)
        while q: 
            val, pathmax, (i, j) = q.get()
            if i == R - 1 and j == C - 1: 
                return max(val, pathmax)
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i,j-1)]:
                if 0 <= ii < R and 0 <= jj < C and not visited[ii][jj]: 
                    q.put((grid[ii][jj], max(grid[ii][jj], pathmax), (ii, jj)))
                    visited[ii][jj] = True

        return -1
driver = Solution()
print(driver.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
      12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
