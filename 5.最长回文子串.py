#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        record = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                        if j-i+1 > record:
                            record = j-i+1
                            result = s[i:j+1]
                    else:
                        if dp[i+1][j-1] == True:
                            dp[i][j] = True
                            if j-i+1 > record:
                                record = j-i+1
                                result = s[i:j+1]
        return result
# @lc code=end

