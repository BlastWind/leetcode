class Solution:
    def findBall(self, grid):
        ans = []
        rowCount = len(grid)
        colCount = len(grid[0])
        balls = colCount
        for b in range(balls):
            nextCol = b
            for row in range(rowCount):
                prevCol = nextCol
                nextCol += grid[row][nextCol]
                if nextCol < 0 or nextCol >= colCount:
                    nextCol = -1
                    break
                # if ball went right, check if right net is -1
                if grid[row][prevCol] == 1 and grid[row][nextCol] == -1:
                    nextCol = -1
                    break
                # if ball went left, check if left net is 1
                if grid[row][prevCol] == -1 and grid[row][nextCol] == 1:
                    nextCol = -1
                    break
            ans.append(nextCol)
        return ans
a = Solution()
a.findBall([[1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1],[-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1],[1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1]])