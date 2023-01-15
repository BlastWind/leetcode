from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window
        # increase window until window is "good", add len(nums) - window_end to total
        # once "good", shrink window_start, for each shrink
            # if still "good", add len(nums) - window_end 
            # if no longer "good", we can start expanding right border again

        # the window itself maintains a freq table of numbers and the number of good indices
        total = 0

        left, right = 0, 0
        # freq = [0] * 11
        freq = defaultdict(int)
        good_indices = 0
        
        freq[nums[0]] = 1
        while right >= left and right < len(nums) - 1: 
            right += 1
            new_num = nums[right]
            good_indices += freq[new_num] # adds the count of equal nums that have smaller indices!
            freq[nums[right]] += 1 
            
            if good_indices >= k: 
                total += len(nums) - (right)

                while good_indices >= k and right > left: 
                    freq[nums[left]] -= 1 
                    good_indices -= freq[nums[left]] # double check later
                    
                    if good_indices >= k: 
                        total += len(nums) - (right)
                    left += 1

        return total

