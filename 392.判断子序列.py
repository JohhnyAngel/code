#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)+1
        m = len(t)+1
        dp = [[0]*m for _ in range(n)]
        result = 0
        for i in range(1, n):
            for j in range(1, m):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == len(s):
            return True
        return False
# @lc code=end

