"""
给定一个整数数组 nums 和一个整数目标值 target，ddawd
请你在该数组中找出 和为目标值 target  的那 两个 整数，
并返回它们的数组下标。
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        lst = []
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    lst.append(i)
                    lst.append(j)
        return lst
    
sl = Solution()
print(sl.twoSum([3,2,4],6))