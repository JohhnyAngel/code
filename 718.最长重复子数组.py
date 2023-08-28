#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)+1
        m = len(nums2)+1
        dp = [[0]*m for _ in range(n)]
        result = -1
        for i in range(1,n):
            for j in range(1,m):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                if dp[i][j] > result:
                    result = dp[i][j]
        return result

# @lc code=end

