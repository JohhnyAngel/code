# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        window = Counter()
        i, count, result = 0, 0, float('inf')
        for j in range(len(s)):
            c = s[j]
            window[c] += 1
            if c in need:
                if window[c] == need[c]:
                    count += 1
                while count == len(need):
                    result = min(result, j-i+1)
                    a = s[i]
                    if a in need and window[a] == need[a]:
                        count -= 1
                    window[a] -= 1
                    if j-i+1 <= result:
                        start = i
                    i += 1
        return s[start:start+result] if result != float('inf') else ""

        
        
        
# @lc code=end

