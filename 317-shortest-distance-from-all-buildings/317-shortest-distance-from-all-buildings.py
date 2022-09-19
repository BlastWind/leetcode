from distutils.command.build import build
from itertools import chain
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # get building coordinates
        buildings = [((i, j),  (i, j)) for j in range(C)
                     for i in range(R) if grid[i][j] == 1]
        buildingsCnt = len(buildings)

        # assign each empty land a visitedBy set, denoting which buildings have visited the empty land
        memo = [[{(i, j): 0} if grid[i][j] == 1 else {}
                for j in range(C)] for i in range(R)]
        q = buildings
        for (i, j), (buildingI, buildingJ) in q:  # for ... in ... mimics a queue!
            for I, J in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # bound check
                if 0 <= I < R and 0 <= J < C and grid[I][J] != 2 and grid[I][J] != 1:
                    # .difference() order matters. This order says: Find the buildings that have yet to visit new node
                    if (buildingI, buildingJ) in memo[I][J]:
                        continue
                    distFromBuilding = memo[i][j][(buildingI, buildingJ)]
                    # set visited in parent call
                    memo[I][J][(buildingI, buildingJ)] = distFromBuilding + 1
                    grid[I][J] = grid[I][J] - \
                        memo[I][J][(buildingI, buildingJ)]
                    if len(memo[I][J]) == buildingsCnt:
                        # return -grid[I][J]
                        pass
                    q.append(((I, J), (buildingI, buildingJ)))
        minn = -(1 << 31)
        for i in range(len(memo)): 
            for j in range(len(memo[i])):
                if len(memo[i][j]) == buildingsCnt: 
                    minn = max(minn, grid[i][j])
        return minn or -1
        # return min(list(d.values() for d in (chain.from_iterable(memo))))
        

driver = Solution()
print(driver.shortestDistance(

    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
