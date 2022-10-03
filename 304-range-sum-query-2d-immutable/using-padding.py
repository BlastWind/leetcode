'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

'''

from itertools import product
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # How to calculate the "up until" sum of 2d array?
        # Expand 1x1 -> 2x2 -> 3x3 until stuck, then, freely expand in row or col

        # Prefill Row 1 and Col 1
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C+1) for _ in range(R+1)]
        for i, j in product(range(1, R+1), range(1, C+1)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return dp[row2][col2] - (dp[row2][col1-1]) - (dp[row1-1][col2]) + dp[row1-1][col1-1]


# a = NumMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = NumMatrix([[-1, -2, -9, 6], [8, -9, -3, -6], [2, 9, -7, -6]])
print(a.sumRegion(0, 0, 0, 0))
# print(a.sumRegion(1, 1, 2, 2))
