from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find the representative of the set
        def parent(x):
            while root[x] != x:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x, y):
            px = parent(x)
            py = parent(y)
            if px != py:
                if size[px] > size[py]:
                    px, py = py, px
                size[py] += size[px]
                root[px] = py

        n = len(grid)
        size = [1]*(n*n)
        root = list(range(n*n))
        vis = [[False]*n for _ in range(n)]
        positions = sorted([(i, j) for i in range(n)
                           for j in range(n)], key=lambda x: grid[x[0]][x[1]])

        # note the vis[x][y] enforcement: Neighbors aren't expanded on first iteration!
        # They can only be joined backwards, on neighbors that have been visited already.
        # This way, we enforce large edges (like 0->24) are not formed immediately. 

        # Proof that still, all nodes will be visited
            # All nodes are visited if all edges, direction not mattering, are visited at least once.
            # Edges are visited twice (because cell -> neighbor is once, and neighbor -> cell is another)
            # If on first visit, the other cell hasn't been visited yet, then, on the second visit, the other cell must be visited
        for i, j in positions:
            vis[i][j] = True
            # explore the neighbors to grow the disjoint sets
            for x, y in (i+1, j), (i-1, j), (i, j-1), (i, j+1):
                if 0 <= x < n and 0 <= y < n and vis[x][y]:
                    union(i*n+j, x*n+y)

            # the start and end points are joined together
            if parent(0) == parent(n*n-1):
                return grid[i][j] # important! Realize that cells are visited in ascending order. So just return grid[i][j] when valid

        return -1


driver = Solution()
print(driver.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
      12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
