#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = [0]*26
        for i in s:
            hash[ord(i) - ord('a')] += 1
        for i in t:
            hash[ord(i) - ord('a')] -= 1
        for i in hash:
            if i != 0:
                return False
        return True

# @lc code=end

