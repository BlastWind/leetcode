from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # smart technique: For each query, add 1 to its start index and -1 to its end index
        # afterwards, we run prefix sum on each row, which effectively keeps the accumulation of the 1's and -1's 
        # and set each new cell as the value of the current accumulation.

        marks = [[0] * n for _ in range(n)]
        for [row1, col1, row2, col2] in queries: 
            for row in range(row1, row2 + 1):
                marks[row][col1] += 1 
                if col2 + 1 < n: 
                    marks[row][col2 + 1] -= 1
        
        for i in range(n):
            for j in range(1, n): # compute prefix sum on each row
                marks[i][j] = marks[i][j-1] + marks[i][j]


        return marks