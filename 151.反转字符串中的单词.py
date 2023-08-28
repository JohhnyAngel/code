# @before-stub-for-debug-begin
from python3problem151 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        i = 0
        j = len(res) - 1
        while i<j:
            res[i], res[j] = res[j], res[i]
            j -= 1
            i += 1
        return " ".join(res)
# @lc code=end

