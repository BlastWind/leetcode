# Since we are in the BST

# If we traverse in order, the elements traversed are in sorted order


from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


class Solution:

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        dq = deque()

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if len(dq) == k:
                if abs(root.val-target) > abs(dq[0] - target):
                    return
                else:
                    dq.popleft()
                    dq.append(root.val)
            else:
                dq.append(root.val)
            inorder(root.right)
        inorder(root)
        return list(dq)
