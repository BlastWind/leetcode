from collections import deque
from functools import reduce
import itertools
from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + digit for digit,
                        group in itertools.groupby(s))

        return reduce(lambda acc, _: ''.join(str(len(list(group))) + digit for digit,
                                             group in itertools.groupby(acc)), range(n-1), '1')


driver = Solution()
print(driver.countAndSay(10))
