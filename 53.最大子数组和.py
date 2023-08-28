# @before-stub-for-debug-begin
from python3problem53 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        result = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            if dp[i] > result:
                result = dp[i]
        return result
            
# @lc code=end

