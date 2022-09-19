# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict, deque
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0 
        # recur down, passing along prevPathSum
        # calculate curPathSum, if curPathSum - target exists in hashmap, 
        
        # it must mean there is some prevPath in the current branch which, when 
        # subtracted from the branch, results in a target match
        cache = defaultdict(int, {0:1})
        def recur(root, target, prevSum):
            if not root: return
            nonlocal res
            curSum = root.val + prevSum 
            res += cache[curSum - target]
            cache[curSum] += 1
            
            recur(root.left, target, curSum)
            recur(root.right, target, curSum)

            cache[curSum] -= 1
        recur(root, targetSum, 0)
        return res
    def pathSumPrintSums(self, root: Optional[TreeNode], targetSum: int):
        cache = defaultdict(int)
        def recur(root, target, prevSum, prevPath):
            if not root: return
            curSum = prevSum + root.val 
            curPath = prevPath + [root.val]
            if cache[curSum - target] > 0: 
                temp = deque()
                sum = 0
                for num in (curPath[::-1]):
                    sum += num 
                    temp.appendleft(num)
                    if sum == target: 
                        print(list(temp))

            cache[curSum] += 1

            recur(root.left, target, curSum, curPath)
            recur(root.right, target, curSum, curPath)

            cache[curSum] -= 1

        recur(root, targetSum, 0, [])
a = Solution()
print(a.pathSumPrintSums(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8))