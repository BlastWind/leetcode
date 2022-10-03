from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        dp = [-1] * len(s)
        for i, c in enumerate(s): 
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    dp[i] = stack.pop()[1]
                else: 
                    stack = []
        print(dp)
        lengthDP = [-1] * len(s)
        for i in range(len(dp)-1, -1, -1):
            to = dp[i]
            if to < 0: continue
            length = 0
            while to >= 0 and i != -1: 
                dp[i] = -1 # because travelling reverse, any future elements that hit this are bound to be smaller than starting from i
                length += (i - to + 1)
                i = to - 1
                to = dp[i]
            
            res = max(res, length)
        return res
    def stackSolution(self, s:str) -> int: 
        maxans = 0 
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else: 
                stack.pop()
                if not stack: stack.append(i)
                else: maxans = max(maxans, i - stack[-1])
        return maxans
driver = Solution()
print(driver.stackSolution("()()"))

# find a way such that, after popping a pair, the index of the last valid ( is still on the stack

# for situations where contiguous pairs start from 0, we need an initial -1 in the stack 

# so algorithm basically translates to: 
# Whenever a ( comes, update the base difference ptr. Whenever a invalid ) comes, update the base difference ptr, 
# a ) must be invalid if it pops the original -1, aka when stack empty
# 