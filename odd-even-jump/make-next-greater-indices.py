# Sub problem derived:
# Given an array `arr`, produce an array whose ith value
# corresponds to the index of the next greater or equal to element of `arr[i]`

# Solution 1: Sort and use stack
from typing import List


def calculateSmallestGreaterOrEqualToIndices(arr: List[int]):
    indices = [-1] * len(arr)
    # as we iterate, indices are for sure greater
    # however, they might not have greater elements
    stack = []
    for i, ele in enumerate(arr):
        while len(stack) > 0 and stack[-1][1] <= ele:
            indices[stack.pop()[0]] = i
        stack.append([i, ele])
    return indices


def calculateGreatestSmallerOrEqualToIndices(arr: List[int]):
    indices = [-1] * len(arr)
    # as we iterate, elements for sure are greater
    # however, they might not have greater indices
    stack = []
    # Note that reverse(sorted([v, i] for i, v in enumerate(arr)) does not work, because the following happens
    # for sorted = sorted([v, i] for i, v in enumerate(arr))= [[1, 0], [1, 1]
    # reverse(sorted) = [[1, 1], [1, 0]], but we don't want that
    # Conversely, by using -, we obtain [[-1, 0], [-1, 1]], indices flow left to right, as required
    temp = sorted([[-v, i] for i, v in enumerate(arr)])
    for _, i in temp:
        while len(stack) > 0 and stack[-1] < i:
            indices[stack.pop()] = i
        stack.append(i)
    return indices


# Similar to original sub problem, but, produce an array whose ith value
# correponds to the next greater or equal to element of `arr[i]`, and not the index of
def calculateSmallestGreaterOrEqualToItems(arr: List[int]):
    stack = []
    res = [-1] * len(arr)
    for i, ele in enumerate(arr):
        while len(stack) > 0 and stack[-1][0] <= ele:
            res[stack.pop()[1]] = ele
        stack.append([ele, i]) # need to still keep track of i to know where to insert into res
    return res

# Yet another sub problem, this time, the order of the array matters even more
# Previously, the answer of the next greater or equal to item won't change as long as its
# index is greater
# But this one calculates the closest item that immediately satisfy the greater or equal to item 

# Note that no sorting is done.
def calculateClosestGreaterOrEqualToItems(arr: List[int]): 
    stack = []
    res = [-1] * len(arr)
    for i, ele in enumerate(arr):
        while len(stack) > 0 and stack[-1][0] <= ele:
            res[stack.pop()[1]] = ele
        # need to still keep track of i to know where to insert into res
        stack.append([ele, i])
    return res
