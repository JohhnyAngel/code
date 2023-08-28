# @before-stub-for-debug-begin
from python3problem115 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s) + 1
        m = len(t) + 1
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# @lc code=end

