# @before-stub-for-debug-begin
from python3problem300 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
# @lc code=end

