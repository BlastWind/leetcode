# Note that there is no need to keep a visited list
# Because, if written the right way, larger nodes won't step into the smaller nodes ever


import queue
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        memo = [[0] * C for _ in range(R)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if memo[row][col]:
                return memo[row][col]
            cur = matrix[row][col]
            memo[row][col] = 1 + max(dfs(row + x, col + y) if row + x >= 0 and row + x <
                                     R and col + y >= 0 and col + y < C and cur < matrix[row + x][col + y] else 0 for x, y in directions)
            return memo[row][col]

    def longestIncreasingPathTopologicalSort(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        indegrees = [[0] * C for _ in range(R)]
        # build indegrees
        for row in range(R):
            for col in range(C):
                for x, y in directions:
                    if row + x >= 0 and row + x < R and col + y >= 0 and col + y < C and matrix[row][col] < matrix[row + x][col + y]:
                        indegrees[row+x][col+y] += 1
        q = []  # remember to pop(0)
        for row in range(R):
            for col in range(C):
                if indegrees[row][col] == 0:
                    q.append((row, col))
        # topologically sort, all we want to know if how many levels of the graph there is (peeling onion) using the pathLen variable
        rounds = 0
        while q:
            for _ in range(len(q)):
                # Remove leaf nodes
                leafR, leafC = q.pop(0)
                for x, y in directions:
                    if leafR + x >= 0 and leafR + x < R and leafC + y >= 0 and leafC + y < C and matrix[leafR + x][leafC + y] > matrix[leafR][leafC]:
                        indegrees[leafR + x][leafC + y] -= 1
                        if indegrees[leafR + x][leafC + y] == 0:
                            q.append((leafR + x, leafC + y))
            rounds += 1
        return rounds


driver = Solution()
print(driver.longestIncreasingPathTopologicalSort(
    [[0], [1], [5], [5]]))

# matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# huh = {i + j*1j: val
#        for i, row in enumerate(matrix)
#        for j, val in enumerate(row)}
# print(huh)
