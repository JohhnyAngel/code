#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def getnext(self, next:List[int], s: str):
        next[0] = 0
        j = 0 # j 为s[:i+1]相同子字符串前缀长度及前缀的后一个字符
        for i in range(1,len(s)):
            while j > 0 and s[i] != s[j]: 
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
    def strStr(self, haystack: str, needle: str) -> int:
        next = [0]*len(needle)
        self.getnext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while haystack[i] != needle[j] and j > 0:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1

# @lc code=end

