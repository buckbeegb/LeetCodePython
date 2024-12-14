
# Solution for Problem 4: Median of Two Sorted Arrays
from typing import Optional
from math import log10

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        left_counter = 0
        right_counter = 0
        final_list = []
        while left_counter < len(nums1) or right_counter < len(nums2):
            if right_counter == len(nums2) or (left_counter < len(nums1) and nums1[left_counter] < nums2[right_counter]):
                final_list.append(nums1[left_counter])
                left_counter += 1
            else:
                final_list.append(nums2[right_counter])
                right_counter += 1
        if len(final_list) % 2 == 0:
            median = float((final_list[len(final_list)//2] + final_list[len(final_list)//2 - 1]) / 2)
        else:
            print(final_list)
            median = float(final_list[len(final_list)//2])
        return median



sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
# nums1 = [1,3]
# nums2 = [2]
sol.findMedianSortedArrays(nums1, nums2)
