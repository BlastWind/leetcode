from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recur(root) -> int: 
            nonlocal ret
            if not root: return 0
            # the max(..., 0) is important:
            # If a subpath ever yields negative, abandon it!
            l = max(recur(root.left), 0)
            r = max(recur(root.right), 0) 
            # Need to update every time a new subpath is considered, since subpath does not 
            # need to touch root
            ret = max(root.val, root.val + l + r)
            return root.val + max(l, r)

        ret = -1001
        recur(root)
        return ret
driver = Solution()
# print(driver.maxPathSum())
