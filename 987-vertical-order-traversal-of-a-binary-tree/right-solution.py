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



class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def recur(root: Optional[TreeNode], col):
            if not root:
                return
            nonlocal minn 
            nonlocal maxx
            minn = min(minn, col) 
            maxx = max(maxx, col)
            mp[col].append(root.val)
            recur(root, col - 1)
            recur(root, col + 1)
            
        minn, maxx = 0, 0
        cols = abs(maxx - minn)
        res = [[] for _ in range(cols)]

        for key in mp: 
            loc = abs(key)
            res[loc] = mp[key]

        if root:
            recur(root, 0)

        return res