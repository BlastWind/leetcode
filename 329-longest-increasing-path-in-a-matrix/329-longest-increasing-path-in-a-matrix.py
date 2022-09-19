from typing import List, Set


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        memo = [[-1] * C for _ in range(R)]

        def dfs(row, col, visited: Set, last):
            if row < 0 or row >= R or col < 0 or col >= C:
                return 0
            if (matrix[row][col], row, col) in visited:
                return 0
            if last >= matrix[row][col]:
                return 0
            if memo[row][col] != -1: 
                return memo[row][col]
            cur = matrix[row][col]
            visited.add((cur, row, col))

            maxx = 1 + max(dfs(row - 1, col, visited, cur), dfs(row + 1, col, visited, cur),
                           dfs(row, col - 1, visited, cur), dfs(row, col + 1, visited, cur))
            visited.remove((cur, row, col))
            memo[row][col] = maxx
            return maxx
        maxxx = 0
        s = set()
        for row in range(R):
            for col in range(C):
                maxxx = max(maxxx, dfs(row, col, s, -1))

        return maxxx


driver = Solution()
print(driver.longestIncreasingPath(
    [[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
