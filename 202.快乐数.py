#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            sum = 0
            nstr = str(n)
            for i in nstr:
                sum += int(i)**2
            if sum == 1:
                return True
            n = sum
        return False
# @lc code=end

