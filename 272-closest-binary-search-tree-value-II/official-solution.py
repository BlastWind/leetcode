from heapq import heappop, heappush, heappushpop
from queue import PriorityQueue
from typing import List, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


class Solution:

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def recur(root):
            if not root:
                return
            recur(root.left)
            heappush(heap, (-abs(root.val - target), root.val))
            if len(heap) > k:
                heappop(heap)
            recur(root.right)

        heap = []
        recur(root)

        return [x for _, x in heap]
