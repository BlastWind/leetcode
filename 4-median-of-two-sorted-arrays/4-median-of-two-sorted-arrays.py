from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        totalL = len(nums2) + len(nums1)
        while True: 
            m = (l + r) // 2
            m2 = (totalL // 2) - (m + 2) # m + 1 is index m to length it covers; the other +1 is conversion from the aforementioned length back to index
            ALeft = nums1[m] if m >= 0 else float("-infinity")
            ARight = nums1[m+1] if m + 1 < len(nums1) else float("infinity")
            BLeft = nums2[m2] if m2 >= 0 else float("-infinity")
            BRight = nums2[m2+1] if m2 + 1 < len(nums2) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight: 
                if (len(nums2) + len(nums1)) % 2: 
                    # odd 
                    return min(ARight, BRight)
                else: 
                    print(ALeft, ARight, BLeft, BRight)
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight: 
                # there needs to be less elements in nums1
                r = m - 1
            else: 
                # there needs to be more elments in nums1 
                l = m + 1


driver = Solution()
print(driver.findMedianSortedArrays([1, 2], [3, 4]))
