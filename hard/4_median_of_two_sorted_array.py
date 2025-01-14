from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        absolute = nums1 + nums2
        absolute.sort()
        return absolute[len(absolute)//2] if len(absolute) % 2 == 1 else (absolute[len(absolute)//2] + absolute[(len(absolute)//2) - 1]) / 2