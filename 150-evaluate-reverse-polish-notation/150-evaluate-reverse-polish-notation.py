from math import ceil, floor, trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x,
            '*': lambda x, y: y * x,
            '/': lambda x, y: trunc(y / x),
        }
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[-1]


driver = Solution()

print(driver.evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
