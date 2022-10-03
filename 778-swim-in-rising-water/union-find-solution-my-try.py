# Slower, O(N^2 log N^2) because union find is log N^2 here.

from itertools import product
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        nodes = []
        topLeft = grid[0][0]
        botRight = grid[R-1][C-1]
        sortedGrid = sorted([(grid[i][j], i, j) for i, j in product(
            range(len(grid)), range(len(grid[0])))])

        representative = {val:val for val, _, _ in sortedGrid} # representative[]
        size = {val: 1 for val in representative}
        
        # sort grid
        for val, i, j in sortedGrid: 
            v = find(val)
            # add neighbor edges 
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= i < R and 0 <= j < C: 
                    u = find(grid[ii][jj])
                    
                    
                    combine(u, v)

        def 

        def find (tup):
            pass

        # for each cell, add neighbor edges, larger edges are representatives of smaller edges
        # however, the bottom right and top left edges are always representatives.

        # def find(u):
        #     if representative[u] == u:
        #         return u
        #     representative[u] = find(representative[u])
        #     return representative[u]

        # def combine(u, v):
        #     u = find(u)
        #     v = find(v)

        #     if u == v:
        #         return

        #     if size[u] < size[v]:
        #         representative[u] = v
        #         size[u] += size[v]
        #     else:
        #         representative[v] = u
        #         size[v] += size[u]


        # go from smallest to largest edge

        # for each edge
        #    add edge
        return -1


driver = Solution()
print(driver.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
      12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
