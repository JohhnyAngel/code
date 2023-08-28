# @before-stub-for-debug-begin
from python3problem344 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        """
        Do not return anything, modify s in-place instead.
        """
# @lc code=end

