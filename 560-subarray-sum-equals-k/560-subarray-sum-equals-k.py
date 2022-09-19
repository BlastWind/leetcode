from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # "freq table" that stores indices
        freq = {0: 1}
        carry = 0
        res = 0
        for num in nums:
            carry += num
            if carry - k in freq:
                res += freq[carry-k]
            freq[carry] = freq.get(carry, 0) + 1
        return res


driver = Solution()
print(driver.subarraySum([1, 2, 3], 3))
