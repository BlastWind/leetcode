from collections import defaultdict
from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # price sum is simply the accumulation down a path
        # minimum path price sum is simply the single lowest price associated with a node 

        # there could be multiple costs at one particular node
        adj_list = defaultdict(list)
        for from_node, to_node in edges: 
            adj_list[from_node].append(to_node)
            adj_list[to_node].append(from_node)

        

        return 0