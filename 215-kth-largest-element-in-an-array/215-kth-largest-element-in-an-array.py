from heapq import heapify, heappop, heappushpop
from itertools import islice
from queue import PriorityQueue
import random
from typing import List
class Solution:
    # we maintain a minheap of length k
    # After each iteration, the heap must contain the n largest elements in the array traversed thus far
    # The head item must be the smallest item, and is the nth largest element in the array traversed thus far
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)


    def findKthLargest2(self, nums: List[int], k: int):

        # put elements smaller than nums[pivot_index] to its left and larger eles to its right
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # move pivot out of the way (to the end)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot: 
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index+=1
            nums[right], nums[store_index] = nums[store_index],  nums[right]
            return store_index
        def select(left, right, k_smallest: int):
            if left == right: return nums[left]
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else: 
                return select(pivot_index + 1, right, k_smallest)
        return select(0, len(nums) - 1, len(nums) - k)
driver = Solution()

# [1, 2, 3, 4, 5, 6], 1st largest = 6, 6th largest = 1
print(driver.findKthLargest2([3, 2, 1, 5, 6, 4], 1))
