# Extension question from https://leetcode.com/discuss/interview-question/351782/Google-or-Phone-Screen-or-Kth-Largest-Element-of-Two-Sorted-Arrays

from typing import List

def kth_smallest_element(nums1: List[int], nums2: List[int], k) -> int:
	len1, len2 = len(nums1), len(nums2)
	# hypothetically, nums1 has same length has nums2
	# Then, make nums1 take k // 2 elements and make nums2 take k // 2 elements
	# If nums2's middle element taken is greater than nums1's middle element taken, expand nums1's takings and shrink nums2's takings.
	# vice versa
	 
	# but say len nums1 == 10 but len nums2 == 100	
	return 89