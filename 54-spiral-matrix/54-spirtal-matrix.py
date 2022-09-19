from typing import List

# Hey babe, note that in the list slicing, I had to do a +1 in many cases to include the end index
# Also, I am gathering the outer elements by iterating over the entire top row, a chunked right column, the entire bottom row, and a chunked left column
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def swirl(rowStart: int, rowEnd: int, colStart: int, colEnd: int) -> List[int]:
            rowDiff, colDiff = rowEnd - rowStart, colEnd - colStart
            if rowDiff < 0 or colDiff < 0:
                return []
            if rowDiff == 0:  # same row, so return the row
                return matrix[rowStart][colStart: colEnd+1]
            if colDiff == 0:  # same col, so return the col
                return [row[colStart] for row in matrix[rowStart: rowEnd+1]]
            around = []
            # entire top row
            around += matrix[rowStart][colStart: colEnd+1]
            # right column but without the last element of the top row and first element of bottom row
            around += [row[colEnd] for row in matrix[rowStart+1: rowEnd]]
            # bottom row. Note that I first do matrix[rowEnd][colStart:colEnd+1] to get the bottom row elements, then I do [::-1] to reverse them
            # I tried doing this one call matrix[rowEnd][colEnd: colStart-1:-1] but it wasn't working, guessing end index of slice can't seem to be negative? Not sure.
            around += matrix[rowEnd][colStart: colEnd+1][::-1]
            # left column but without first element of top row and last element of bottom row
            around += [row[colStart] for row in matrix[rowEnd-1: rowStart: -1]]
            return around + swirl(rowStart + 1, rowEnd - 1, colStart + 1, colEnd - 1)
        return swirl(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

a = Solution()
print(a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
