from collections import defaultdict
from pprint import pprint
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # algorithm: Always collect the next closest apple.
        # The algorithm utilizes an adjacency matrix mat where mat[i][j] represents the dist between node i and j

        def make_mat():
            '''
            Returns a matrix mat where mat[i][j] is the dist between node i and j
            '''
            # inits
            mat = [[-1] * (n) for _ in range(n)]
            for i in range(len(mat)):
                mat[i][i] = 0

            adj_list = defaultdict(list)
            for (f, t) in edges: 
                adj_list[f].append(t)

            # build one cell (technically two for mirror-ness in mat)
            def step(from_node: int, to_node: int):
                for i in range(n):
                    # for each cell going to from_node
                    if mat[i][from_node] != -1: 
                        mat[i][to_node] = mat[i][from_node] + 1 # two cells set

                for i in range(n):
                    mat[to_node][i] = mat[i][to_node] 

                for next in adj_list[to_node]:
                    step(to_node, next)
            
            for zero_next in adj_list[0]: # run build
                step(0, zero_next)

            return mat 
        mat = make_mat()

        applesAt = set([i for i in range(len(hasApple)) if hasApple[i]])
        pprint(mat)

        def traverse():
            '''
            starting from 0, find closest apple by querying each apple in mat
            then, remove this apple, add dist to sum, and start at where the apple is.
            when no more apple, remember to return to 0
            '''

            sum = 0
            def step(from_node: int) -> int:
                nonlocal sum
                if len(applesAt) == 0: 
                    sum += mat[from_node][0]
                    return sum 

                min_dist, closest_apple = min([(mat[from_node][apple], apple) for apple in applesAt])
                sum += min_dist
                applesAt.remove(closest_apple)
                step(closest_apple)
                return sum

            step(0)
            return sum

        return traverse()


# another idea: Maybe just do an ordered traversal, but sever edges during?

driver = Solution()
print(
    driver.minTime(
        4,
        [[0,2],[0,3],[1,2]],
        [False,True, False, False],
    )
)
