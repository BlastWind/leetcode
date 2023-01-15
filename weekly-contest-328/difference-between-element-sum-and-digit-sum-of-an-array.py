from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = 0 
        for ele in nums: 
            for digit in str(ele):
                digitSum += int(digit)

        return abs(elementSum - digitSum)