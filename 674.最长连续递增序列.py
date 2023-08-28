#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)
# @lc code=end

