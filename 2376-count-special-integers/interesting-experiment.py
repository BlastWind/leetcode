from math import perm
from typing import List
# Most technique in this solution are ubiquitous in digit DP problems
# However, I differ with other solutions by not differentiating between isEdge and not edge results in the memo object
# Others might have done it because the result starting at the same index with the same mask is different between isEdge and not edge. 
# However, they fail to consider that the isEdge cases are the last ones run, so no "not edge" cases will reuse result from an isEdge case
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digitLen = len(str(n))
        def recur(ind: int,  isEdge: int, prevMask: int, memo: List[List[int]]) -> int:
            if ind >= digitLen:
                # prevMask is allowed to be 0 when the ending condition is met
                return 1 if prevMask else 0 
            firstDigit = int(str(n)[ind])
            if memo[ind][prevMask] != -1 and not isEdge:
                return memo[ind][prevMask]
            def inner(x: int):
                if (1 << x) & prevMask:  # x already used
                    return 0
                newMask = prevMask if prevMask == 0 and x == 0 else prevMask | (
                    1 << x)
                return recur(ind + 1,  1 if isEdge and x == firstDigit else 0, newMask, memo)
            memo[ind][prevMask] = sum(
                map(inner, range(firstDigit + 1 if isEdge else 10)))
            return memo[ind][prevMask]
        return recur(0, 1, 0, [[-1] * 1024 for _ in range(10)])

    # Given 8765
    # First calculate result with digits < N which is
    # XXX 
    #  XX 
    #   X
    # Now count the number with same prefix 
    def countSpecialNumbers2(self, N):
        L = list(map(int, str(N + 1)))
        n = len(L)
        # count the number with digits < N
        res = sum(9 * perm(9, i) for i in range(n - 1))
        s = set()
        # count the number with same prefix
        for i, x in enumerate(L):
            for y in range(i == 0, x):
                # For example, when i, x = 2, 3 for L = [2, 2, 4]
                # And y = 0 (so 220)
                # perm(9 - i, n - i - 1) is perm(7, 3-2-1) = perm(7, 0), perm(x, 0) = 1
                # So just simple add 1
                if y not in s:
                    res += perm(9 - i, n - i - 1)
            # Example: 223
            # On second enumeration, we have i = 1 and x = 2
            # We want to match away 20X and 21X
            # However, we know that starting the next index, nothing would work because we're matching 22X, so stop.
            if x in s:
                break
            s.add(x)
        return res
driver = Solution()
print(driver.countSpecialNumbers2(223))
