# @before-stub-for-debug-begin
from python3problem583 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        for i in range(n):
            for j in range(m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]

# @lc code=end

