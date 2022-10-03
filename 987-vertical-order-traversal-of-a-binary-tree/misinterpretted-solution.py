### I initially thought this problem was a little harder
### where the tree [0,1,null,null,2,6,3,null,null,null,4,null,5] will actually only have 2 columns.
### But then I read that going to the left is always col - 1 and right is always col + 1


from collections import defaultdict
from math import ceil, floor
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def centerfloor(x):  # centerfloor towards 0
    return ceil(x) if x < 0 else floor(x)


def iswhole(x):
    return x - ceil(x) == 0


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)

        def recur(root: Optional[TreeNode], rootCol, parentCol):
            if not root:
                return
            if parentCol > rootCol:
                if iswhole(rootCol):
                    recur(root.left, rootCol - 1, rootCol)
                else:
                    recur(root.left, rootCol -
                          ((abs(parentCol) - abs(rootCol)) / 2), rootCol)
                mp[centerfloor(rootCol) if rootCol - centerfloor(rootCol)
                   >= 0.5 else ceil(rootCol)].append(root.val)

                recur(root.right, (rootCol + parentCol) / 2, rootCol)
            else:
                recur(root.left, (rootCol + parentCol) / 2, rootCol)
                mp[centerfloor(rootCol) if rootCol - centerfloor(rootCol)
                   >= 0.5 else ceil(rootCol)].append(root.val)

                if iswhole(rootCol):
                    recur(root.right, rootCol + 1, rootCol)
                else:
                    recur(root.right, rootCol +
                          ((abs(parentCol) - abs(rootCol)) / 2), rootCol)
            print(root.val, rootCol, centerfloor(rootCol) if rootCol - centerfloor(rootCol)
                  >= 0.5 else ceil(rootCol))

        if root:
            if root.left:
                recur(root.left, -1, 0)
            mp[0].append(root.val)
            if root.right:
                recur(root.right, 1, 0)

        return [sorted(l) for l in mp.values()]
