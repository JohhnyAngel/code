#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        L = len(s)
        for i in range(1, L//2 + 1):
            if L % i == 0:
                substr = s[:i]
                if substr*(L//i) == s:
                    return True
        return False
# @lc code=end

