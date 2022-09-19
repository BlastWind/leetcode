from typing import List


class Solution:
    # [[bitmask]: result, [bitmask]: result]
    def countSpecialNumbers(self, n: int) -> int:
        digitLen = len(str(n))

        def recur(ind: int, prevDigit: int, isEdge: int, prevMask: int, memo: List[List[List[int]]]) -> int:
            if ind >= digitLen:
                # and prevMask checks if numbers have been used, thus eliminating number of all zeroes
                return 1 if prevMask else 0
            firstDigit = int(str(n)[ind])
            sum = 0
            if memo[ind][isEdge][prevMask] != -1:
                return memo[ind][isEdge][prevMask]
            for x in range(firstDigit + 1 if isEdge else 10):
                if (1 << x) & prevMask:  # x already used:
                    # memo[ind][prevMask] = 0
                    continue

                newMask = prevMask | (1 << x)
                # x has not been used
                # if zero is used as an actual value
                sum += recur(ind + 1, x, 1 if isEdge and x == firstDigit else 0, prevMask if prevDigit == 0 else newMask, memo) if x == 0 else recur(
                    ind + 1, x, 1 if isEdge and x == firstDigit else 0, newMask, memo)
            memo[ind][isEdge][prevMask] = sum
            return memo[ind][isEdge][prevMask]
        return recur(0, 0, 1, 0, [[[-1] * 1024, [-1] * 1024] for _ in range(10)])


driver = Solution()
print(driver.countSpecialNumbers(62850183))
a = set()
