# Does not work because: 
# each iteration is getting more container values than it is supposed to!


from bisect import bisect, bisect_left, insort
from itertools import product
from typing import List


def findSmallestLargerOrEqualTo(arr: List[int], target):
    if not arr or target > arr[len(arr)-1]: return -10000000000000000000 # There is no element larger than target in the array
    lo, hi = 0, len(arr) -1    
    while lo < hi: 
        mid = (lo + hi) // 2
        if arr[mid] < target: # if strictly smaller, smallest >= must be to the right of mid
            lo = mid + 1
        else: 
            hi = mid # if non strictly larger, old arr[mid] definitely could be smallestLargerOrEqualTo, so leave hi = mid and not hi = mid - 1
    return arr[lo]
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # DP can be kept to calculate the sums from (0, 0) to any (n, m)
        # From there, one could traverse through n, m and calculate sum of each submatrix by doing DP[n][m] - all DP[x][y] where x < n and y < m. O(n*n*m*m)
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C+1) for _ in range(R+1)]
        sorted = [0] # maintains areas in order
        res = -100000000
        for i, j in product(range(1, R+1), range(1, C+1)): 
            dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            # find the previous area, which when subtracted from current area, is <= k
            # cA - pA <= k; cA - k <= pA. So, find the smallest larger or equal to pA than (cA - k)
            smallestLargerOrEqualTo = findSmallestLargerOrEqualTo(sorted, dp[i][j] - k)
            # print(smallestLargerOrEqualTo)
            if smallestLargerOrEqualTo <= k:
                res = max(res, dp[i][j] - smallestLargerOrEqualTo)
            insort(sorted, dp[i][j])
        return res
driver = Solution()


print(driver.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]]
                             ,2))
# print(driver.maxSumSubmatrix([[27, 5, -20, -9, 1, 26, 1, 12, 7, -4, 8, 7, -1, 5, 8], [16, 28, 8, 3, 16, 28, -10, -7, -5, -13, 7, 9, 20, -9, 26], [24, -14, 20, 23, 25, -16, -15, 8, 8, -6, -14, -6, 12, -19, -13], [28, 13, -17, 20, -3, -18, 12, 5, 1, 25, 25, -14, 22, 17, 12], [7, 29, -12, 5, -5, 26, -5, 10, -5, 24, -9, -19, 20, 0, 18], [-7, -11, -8, 12, 19, 18, -15, 17, 7, -1, -11, -10, -1, 25, 17], [-3, -20, -20, -7, 14, -12, 22, 1, -9, 11, 14, -16, -5, -12, 14], [-20, -4, -17, 3, 3, -
#       18, 22, -13, -1, 16, -11, 29, 17, -2, 22], [23, -15, 24, 26, 28, -13, 10, 18, -6, 29, 27, -19, -19, -8, 0], [5, 9, 23, 11, -4, -20, 18, 29, -6, -4, -11, 21, -6, 24, 12], [13, 16, 0, -20, 22, 21, 26, -3, 15, 14, 26, 17, 19, 20, -5], [15, 1, 22, -6, 1, -9, 0, 21, 12, 27, 5, 8, 8, 18, -1], [15, 29, 13, 6, -11, 7, -6, 27, 22, 18, 22, -3, -9, 20, 14], [26, -6, 12, -10, 0, 26, 10, 1, 11, -10, -16, -18, 29, 8, -8], [-19, 14, 15, 18, -10, 24, -9, -7, -19, -14, 23, 23, 17, -5, 6]], -100))

# print(findSmallestLargerOrEqualTo([1, 5, 7], 5))