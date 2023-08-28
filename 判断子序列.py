class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)+1
        m = len(t)+1
        dp = [[0]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                a = s[i-1]
                b = t[j-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == len(s):
            return True
        return False

solu = Solution()
s = "ace"
t = "abc"
result = solu.isSubsequence(s,t)