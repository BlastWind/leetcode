from random import randint
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        # naive algo: sum the list
        # create an array of that length

        # create prefix array:
        # [1, 3] -> [0, 1, 4]

        # And then binary search for which range we belong in
        prefix = [w[0]]
        for weight in w[1:]:
            prefix.append(weight + prefix[-1])
        self.range = prefix

    def pickIndex(self) -> int:
        r = self.range[-1] * random.random()
        # find index of smallest strictly larger element than with binary search 
        lo, hi = 0, len(self.range) - 1
        while lo < hi: 
            mid = lo + (hi - lo) // 2 
            if self.range[mid] < r: 
                # move pass
                lo = mid + 1
            else: # when >= 1, can't move pass because mid might be the smallest strictly larger element 
                hi = mid
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
obj = Solution([3, 14, 1, 7])
count = [0] * len(obj.range)
for _ in range(1000):
    count[obj.pickIndex()] += 1
print(count)
