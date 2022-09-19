from itertools import product
from typing import List
import numpy as np

from itertools import chain


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid) - 2, len(grid) - 2
        res = [[0] * C for _ in range(R)]
        for r, c in product(range(R), range(C)):
            res[r][c] = max(list(chain((row[c: c + 2])
                            for row in grid[r: r + 2])))
        return res

    def largestLocal2(self, grid: List[List[int]]) -> List[List[int]]:
        return [[max(list(chain((row[c: c + 2])
                                for row in grid[r: r + 2])))
                 for c in range(len(grid) - 2)] for r in range(len(grid) - 2)]


print(Solution().largestLocal2(
    [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
