# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def nSum(self, n, nums, target):
        res = []
        if n == 2:
            i = 0
            j = len(nums)-1
            while i < j:
                if nums[i]+nums[j] < target:
                        i += 1
                elif nums[i]+nums[j] > target:
                        j -= 1
                else:
                    res.append([nums[i], nums[j]])
                    while i < j and nums[i+1] == nums[i]:
                        i += 1
                    while i < j and nums[j-1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1
            return res
        
        else:
            i = 0
            while i < len(nums):
                sub = self.nSum(n-1, nums[i+1:], target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                     i += 1
                i += 1
            return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = self.nSum(3, nums, 0)
        return result


# @lc code=end

