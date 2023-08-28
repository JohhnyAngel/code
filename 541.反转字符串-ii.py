# @before-stub-for-debug-begin
from python3problem541 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverse(self, s: list) -> str:
        i = 0
        j = len(s) - 1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
    def reverseStr(self, s: str, k: int) -> str:
        slist = list(s)
        for i in range(0, len(slist), 2*k):
            if i+k <= len(slist):
                slist[i:i+k] = self.reverse(slist[i:i+k])
            else:
                slist[i:] = self.reverse(slist[i:])
        return "".join(slist)

# @lc code=end

