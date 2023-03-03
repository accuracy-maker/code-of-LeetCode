"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        n = len(nums1)
        if n%2==0:
            return (nums1[n//2]+nums1[(n//2)-1])/2
        else:
            return (nums1[n//2])