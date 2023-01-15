from collections import defaultdict, deque
from typing import List, Set


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        for (from_node, to_node) in edges:
            adj_list[from_node].append(to_node)
            adj_list[to_node].append(from_node)

        def dfs(from_node: int, visited: Set[int]) -> int: 
            acc = 0
            visited.add(from_node)

            # collect children sum
            for neighbor in adj_list[from_node]:
                if neighbor not in visited:
                    acc += dfs(neighbor, visited)
                
            if acc == 0: 
                return 2 if hasApple[from_node] and from_node != 0 else 0 
            else: 
                return acc if from_node == 0 else acc + 2

        return dfs(0, set())

driver = Solution()
print(
    driver.minTime(
        7,
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        [False,False,True,False,True,True,False],
    )
)
