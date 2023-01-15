from collections import defaultdict, deque
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # idea, to find closest apple to a node, simply bfs until we hit apple.
        # also keep track of apple count, because when it's 0, don't search anymore, just return to node 0

        adj_list = defaultdict(list)
        for (from_node, to_node) in edges:
            adj_list[from_node].append(to_node)
            # adj_list[to_node].append(from_node)

        def collect_apples(from_node: int, apples_left: int, acc: int) -> int:
            if apples_left == 0:
                # do bfs until node 0
                q = deque([from_node])
                level = 0
                while q: 
                    for _ in range(len(q)):
                        node = q.popleft()
                        if node == 0:
                            return acc + level
                        for neighbor in adj_list[node]:
                            q.append(neighbor)

                    level += 1

            q = deque([from_node])
            level = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if hasApple[node]:
                        hasApple[node] = False
                        return collect_apples(node, apples_left - 1, acc + level)
                    for neighbor in adj_list[node]:
                        q.append(neighbor)

                level += 1

            assert False

        return collect_apples(0, hasApple.count(True), 0)


driver = Solution()
print(
    driver.minTime(
        7,
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        [False,False,True,False,True,True,False],
    )
)
