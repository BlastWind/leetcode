from collections import defaultdict, deque
from heapq import heappop, heappush
from optparse import Option
from typing import List, Optional, Tuple
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        # if key not in list when set is called, list is created on the spot
        adjacencyList = defaultdict(list)

        def buildGraph(parent, node) -> None:
            if not node:
                return
            if parent:
                adjacencyList[parent.val].append(node.val)
                adjacencyList[node.val].append(parent.val)
            buildGraph(node, node.left)
            buildGraph(node, node.right)
        buildGraph(None, root)

        visited = set()
        visited.add(-1)

        def time(root):
            if root is None or root in visited:
                return 0
            visited.add(root)
            maxx = 0
            for neighbor in adjacencyList[root]:
                maxx = max(time(neighbor), maxx)
            return 1 + maxx
        return time(start) - 1

    def amountOfTimeBFS(self, root: Optional[TreeNode], start: int) -> int:

        # if key not in list when set is called, list is created on the spot
        adjacencyList = defaultdict(list)

        def buildGraph(parent, node) -> None:
            if not node:
                return
            if parent:
                adjacencyList[parent.val].append(node.val)
                adjacencyList[node.val].append(parent.val)
            buildGraph(node, node.left)
            buildGraph(node, node.right)
        buildGraph(None, root)

        visited = set()
        visited.add(-1)

        q = deque([start])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                for neighbor in adjacencyList[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
            res += 1
        return res


    def amountOfTimeOnePassDFS(self, root: Optional[TreeNode], start: int) -> int:
        # returns (True, dist to infected) or (False, dist to leaf)
        def dfs(root) -> Tuple[bool, int, int]:
            if not root:
                return (False, 0, 0)
            leftHit, leftLen, leftMax = dfs(root.left)
            rightHit, rightLen, rightMax = dfs(root.right)
            # if infected node found now
            if root.val == start:
                return (True, 0, max(leftLen, rightLen)) # 0 because the start node is already infected at time 0
            # if infected node found previously
            if leftHit: 
                return (True, leftLen + 1, max(leftMax, leftLen + rightLen + 1))
            if rightHit:
                return (True, rightLen + 1,  max(rightMax, leftLen + rightLen + 1))
            # if no infected node found yet
            return (False, 1 + max(leftLen, rightLen), 0)
        return dfs(root)[2]

    


a = Solution()
print(a.amountOfTime(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), 1))

# rotate the binary tree and make startNode the root
