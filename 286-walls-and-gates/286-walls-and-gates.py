from collections import deque
from typing import List

# Key idea: Simultaneous BFS from all gates
# In other words, multisource BFS


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        R, C = len(rooms), len(rooms[0])
        wall, gate, empty = -1, 0, (1 << 31) - 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(i, j) for j in range(C) for i in range(R) if rooms[i][j] == gate]
        for i, j in q:
            for I, J in [(i + x, j + y) for x, y in dirs]:
                if 0 <= I < R and 0 <= J < C and rooms[I][J] == empty:
                    rooms[I][J] = rooms[i][j] + 1
                    q.append((I, J))

    def oldWallsAndGates(self, rooms: List[List[int]]) -> None:
        R, C = len(rooms), len(rooms[0])
        wall, gate, empty = -1, 0, (1 << 31) - 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # start from all gates
        q = deque([(i, j) for j in range(C)
                  for i in range(R) if rooms[i][j] == gate])

        visited = set(q)
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                visited.add((x, y))
                # if already has dist, don't keep going
                if rooms[x][y] > 0 and rooms[x][y] < empty:
                    continue
                rooms[x][y] = dist
                for dir in dirs:
                    nx, ny = x + dir[0], y + dir[1]
                    if nx >= R or ny >= C or nx < 0 or ny < 0 or rooms[nx][ny] == wall or (nx, ny) in visited:
                        continue
                    q.append((nx, ny))
            dist += 1


driver = Solution()
rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]

# rooms = [[0, 0], [0, 0]]
driver.wallsAndGates(rooms)
print(rooms)
