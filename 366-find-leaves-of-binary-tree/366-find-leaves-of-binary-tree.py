from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeavesSimulation(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Actually find leaves, remove them, and repeat till no leaves
        res = []

        def emptyLeaves(root):
            if not root:
                return None
            if not root.left and not root.right:
                # root is leaf
                res[-1].append(root.val)
                return None

            root.left = emptyLeaves(root.left)
            root.right = emptyLeaves(root.right)
            return root
        while root:
            res.append([])
            root = emptyLeaves(root)
        return res

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return height from bottom
        res = defaultdict(list)

        def dfs(root) -> int:
            if not root:
                return 0
            distFromBottom = 1 + max(dfs(root.left), dfs(root.right))
            res[distFromBottom].extend(root.val)
            return distFromBottom
        dfs(root)
        return res.values()


driver = Solution()
print(driver.findLeaves())
