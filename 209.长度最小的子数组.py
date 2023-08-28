# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum1 = 0
        result = float('inf')
        for j in range(len(nums)):
            sum1 += nums[j]
            while sum1 >= target:
                sum1 -= nums[i]
                result = min(j-i+1, result)
                i += 1
        return 0 if result == float('inf') else result
# @lc code=end

