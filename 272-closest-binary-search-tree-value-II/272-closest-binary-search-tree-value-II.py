from bisect import bisect, insort
from fileinput import close
from typing import (
    List,
)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def insert(into: List[int], val: int, compareFn):
    # into is sorted in ascending order
    # compareFn :: a -> b -> Bool, True then insert before
    for i, num in enumerate(into):
        if compareFn(val, num) : 
            return into[:i] + [val] + into[i:]
    return into + [val]
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
             we will sort your return value in output
    """

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        # write your code here
        


        def merge(l1: List[int], l2: List[int], rootVal: int, k: int) -> List[int]:
            l1Ptr, l2Ptr = 0, 0
            res = []
            while l1Ptr < len(l1) and l2Ptr < len(l2):
                if abs(l1[l1Ptr] - target) < abs(l2[l2Ptr] - target):
                    res.append(l1[l1Ptr])
                    l1Ptr += 1
                else:
                    res.append(l2[l2Ptr])
                    l2Ptr += 1
            if l1Ptr < len(l1):  # still l1Ptr left
                res += l1[l1Ptr: k-len(res)]
            if l2Ptr < len(l2):
                res += l2[l2Ptr: k-len(res)]

            res = insert(res, rootVal, lambda x, y: abs(x - target) < abs(y - target))

            return res[:k]

        def closest_k_recur(root) -> List[int]:
            if not root:
                return []
            l1 = closest_k_recur(root.left)
            l2 = closest_k_recur(root.right)
            return merge(l1, l2, root.val, k)
        return closest_k_recur(root)

a = Solution()
# tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
tree = TreeNode(1, None, TreeNode(2))
# print(a.closestKValues(tree, 3.7, 1))
# a = [1, 2, 3]
# def lessThan(a, b): return a < b

def merge(l1: List[int], l2: List[int], rootVal: int, k: int, target:float) -> List[int]:
        l1Ptr, l2Ptr = 0, 0
        res = []
        while l1Ptr < len(l1) and l2Ptr < len(l2):
            if abs(l1[l1Ptr] - target) < abs(l2[l2Ptr] - target):
                res.append(l1[l1Ptr])
                l1Ptr += 1
            else:
                res.append(l2[l2Ptr])
                l2Ptr += 1
        if l1Ptr < len(l1):  # still l1Ptr left
            res += l1[l1Ptr: l2Ptr + k-len(res)]
        if l2Ptr < len(l2):
            res += l2[l2Ptr: l2Ptr+k-len(res)]

        res = insert(res, rootVal, lambda x, y: abs(
            x - target) < abs(y - target))

        return res[:k]


print(merge([1, 0],[3, 4, 5, 6, 7, 8], 2, 6, 2.42))

