# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums)-1, len(nums)-1
        result = [float('inf')] * len(nums)
        while i<=j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                result[k] = nums[i]*nums[i]
                i += 1
            else:
                result[k] = nums[j]*nums[j]
                j -= 1
            k -= 1
        return result
# @lc code=end

