# To fix does-not-work.py
# Note that we can find maxSumSubmatrix by iterating by traversing through all 1-rowed sub grids, 2-rowed sub grids, ...
# Traversing through all n-rowed sub grids will actually find maxSumSubmatrix of all sub grids of size n*n


from bisect import bisect, bisect_left, insort
from itertools import product
from operator import add
from typing import List


def findSmallestLargerOrEqualTo(arr: List[int], target):
    if not arr or target > arr[len(arr)-1]:
        return (False, 0)  # There is no element larger than target in the array
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:  # if strictly smaller, smallest >= must be to the right of mid
            lo = mid + 1
        else:
            # if non strictly larger, old arr[mid] definitely could be smallestLargerOrEqualTo, so leave hi = mid and not hi = mid - 1
            hi = mid
    return (True, arr[lo])


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        res = -10000000
        for i in range(1, R+1):
            lastCompressed = None
            for j in range(0, R-i+1):
                # i, j corresponds to the jth i-rowed sub grid

                # column sums of the jth i-rowed subgrid
                # from j to j + i, add each row
                compressed = list(
                    map(sum, zip(*matrix[j:j+i]))) if not lastCompressed else lastCompressed
                if lastCompressed:
                    for ii, v in enumerate(matrix[j-1]):
                        compressed[ii] -= v
                    for ii, v in enumerate(matrix[j+i-1]):
                        compressed[ii] += v
                lastCompressed = compressed
                # KADANE BEGIN
                acc = maxx = compressed[0]
                for v in compressed[1:]:
                    acc = max(acc + v, v)
                    maxx = max(maxx, acc)
                if maxx <= k:
                    res = max(res, maxx)
                    continue
                # KADANE END
                sortedContainer = [0]  # keeps prefix sums
                acc = 0
                for v in compressed:
                    acc += v  # acc
                    ok, smallestLargerOrEqualTo = findSmallestLargerOrEqualTo(
                        sortedContainer, acc - k)
                    if ok:
                        res = max(res, acc - smallestLargerOrEqualTo)
                    insort(sortedContainer, acc)
        return res


driver = Solution()


print(driver.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
# print(driver.maxSumSubmatrix([[27, 5, -20, -9, 1, 26, 1, 12, 7, -4, 8, 7, -1, 5, 8], [16, 28, 8, 3, 16, 28, -10, -7, -5, -13, 7, 9, 20, -9, 26], [24, -14, 20, 23, 25, -16, -15, 8, 8, -6, -14, -6, 12, -19, -13], [28, 13, -17, 20, -3, -18, 12, 5, 1, 25, 25, -14, 22, 17, 12], [7, 29, -12, 5, -5, 26, -5, 10, -5, 24, -9, -19, 20, 0, 18], [-7, -11, -8, 12, 19, 18, -15, 17, 7, -1, -11, -10, -1, 25, 17], [-3, -20, -20, -7, 14, -12, 22, 1, -9, 11, 14, -16, -5, -12, 14], [-20, -4, -17, 3, 3, -
#       18, 22, -13, -1, 16, -11, 29, 17, -2, 22], [23, -15, 24, 26, 28, -13, 10, 18, -6, 29, 27, -19, -19, -8, 0], [5, 9, 23, 11, -4, -20, 18, 29, -6, -4, -11, 21, -6, 24, 12], [13, 16, 0, -20, 22, 21, 26, -3, 15, 14, 26, 17, 19, 20, -5], [15, 1, 22, -6, 1, -9, 0, 21, 12, 27, 5, 8, 8, 18, -1], [15, 29, 13, 6, -11, 7, -6, 27, 22, 18, 22, -3, -9, 20, 14], [26, -6, 12, -10, 0, 26, 10, 1, 11, -10, -16, -18, 29, 8, -8], [-19, 14, 15, 18, -10, 24, -9, -7, -19, -14, 23, 23, 17, -5, 6]], -100))

# print(findSmallestLargerOrEqualTo([1, 5, 7], 5))
