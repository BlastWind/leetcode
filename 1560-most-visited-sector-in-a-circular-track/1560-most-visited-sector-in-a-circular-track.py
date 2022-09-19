from collections import defaultdict
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start,  last = rounds[0],   rounds[-1]
        return list(range(start, last + 1)) or list(range(1, last + 1)) + list(range(start, n + 1))


driver = Solution()
print(driver.mostVisited(4, [1, 3, 1, 2]))
