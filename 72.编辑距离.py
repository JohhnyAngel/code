#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        for i in range(1,n):
            for j in range(1,m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

