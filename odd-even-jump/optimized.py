from bisect import insort_left
from cgitb import small
from collections import OrderedDict
from operator import index, indexOf
from typing import Dict, List, Tuple


class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

            # higher[i] corresponds to whether or not the ith index odd jump success
            # lower[i] corresponds to whether or not ith index even jump success
        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)


driver = Solution()
print(driver.oddEvenJumps([1, 2, 3, 2, 1, 4, 4, 5]))
