# Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values of the board?

# Thoughts:
# Setting to -1 is the easiest solution, no extra memory used
# If this is disabled, that means either there is a O(1) way to storing battleship information 
# Or 


from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                if board == "*":
                    continue
                if board == "X":
                    for x, y in directions:
                        nx, ny = r + x, c + y
                        if nx >= 0 and nx < R and ny >= 0 and ny < C and board[nx][ny] == "X":
                            # battleship in this direction
                            while nx >= 0 and nx < R and ny >= 0 and ny < C and board[nx][ny] == "X":
                                nx, ny = nx + x, ny + y
                                board[nx][ny] = "*"
                            break
                    res += 1
                board[r][c] = "*"
        return res
driver = Solution()
print(driver.countBattleships(
    [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
