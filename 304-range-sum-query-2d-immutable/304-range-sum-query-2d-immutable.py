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
        dp = [[0] * C for _ in range(R)]
        dp[0][0] = matrix[0][0]
        for i in range(1, C):
            dp[0][i] = dp[0][i-1] + matrix[0][i]
        for i in range(1, R):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        
        for i, j in product(range(1, R), range(1, C)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]

        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # might delete leftStrip and topStrip
        tL = self.dp
        if row1 == 0 and col1 == 0: 
            return tL[row2][col2]
        if row1 == 0: 
            return tL[row2][col2] - tL[row2][col1-1]
        if col1 == 0: 
            return tL[row2][col2] - tL[row1-1][col2]
        # print((tL[col1-1][row2]), (tL[row1-1][col2]))
        return tL[row2][col2] - (tL[row2][col1-1]) - (tL[row1-1][col2]) + tL[row1-1][col1-1]


# a = NumMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = NumMatrix([[-1, -2, -9, 6], [8, -9, -3, -6], [2, 9, -7, -6]])
print(a.sumRegion(0,0,0,0))
# print(a.sumRegion(1, 1, 2, 2))
