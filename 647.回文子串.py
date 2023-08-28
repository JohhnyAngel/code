# @before-stub-for-debug-begin
from python3problem647 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1] == True:
                        result += 1
                        dp[i][j] = True
        return result
# @lc code=end

