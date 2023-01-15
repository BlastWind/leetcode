from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # count num pos
        num_pos, num_neg = 0, 0
        for v in nums: 
            if v > 0: 
                num_pos += 1
            elif v < 0: 
                num_neg += 1

            


        return max(num_pos, num_neg)


        # return max (num pos, num neg)
        return 0