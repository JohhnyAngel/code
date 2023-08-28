#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = {}
        for i in magazine:
            record[i] = record.get(i,0) + 1
        for i in ransomNote:
            if i not in record or not record[i]:
                return False
            record[i] -= 1
        return True
# @lc code=end

